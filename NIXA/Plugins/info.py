from NIXA.main import bot
from pyrogram import filters


OWNER = [5513481385]
sudos = [5119324429]



@bot.on_message(filters.command('id'))
def ids(_, message):
    reply = message.reply_to_message
    if reply:
        message.reply_text(
            f"**ʏᴏᴜʀ ɪᴅ**: `{message.from_user.id}`\n**{reply.from_user.first_name}'s ɪᴅ**: `{reply.from_user.id}`\n**ᴄʜᴀᴛ ɪᴅ**: `{message.chat.id}`"
        )
    else:
        message.reply(
            f"**ʏᴏᴜʀ ɪᴅ**: `{message.from_user.id}`\n**ᴄʜᴀᴛ ɪᴅ**: `{message.chat.id}`"
        )


@bot.on_message(filters.command("info"))
def info(_, message):
    if message.text == "/info":
        user = message.from_user.id
    if message.reply_to_message:
        user = message.reply_to_message.from_user.id
    if not message.reply_to_message and message.text != "/info" and user.isnumeric(
    ):
        user = message.text.split(" ")[1]

    if not message.reply_to_message and message.text != "/info" and not user.isnumeric(
    ):
        k = bot.get_users(message.text.split(" ")[1])
        user = k.id

    if user == OWNER:
        status = "ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴍʏ ᴏᴡɴᴇʀ"

    elif user in sudos:
        status = "ᴛʜɪs ᴘᴇʀsᴏɴ ɪs ᴏɴᴇ ᴏғ ᴍʏ sᴜᴅᴏ ᴜsᴇʀs !"

    else:
        status = "ᴍᴇᴍʙᴇʀ"

    pfp_count = bot.get_profile_photos_count(user)

    if not pfp_count == 0:
        pfp = bot.get_profile_photos(user, limit=1)
        pfp_ = pfp[0]['thumbs'][0]['file_id']

    foo = bot.get_users(user)
    data = f"""**ғɪʀsᴛ ɴᴀᴍᴇ** : {foo.first_name}
**ʟᴀsᴛ ɴᴀᴍᴇ**: {foo.last_name}
**ᴛᴇʟᴇɢʀᴀᴍ ɪᴅ**: {foo.id}
**ᴘᴇʀᴍᴀʟɪɴᴋ**: {foo.mention(foo.first_name)}
**ɪs_ʙᴏᴛ**: {foo.is_bot}
**sᴛᴀᴛᴜs**: {status}
"""

    if pfp_count != 0:
        message.reply_photo(pfp_, caption=data)

    else:
        message.reply_text(data)
