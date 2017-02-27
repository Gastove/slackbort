### Hi! I'm Slackbort

Slackbort here. I'm a terrible slackbot. I just sort of shout in to a Slack
channel if I can find the creds.

Here's how to do the Slackbort:

``` shell
git clone <the slackbort uri> && cd slackbort
mkvirtualenv slackbort
pip install -r requirements.txt
cp auth.cfg.tpl auth.cfg
<edit auth.cfg to contain your API token>
python slackbort -h # Prints usage options!

# For instance:
python slackbort -c borttorst -m "IM IN YER SLACKS, BEIN OLD WOMENZ"
```
