import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "82a94d416e05ca5cc3bc04da8494d7ca"))
API_HASH = getenv("API_HASH", "20798317")

BOT_TOKEN = getenv("BOT_TOKEN", "6829228356:AAFmAyxceIPu6alCxoIZMFOG-LZ9PrV3mNg")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://VamsixD:VamsixD@vamsi.x7gyybv.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1002141779241"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "𝙅𝙚𝙨𝙨𝙮 ✘ 𝙈𝙪𝙨𝙞𝙘")

OWNER_ID = list(map(int, getenv("OWNER_ID", "6439286014").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/dattudd/Whitemusic")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/its_dev_telegram")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/its_dev_telegram")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "5000"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "5ab40dd28a9943ea83c63ec737e62039")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "217085ffa4224f1aa335174e457a462c")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "BQE9W20Ab9lwY5vg09bEH3URyeSCgm0YnUpJs8Tq6cjFallCX9Z7TOW5aO0DQyYTco0OxocCtL-UBF_ohcjEHKpCIuABTiRK0vl3slQ5ETwMv4Ctnq3EPUBbQe2anXFxXgzojStaa7x1QQSE53IIF7BwrPlr8ALO6AF26p6DepWorPd7MJf3ZKPrttJMcxJJGL99iloxDBLdXDiPTHjVj867S6RH8oIoUnmHNxVDqVzjSsVvICmvmzhlN2Eq6C05PRB_lPBzFex-5eJRCH6vwr21pnf-NLWqqF5I5MaqfEstHGkUiJW5tVFo65GzzFBkEAflJSxgYwKsyxCpgOnAmD8tearfXwAAAAGbCUdtAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "logs.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://telegra.ph/file/5663815f7a0bcd927dff8.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://telegra.ph/file/5663815f7a0bcd927dff8.jpg",
)

PLAYLIST_IMG_URL = "https://te.legra.ph/file/3b4a340465a75c1c40eb6.jpg"

GLOBAL_IMG_URL = "https://te.legra.ph/file/3b4a340465a75c1c40eb6.jpg"

STATS_IMG_URL = "https://telegra.ph/file/5663815f7a0bcd927dff8.jpg"

TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/3b4a340465a75c1c40eb6.jpg"

TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/3b4a340465a75c1c40eb6.jpg"

STREAM_IMG_URL = "https://te.legra.ph/file/3b4a340465a75c1c40eb6.jpg"

SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/3b4a340465a75c1c40eb6.jpg"

YOUTUBE_IMG_URL = "https://te.legra.ph/file/3b4a340465a75c1c40eb6.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/3b4a340465a75c1c40eb6.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/3b4a340465a75c1c40eb6.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/3b4a340465a75c1c40eb6.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://telegra.ph/file/5663815f7a0bcd927dff8.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://telegra.ph/file/5663815f7a0bcd927dff8.jpg"
