#!/usr/bin/env python

import requests

import argparse
from ConfigParser import ConfigParser

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
    resp = requests.post(URL, params=params)
    return resp


def form_params(msg, chan, auth):
    built_params = BASE_PARAMS.copy()
    built_params['text'] = msg
    built_params['channel'] = chan
    built_params['token'] = auth

    return built_params


def make_argument_parser():
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
