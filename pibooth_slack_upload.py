# -*- coding: utf-8 -*-

"""pibooth plugin for uploading pictures to Slack channel"""

import os
import subprocess

import pibooth
from pibooth.utils import LOGGER


__version__ = "1.0.0"

SECTION = 'SLACK'
SLACK_BASE_URL = 'https://slack.com'

@pibooth.hookimpl
def pibooth_configure(cfg):
    """Declare the new configuration options"""
    cfg.add_option(SECTION, 'slack_token', '', "Slack Token")
    cfg.add_option(SECTION, 'slack_channel_id', '', "Slack Channel Id")


@pibooth.hookimpl
def pibooth_startup(app, cfg):
    """Verify Slack credentials"""
    slack_token = cfg.get(SECTION, 'slack_token')
    slack_channel_id = cfg.get(SECTION, 'slack_channel_id')

    if not slack_token:
        LOGGER.error("Slack Token not defined in ["+SECTION+"][slack_token], uploading deactivated")
    elif not slack_channel_id:
        LOGGER.error("Slack Channel Id not defined in ["+SECTION+"][slack_channel_id], uploading deactivated")
    else:
        LOGGER.info("Enabled Slack upload")
        app.slack_upload_enabled = True


@pibooth.hookimpl
def state_processing_exit(app, cfg):
    """Upload picture to Slack Channel"""
    if hasattr(app, 'slack_upload_enabled'):
        LOGGER.info("Attempting to upload file to slack: {}".format(app.previous_picture_file))

        slack_token = cfg.get(SECTION, 'slack_token').strip('"')
        slack_channel_id = cfg.get(SECTION, 'slack_channel_id').strip('"')

        curl_cmd = subprocess.run(
            [
                "curl",
                "{}/api/files.upload".format(SLACK_BASE_URL),
                "-H", "Authorization: Bearer {}".format(slack_token),
                "-F", "file=@{}".format(app.previous_picture_file),
                "-F", "channels={}".format(slack_channel_id),
                "--silent",
                "--show-error"
            ],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if curl_cmd.returncode == 0:
            LOGGER.info("File uploaded to Slack successfully!")
        else:
            LOGGER.error("Upload to Slack failed!")
