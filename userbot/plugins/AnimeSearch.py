#By @WhySooSerious,Kangers can Take the Credits 😋
import datetime
import asyncio
from telethon import events
from telethon.errors.rpcerrorlist import YouBlockedUserError, UserAlreadyParticipantError
from telethon.tl.functions.account import UpdateNotifySettingsRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from userbot.utils import admin_cmd
import time
 
from userbot import ALIVE_NAME
naam = str(ALIVE_NAME)

bot = "@AniFluidbot"
 

@borg.on(admin_cmd(pattern="urband ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@KeikoSDbot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1212429864))
              await event.client.send_message(chat, "/ud {}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Master! Please Unblock (@KeikoSDbot) ```")
              return
          if response.text.startswith("Country"):
             await event.edit("😶**Country Not Found**😅\n\n[🔴🔴🔴🔴\n ⏩⏩ How to use ⏪⏪\n🔵🔵🔵🔵](https://t.me/Dev_OwO)")
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

@borg.on(admin_cmd(pattern="sanime ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@AniFluidbot"
    await event.edit("```Checking...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=1072580256))
              await event.client.send_message(chat, "/anime {}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Master! Please Unblock (@AniFluidbot) ```")
              return
          if response.text.startswith("🕒"):
             await event.edit("**please wait..**")
             await event.client.send_message(event.chat_id, response.message)
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)

@borg.on(admin_cmd(pattern="ssanime ?(.*)"))
async def _(event):
    if event.fwd_from:
        return 
    input_str = event.pattern_match.group(1)
    reply_message = await event.get_reply_message()
    chat = "@NepGearbot"
    await event.edit("```Fetching Details...```")
    async with event.client.conversation(chat) as conv:
          try:     
              response = conv.wait_event(events.NewMessage(incoming=True,from_users=778490365))
              await event.client.send_message(chat, "/anime {}".format(input_str))
              response = await response 
          except YouBlockedUserError: 
              await event.reply("```Master! Please Unblock (@AniFluidbot) ```")
              return
          if response.text.startswith("🕒"):
             await event.edit("**please wait..**")
             await event.client.send_message(event.chat_id, response.message)
          else: 
             await event.delete()
             await event.client.send_message(event.chat_id, response.message)
