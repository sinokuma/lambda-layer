import json
import logging
import re
import urllib.request

logger = logging.getLogger()
logger.setLevel(logging.INFO)

pattern = 'https?://[\\w/:%#\\$&\\?\\(\\)~\\.=\\+\\-]+'

def notify(webhook_url, message, username=None, icon_emoji=None):
    """Post message to Slack

    Arguments:
        webhook_url {string} -- Slack webhook URL
        message {string} -- Message contents
        username {string} -- Slack display user name
        icon_emoji {string} -- Slack display emoji-icon (e.g. :hogehoge:)

    Returns:
        [integer] -- HTTP status code of response
    """
    if not re.match(pattern, webhook_url):
        logger.error('Webhook URL is invalid.')
        return 400
    else:
        send_data = __create_send_data(username, icon_emoji, message)
        if not 'text' in send_data:
            logger.error('Message is required.')
            return 400
        else:
            payload = 'payload=' + json.dumps(send_data)
            request = urllib.request.Request(webhook_url, data=payload.encode('utf-8'), method='POST')
            try:
                with urllib.request.urlopen(request) as response:
                    return response.getcode()
            except urllib.error.HTTPError as err:
                logger.error(err.reason)
                return err.code
            except urllib.error.URLError as err:
                logger.error(err.reason)
                return None

def __create_send_data(username, icon_emoji, message):
    """Create sending data

    Arguments:
        username {string} -- Slack display user name
        icon_emoji {string} -- Slack display emoji-icon (e.g. :hogehoge:)
        message {string} -- Message contents

    Returns:
        [dict] -- Sending data for JSON payload
    """
    msg = {}
    if username:
        msg['username'] = username
    if icon_emoji:
        msg['icon_emoji'] = icon_emoji
    if message:
        msg['text'] = message
    return msg

def test_notify():
    assert notify(
        webhook_url='SLACK_WEBHOOK_URL',
        message='This is test message.'
        ) == 200
    assert notify(
        webhook_url='SLACK_WEBHOOK_URL',
        message=''
        ) == 400
    assert notify(
        webhook_url='SLACK_WEBHOOK_URL',
        message=None
        ) == 400
    assert notify(
        webhook_url='ftp://invalid-url-example.com/hogehoge',
        message='This is test message.'
        ) == 400
    assert notify(
        webhook_url='SLACK_WEBHOOK_URL',
        message='This is test message.',
        username='username',
        icon_emoji=':toshizo:'
    ) == 200
