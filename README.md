pibooth-slack-upload
=================

[![Python 3.6+](https://img.shields.io/badge/python-3.6+-red.svg)](https://www.python.org/downloads)

[![PyPi package](https://badge.fury.io/py/pibooth-slack-upload.svg)](https://pypi.org/project/pibooth-slack-upload)
[![PyPi downloads](https://img.shields.io/pypi/dm/pibooth-slack-upload?color=purple)](https://pypi.org/project/pibooth-slack-upload)

`pibooth-slack-upload` is a plugin for the [pibooth](https://pypi.org/project/pibooth) application.

Permits upload of pictures to a Slack channel. Plugin requires an internet connection.

Install
-------

```shell
pip3 install pibooth-slack-upload
```

Configuration
-------------

Below are the new configuration options available in the [pibooth](https://pypi.org/project/pibooth) configuration. **The keys and their default values are automatically added to your configuration after first** [pibooth](https://pypi.org/project/pibooth) **restart.**

``` {.ini}
[SLACK]

# Slack Token
slack_token =

# Slack Channel Id
slack_channel_id =

```

### Note

Edit the configuration by running the command `pibooth --config`.
