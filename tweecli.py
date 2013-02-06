#!/usr/bin/python

import argparse
import tweepy
import ConfigParser
from os.path import expanduser

parser = argparse.ArgumentParser()
parser.add_argument("message")
args = parser.parse_args()
if len(args.message) > 140:
    print "Message is too long, max 140 characters."
    exit()

home = expanduser("~")
config = ConfigParser.ConfigParser()
config.read(home + '/.tweeclirc')

auth = tweepy.OAuthHandler(
    config.get('tweecli', 'consumer_key'),
    config.get('tweecli', 'consumer_secret')
)
auth.set_access_token(
    config.get('tweecli', 'access_token'),
    config.get('tweecli', 'access_token_secret')
)

api = tweepy.API(auth)
api.update_status(args.message)
