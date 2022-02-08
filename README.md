# MundusBot

Latest Version: 1.0 "GENESIS"

A telegram bot written in Python 3.9 for a private server, but can now be used anywhere.

This bot requires you to expose your Bot token as an environemnt variable called ```BOT_TOKEN``` in all instances, so locally (can be done with dotenv if desired), as well as when hosted.

Requires a few libraries to get running, for an easy install you can just run ```pip3 install -r requirements.txt``` from the root directory.

# 1.0 'GENESIS' Changelog

* Begining stages of a MEME bot mimicing another priavte chat bot that has an actual use case, see the repo this was forked from for an actual bot use case

* Added a plethora of meme commands associated with the ELP group for the users enjoyment

* Hosted on GCP's Cloud Run service, which utilizes gunicorn to run a virtual environment for HTTP requests

* Webhook is configured for bot updates (see Telegram bot API docs for more info)

* See [custom functions](./lib/custom.py) for a detailed list of stickers, gifs and memes that can be requested from a chat

* Added a custom getwojakindex function for working with the wojakindex.xyz API

* ```settings.json``` is all but deprecated, since this bot does not use a database, however it may be easier for you to run this bot locally using the ```settings.json``` file

## Donations

kodymaus.eth

*jk, pls don't donate, this was just for fun*
