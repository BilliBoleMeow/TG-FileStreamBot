# This file is a part of TG-FileStreamBot
# Coding : Jyothis Jayanth [@EverythingSuckz]

import logging
from pyrogram import filters, errors
from WebStreamer.vars import Var
from urllib.parse import quote_plus
from WebStreamer.bot import StreamBot, logger
from WebStreamer.utils import get_hash, get_name
from pyrogram.enums.parse_mode import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant


@StreamBot.on_message(
    filters.private
    & (
        filters.document
        | filters.video
        | filters.audio
        | filters.animation
        | filters.voice
        | filters.video_note
        | filters.photo
        | filters.sticker
    ),
    group=4,
)
async def media_receive_handler(_, m: Message):
    banned_users = Var.BANNED_USERS.split() if Var.BANNED_USERS else []
    if str(m.from_user.id) in banned_users:
        return await m.reply("You are banned from using this bot.", quote=True)

    try:
        user = await client.get_chat_member(Var.UPDATES_CHANNEL, user_id=m.from_user.id)
    except UserNotParticipant:
        return await m.reply(text="""<i>Join The Update Channel To Use Me.</i>""",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Join Now", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ],
                ))

    try:
        log_msg = await m.forward(chat_id=Var.BIN_CHANNEL)
        
        file_hash = get_hash(log_msg, Var.HASH_LENGTH)
        stream_link = f"{Var.URL}{log_msg.id}/{quote_plus(get_name(m))}?hash={file_hash}"
        short_link = f"{Var.URL}{file_hash}{log_msg.id}"
        logger.info(f"Generated link: {stream_link} for {m.from_user.first_name}")
        await m.reply_text(
            text="<code>{}</code>\n(<a href='{}'>shortened</a>)".format(
                stream_link, short_link
            ),
            quote=True,
            parse_mode=ParseMode.HTML,
            reply_markup=InlineKeyboardMarkup(
                [[InlineKeyboardButton("Open", url=stream_link)]]
            ),
        )
        
    except Exception as e:
        logger.exception(e) # Log the error
        await m.reply("Something went wrong. Please contact the bot admin @iamLiquidX for support.", quote=True)
