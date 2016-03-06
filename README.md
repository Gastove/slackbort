### Hi! I'm Slackbort

Slackbort here. I'm a terrible slackbot. I just sort of shout in to a Slack
channel if I can find a Slack Bot User API Token in my `auth.cfg`. Assuming I
can, I work a little like this:

#### Get help:
``` shell
$ python slackbort -h
usage: slackbort [-h] [-c CHANNEL] -m MESSAGE

optional arguments:
  -h, --help            show this help message and exit
  -c CHANNEL, --channel CHANNEL
                        Which channel to post to, like #general
  -m MESSAGE, --message MESSAGE
                        A message to post! Surround with quotes.
```

(I know that says "optional arguments," but that's just Python's `argparse`
telling a fib. Channel and Message are both required.)

#### Setup:
Real easy: copy `auth.cfg.tpl` to `auth.cfg` in the main dir of this
project. Replace `<put your secret key here>` with a valid Slack Bot User API
token. Done!
