#!/usr/bin/env python

# Python standard libraries
import argparse
from ConfigParser import ConfigParser

# Third-party libraries
import requests

# Static Constants
URL = "http://slack.com/api/chat.postMessage"
CFG_FILE = "auth.cfg"
CFG = ConfigParser()
CFG.read(CFG_FILE)

BASE_PARAMS = {
    'token': '',
    'channel': '',
    'text': '',
    'username': 'slackbort'
}


def post_chat(params):
    """
    Posts a configured message to the given URL.
    params:
        dict of token, channel, text, and username
    """
    resp = requests.post(URL, params=params)
    return resp


def form_params(msg, chan, auth):
    """
    Builds a complete params dict.
    msg:
        String text to post to slack
    chan:
        Channel to post to
    token:
        Auth token for the slack group being posted to
    """
    built_params = BASE_PARAMS.copy()
    built_params['text'] = msg
    built_params['channel'] = chan
    built_params['token'] = auth

    return built_params


def make_argument_parser():
    """
    Builds a command-line argument parser using Python's argparse
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('-c', '--channel', default='#borttorst',
                        help='Which channel to post to, like #general')
    parser.add_argument('-m', '--message', required=True,
                        help='A message to post! Surround with quotes.')

    return parser


def main():
    parser = make_argument_parser()
    args = parser.parse_args()

    message = args.message
    channel = args.channel
    auth = CFG.get('Auth', 'secret_key')

    params = form_params(message, channel, auth)
    resp = post_chat(params)
    print resp.text


if __name__ == '__main__':
    main()
