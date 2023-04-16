# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

from pyrogram import filters
from pyrogram.types import Message
from WebStreamer.bot import StreamBot
from pyrogram.enums.parse_mode import ParseMode
from WebStreamer.vars import Var
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

@StreamBot.on_message(filters.command(["start", "help"]) & filters.private
async def start(_, m: Message):
    if Var.ALLOWED_USERS and not ((str(m.from_user.id) in Var.ALLOWED_USERS) or (m.from_user.username in Var.ALLOWED_USERS)):
        return await m.reply(
            "You are not in the allowed list of users who can use me. \
            Check <a href='https://github.com/EverythingSuckz/TG-FileStreamBot#optional-vars'>this link</a> for more info.",
            disable_web_page_preview=True, quote=True
        )
    await m.reply(
        text="""
<b>A Simple Telegram File To Link Generation Bot.</b>\n.                           <b>Maintained By 👇</b>""",
            parse_mode=ParseMode.HTML,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup( [ [InlineKeyboardButton('LiquidX', url=f"https://t.me/liquidxprojects")] ]  ))
