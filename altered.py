#!/usr/bin/env python3

import os
import sys
import discord
import asyncio
import json
from functools import reduce


with open(os.path.join(os.path.dirname(__file__), "conf.json")) as conf:
    params = json.load(conf)

token = params["token"]

client = discord.Client()

reboot_on_shutdown = 0

@asyncio.coroutine
def shutdown():
    yield from client.logout()


@client.event
@asyncio.coroutine
def on_ready():
    global ME
    ME = client.user


@client.event
@asyncio.coroutine
def on_message(msg):
    if msg.author == ME:
        return  # Altered should not respond to its own messages


try:
    client.run(token)
except: 
    pass
finally:
    sys.exit(reboot_on_shutdown)
