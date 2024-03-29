from pyrogram import Client, errors
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
)
from youtubesearchpython import VideosSearch
from pyrogram.types import (
  CallbackQuery,
  InlineKeyboardButton,
  InlineKeyboardMarkup,
  Message,
)

def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        videoid = data["id"]
        return [songname, url, duration, thumbnail, videoid]
    except Exception as e:
        print(e)
        return 0

def stream_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/TeleBotxSupport"),
      InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url="https://t.me/TeleBotsUpdate"),
    ],
    [
      InlineKeyboardButton(text="✚ ᴍᴇɴᴜ", callback_data="cbmenu"),
      InlineKeyboardButton(text="⟳ ᴄʟᴏsᴇ", callback_data="cls"),
    ],
  ]
  return buttons

def menu_markup(user_id):
  buttons = [
     [
      InlineKeyboardButton(text="II", callback_data=f'cbpause | {user_id}'),
      InlineKeyboardButton(text="▷", callback_data=f'cbresume | {user_id}')
     ],
     [
      InlineKeyboardButton(text="‣‣I", callback_data=f'cbskip | {user_id}'),
      InlineKeyboardButton(text="▢", callback_data=f'cbstop | {user_id}')
     ],
     [
      InlineKeyboardButton(text="🔇", callback_data=f'cbmute | {user_id}'),
      InlineKeyboardButton(text="ᴜᴩᴅᴀᴛᴇs", url=f"https://t.me/TeleBotxSupport"),
      InlineKeyboardButton(text="🔊", callback_data=f'cbunmute | {user_id}')
     ],
     [
      InlineKeyboardButton(text="ɢᴏ ʙᴀᴄᴋ",callback_data="cbhome")
     ],
  ]   
  return buttons



def audio_markup(user_id):
  buttons = [
    [
      InlineKeyboardButton(text="sᴜᴘᴘᴏʀᴛ", url="https://t.me/TeleBotxSupport"),
      InlineKeyboardButton(text="ᴜᴘᴅᴀᴛᴇs", url="https://t.me/TeleBotsUpdate"),
    ],
    [
      InlineKeyboardButton(text="✚ ᴍᴇɴᴜ", callback_data="cbmenu"),
      InlineKeyboardButton(text="⟳ ᴄʟᴏsᴇ", callback_data="cls"),
    ],
  ]
  return buttons




def song_download_markup(videoid):
    buttons = [
        [
            InlineKeyboardButton(
                text="⬇️ ᴀᴜᴅɪᴏ",
                callback_data=f"gets audio|{videoid}",
            ),
            InlineKeyboardButton(
                text="⬇️ ᴠɪᴅᴇᴏ",
                callback_data=f"gets video|{videoid}",
            ),
        ],
        [
            InlineKeyboardButton(
                text="ɢᴏ ʙᴀᴄᴋ",
                callback_data="cbhome",
            )
        ],
    ]
    return buttons

 
