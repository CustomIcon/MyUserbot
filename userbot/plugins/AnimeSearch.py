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
 
@borg.on(admin_cmd("sanime ?(.*)"))
async def _(event):
    if event.fwd_from:
        return    
    sysarg = event.pattern_match.group(1)

      async with event.client.conversation(bot) as conv:
          try:
              await conv.send_message("/start")
              response = await conv.get_response()
              await conv.send_message("/anime" + sysarg)
              result = await conv.get_response()
 
              await borg.send_message(event.chat_id, result.text)
 
              await event.delete()


 from uniborg.util import admin_cmd

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

@borg.on(admin_cmd("scharacter ?(.*)"))
 
async def _(event):
 
    if event.fwd_from:
 
        return    
 
    sysarg = event.pattern_match.group(1)
 
      async with event.client.conversation(bot) as conv:
 
          try:
 
              await conv.send_message("/start")
 
              response = await conv.get_response()
 
              await conv.send_message("/character" + sysarg)
 
              audio = await conv.get_response()
 
              await borg.send_message(event.chat_id, audio.text)
 
              await event.delete()
