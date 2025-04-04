#!/usr/bin/env python3
class WZMLStyle:
    # ----------------------
    # async def start(client, message) ---> __main__.py
    ST_BN1_NAME = "OWNER"
    ST_BN1_URL = "https://t.me/Ruban9124"
    ST_BN2_NAME = "SUPPORT"
    ST_BN2_URL = "https://t.me/MadxBotz"
    ST_BN2_NAME = "Buy Premium"
    ST_BN2_URL = "https://t.me/MadxBotzSupport"
    ST_MSG = """<i>𝗧𝗵𝗶𝘀 𝗯𝗼𝘁 𝗰𝗮𝗻 𝗺𝗶𝗿𝗿𝗼𝗿 𝗮𝗹𝗹 𝘆𝗼𝘂𝗿 𝗹𝗶𝗻𝗸𝘀|𝗳𝗶𝗹𝗲𝘀|𝘁𝗼𝗿𝗿𝗲𝗻𝘁𝘀 𝘁𝗼 𝗚𝗼𝗼𝗴𝗹𝗲 𝗗𝗿𝗶𝘃𝗲 𝗼𝗿 𝗮𝗻𝘆 𝗿𝗰𝗹𝗼𝗻𝗲 𝗰𝗹𝗼𝘂𝗱 𝗼𝗿 𝘁𝗼 𝘁𝗲𝗹𝗲𝗴𝗿𝗮𝗺.</i>
<b>Type {help_command} to get a list of available commands</b>"""
    ST_BOTPM = """<i>Now, This bot will send all your files and links here. Start Using ...</i>"""
    ST_UNAUTH = """<i>You Are not authorized user! Deploy your own WZML-X Mirror-Leech bot</i>"""
    OWN_TOKEN_GENERATE = (
        """<b>Temporary Token is not yours!</b>\n\n<i>Kindly generate your own.</i>"""
    )
    USED_TOKEN = (
        """<b>Temporary Token already used!</b>\n\n<i>Kindly generate a new one.</i>"""
    )
    LOGGED_PASSWORD = """<b>Bot Already Logged In via Password</b>\n\n<i>No Need to Accept Temp Tokens.</i>"""
    ACTIVATE_BUTTON = "Activate Temporary Token"
    TOKEN_MSG = """<b><u>Generated Temporary Login Token!</u></b>
<b>Temp Token:</b> <code>{token}</code>
<b>Validity:</b> {validity}"""
    # ---------------------
    # async def token_callback(_, query): ---> __main__.py
    ACTIVATED = "✅️ Activated ✅"
    # ---------------------
    # async def login(_, message): --> __main__.py
    LOGGED_IN = "<b>Already Bot Login In!</b>"
    INVALID_PASS = "<b>Invalid Password!</b>\n\nKindly put the correct Password ."
    PASS_LOGGED = "<b>Bot Permanent Login Successfully!</b>"
    LOGIN_USED = "<b>Bot Login Usage :</b>\n\n<code>/cmd [password]</code>"
    # ---------------------
    # async def log(_, message): ---> __main__.py
    LOG_DISPLAY_BT = "📑 Log Display"
    WEB_PASTE_BT = "📨 Web Paste (SB)"
    # ---------------------
    # async def bot_help(client, message): ---> __main__.py
    BASIC_BT = "Basic"
    USER_BT = "Users"
    MICS_BT = "Mics"
    O_S_BT = "Owner & Sudos"
    CLOSE_BT = "Close"
    HELP_HEADER = "㊂ Help Guide Menu!</i></b>\n\n<b>NOTE: <i>Click on any CMD to see more minor detalis.</i></b>"

    # async def stats(client, message):
    BOT_STATS = """⌬ BOT STATISTICS :</i></b>
┖ <b>Bot Uptime :</b> {bot_uptime}

┎ RAM ( MEMORY ) :</i></b>
┃ {ram_bar} {ram}%
┖ <b>U :</b> {ram_u} | <b>F :</b> {ram_f} | <b>T :</b> {ram_t}

┎ SWAP MEMORY :</i></b>
┃ {swap_bar} {swap}%
┖ <b>U :</b> {swap_u} | <b>F :</b> {swap_f} | <b>T :</b> {swap_t}

┎ DISK :</i></b>
┃ {disk_bar} {disk}%
┃ <b>Total Disk Read :</b> {disk_read}
┃ <b>Total Disk Write :</b> {disk_write}
┖ <b>U :</b> {disk_u} | <b>F :</b> {disk_f} | <b>T :</b> {disk_t}
    
    """
    SYS_STATS = """⌬ OS SYSTEM :</i></b>
┠ <b>OS Uptime :</b> {os_uptime}
┠ <b>OS Version :</b> {os_version}
┖ <b>OS Arch :</b> {os_arch}

⌬ NETWORK STATS :</i></b>
┠ <b>Upload Data:</b> {up_data}
┠ <b>Download Data:</b> {dl_data}
┠ <b>Pkts Sent:</b> {pkt_sent}k
┠ <b>Pkts Received:</b> {pkt_recv}k
┖ <b>Total I/O Data:</b> {tl_data}

┎ <b>CPU :</b>
┃ {cpu_bar} {cpu}%
┠ <b>CPU Frequency :</b> {cpu_freq}
┠ <b>System Avg Load :</b> {sys_load}
┠ <b>P-Core(s) :</b> {p_core} | <b>V-Core(s) :</b> {v_core}
┠ <b>Total Core(s) :</b> {total_core}
┖ <b>Usable CPU(s) :</b> {cpu_use}
    """
    REPO_STATS = """⌬ REPO STATISTICS :</i></b>
┠ <b>Bot Updated :</b> {last_commit}
┠ <b>Current Version :</b> {bot_version}
┠ <b>Latest Version :</b> {lat_version}
┖ <b>Last ChangeLog :</b> {commit_details}

⌬ <b>REMARKS :</b> <code>{remarks}</code>
    """
    BOT_LIMITS = """⌬ BOT LIMITATIONS :</i></b>
┠ <b>Direct Limit :</b> {DL} GB
┠ <b>Torrent Limit :</b> {TL} GB
┠ <b>GDrive Limit :</b> {GL} GB
┠ <b>YT-DLP Limit :</b> {YL} GB
┠ <b>Playlist Limit :</b> {PL}
┠ <b>Mega Limit :</b> {ML} GB
┠ <b>Clone Limit :</b> {CL} GB
┖ <b>Leech Limit :</b> {LL} GB

┎ <b>Token Validity :</b> {TV}
┠ <b>User Time Limit :</b> {UTI} / task
┠ <b>User Parallel Tasks :</b> {UT}
┖ <b>Bot Parallel Tasks :</b> {BT}
    """
    # ---------------------

    # async def restart(client, message): ---> __main__.py
    RESTARTING = "<i>Restarting...</i>"
    # ---------------------

    # async def restart_notification(): ---> __main__.py
    RESTART_SUCCESS = """⌬ Restarted Successfully!</i></b>
┠ <b>Date:</b> {date}
┠ <b>Time:</b> {time}
┠ <b>TimeZone:</b> {timz}
┖ <b>Version:</b> {version}"""
    RESTARTED = """⌬ Bot Restarted!</i></b>"""
    # ---------------------

    # async def ping(client, message): ---> __main__.py
    PING = "<i>Starting Ping..</i>"
    PING_VALUE = "<b>Pong</b>\n<code>{value} ms..</code>"
    # ---------------------

    # async def onDownloadStart(self): --> tasks_listener.py
    LINKS_START = """Task Started</i></b>
┠ <b>Mode:</b> {Mode}
┖ <b>By:</b> {Tag}\n\n"""
    LINKS_SOURCE = """➲ <b>Source:</b>
┖ <b>Added On:</b> {On}
------------------------------------------
{Source}
------------------------------------------\n\n"""

    # async def __msg_to_reply(self): ---> pyrogramEngine.py
    PM_START = "➲<b><u>𝙃𝙪𝙧𝙧𝙖𝙮 🥳\n\n 𝙏𝙖𝙨𝙠 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 :</u></b>\n┃\n┖ <b>𝗟𝗶𝗻𝗸:</b> <a href='{msg_link}'>𝘾𝙡𝙞𝙘𝙠 𝙃𝙚𝙧𝙚</a>"
    L_LOG_START = "➲ <b><u>𝙇𝙚𝙚𝙘𝙝 𝙎𝙩𝙖𝙧𝙩𝙚𝙙 :</u></b>\n┃\n┠ <b>𝗨𝘀𝗲𝗿 :</b> {mention} ( #ID{uid} )\n┖ <b>𝗦𝗼𝘂𝗿𝗰𝗲 :</b> <a href='{msg_link}'>𝘾𝙡𝙞𝙘𝙠 𝙃𝙚𝙧𝙚</a>"

    # async def onUploadComplete(): ---> tasks_listener.py
    NAME = "🚀 {Name}</i>\n\n"
    SIZE = "┌  <b>📦 sɪᴢᴇ : </b> {Size}\n"
    ELAPSE = "├  <b>♻️ ᴇʟᴀᴘsᴇᴅ :</b> {Time}\n"
    MODE = "├  <b>⚙️ ᴍᴏᴅᴇ:</b> {Mode}\n"

    # ----- LEECH -------
    L_TOTAL_FILES = "├  <b>🗂️ ᴛᴏᴛᴀʟ ꜰɪʟᴇs :</b> {Files}\n"
    L_CORRUPTED_FILES = "├  <b>🗂️ ᴄᴏʀʀᴜᴘᴛᴇᴅ ꜰɪʟᴇs :</b> {Corrupt}\n"
    L_CC = "└  <b>👷 ʙʏ : </b>{Tag}\n\n"
    PM_BOT_MSG = "➲ 𝗙𝗶𝗹𝗲(𝘀) 𝗵𝗮𝘃𝗲 𝗯𝗲𝗲𝗻 𝗦𝗲𝗻𝘁 𝗮𝗯𝗼𝘃𝗲</i></b>"
    L_BOT_MSG = "➲ 𝗙𝗶𝗹𝗲(𝘀) 𝗵𝗮𝘃𝗲 𝗯𝗲𝗲𝗻 𝗦𝗲𝗻𝘁 𝘁𝗼 𝗕𝗼𝘁 𝗣𝗠 (𝗣𝗿𝗶𝘃𝗮𝘁𝗲)"
    L_LL_MSG = "➲ 𝗙𝗶𝗹𝗲(𝘀) 𝗵𝗮𝘃𝗲 𝗯𝗲𝗲𝗻 𝗦𝗲𝗻𝘁. 𝗔𝗰𝗰𝗲𝘀𝘀 𝘃𝗶𝗮 𝗟𝗶𝗻𝗸𝘀...\n"

    # ----- MIRROR -------
    M_TYPE = "├  <b>⚙️ ᴛʏᴘᴇ :</b> {Mimetype}\n"
    M_SUBFOLD = "├  <b>🔐 sᴜʙ ꜰᴏʟᴅᴇʀs :</b> {Folder}\n"
    TOTAL_FILES = "├  <b>🗂️ ꜰɪʟᴇs :</b> {Files}\n"
    RCPATH = "├  <b>⛓️ ᴘᴀᴛʜ :</b><code> {RCpath}</code>\n"
    M_CC = "└  <b>👷 ʙʏ : </b>{Tag}\n\n"
    M_BOT_MSG = "➲ 𝗟𝗶𝗻𝗸(𝘀) 𝗵𝗮𝘃𝗲 𝗯𝗲𝗲𝗻 𝗦𝗲𝗻𝘁 𝘁𝗼 𝗕𝗼𝘁 𝗣𝗠 (𝗣𝗿𝗶𝘃𝗮𝘁𝗲)"
    # ----- BUTTONS -------
    CLOUD_LINK = "☁️ 𝗖𝗹𝗼𝘂𝗱 𝗟𝗶𝗻𝗸"
    SAVE_MSG = "📨 𝗦𝗮𝘃𝗲 𝗠𝗲𝘀𝘀𝗮𝗴𝗲"
    RCLONE_LINK = "♻️ 𝗥𝗖𝗹𝗼𝗻𝗲 𝗟𝗶𝗻𝗸"
    DDL_LINK = "📎 {Serv} 𝗟𝗶𝗻𝗸"
    SOURCE_URL = "🔐 𝗦𝗼𝘂𝗿𝗰𝗲 𝗟𝗶𝗻𝗸"
    INDEX_LINK_F = "🗂 𝗜𝗻𝗱𝗲𝘅 𝗟𝗶𝗻𝗸"
    INDEX_LINK_D = "⚡ 𝗜𝗻𝗱𝗲𝘅 𝗟𝗶𝗻𝗸"
    VIEW_LINK = "🌐 𝗩𝗶𝗲𝘄 𝗟𝗶𝗻𝗸"
    CHECK_PM = "📥 𝗩𝗶𝗲𝘄 𝗶𝗻 𝗕𝗼𝘁 𝗣𝗠"
    CHECK_LL = "🖇 𝗩𝗶𝗲𝘄 𝗶𝗻 𝗟𝗶𝗻𝗸𝘀 𝗟𝗼𝗴"
    MEDIAINFO_LINK = "📃 𝗠𝗲𝗱𝗶𝗮𝗜𝗻𝗳𝗼"
    SCREENSHOTS = "🖼 𝗦𝗰𝗿𝗲𝗲𝗻𝗦𝗵𝗼𝘁𝘀"
    # ---------------------

    # def get_readable_message(): ---> bot_utilis.py
    ####--------OVERALL MSG HEADER----------
    STATUS_NAME = "<b>🚧 {Name} 🚧</b>"

    #####---------PROGRESSIVE STATUS-------
    BAR = "\n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n\n┌  🚀 {Bar}"
    PROCESSED = "\n├  <b>🔄 ᴘʀᴏᴄᴇssᴇᴅ :</b> {Processed}"
    STATUS = '\n├  <b>⏬ ꜱᴛᴀᴛᴜꜱ :</b> <a href="{Url}">{Status}</a>'
    ETA = "\n├  <b>⏳ ᴇᴛᴀ :</b> {Eta}"
    SPEED = "\n├  <b>⚡️ sᴘᴇᴇᴅ :</b> {Speed}"
    ELAPSED = "\n├  <b>♻️ ᴇʟᴀᴘsᴇᴅ :</b> {Elapsed}"
    ENGINE = "\n├  <b>⛓️ ᴇɴɢɪɴᴇ :</b> {Engine}"
    STA_MODE = "\n├  <b>⚙️ ᴍᴏᴅᴇ:</b> {Mode}"
    SEEDERS = "\n├  <b>🌱 sᴇᴇᴅᴇʀs :</b> {Seeders} \n├  "
    LEECHERS = "<b>🐌 ʟᴇᴇᴄʜᴇʀs :</b> {Leechers}"

    ####--------SEEDING----------
    SEED_SIZE = "\n├  <b>📦 sɪᴢᴇ : </b>{Size}"
    SEED_SPEED = "\n├  <b>⚡️ sᴘᴇᴇᴅ : </b> {Speed} \n├  "
    UPLOADED = "<b>📤 ᴜᴘʟᴏᴀᴅᴇᴅ : </b> {Upload}"
    RATIO = "\n├  <b>☑️ ʀᴀᴛɪᴏ : </b> {Ratio} \n├  "
    TIME = "<b>⏰ ᴛɪᴍᴇ : </b> {Time}"
    SEED_ENGINE = "\n├  <b>⛓️ ᴇɴɢɪɴᴇ :</b> {Engine}"

    ####--------NON-PROGRESSIVE + NON SEEDING----------
    STATUS_SIZE = "\n├  <b>📦 sɪᴢᴇ : </b>{Size}"
    NON_ENGINE = "\n├  <b>⛓️ ᴇɴɢɪɴᴇ :</b> {Engine}"

    ####--------OVERALL MSG FOOTER----------
    USER = "\n├  <b>🆔 ᴜꜱᴇʀ ɴᴀᴍᴇ :</b> <code>{User}</code> \n├  "
    ID = "<b>👤 ᴜsᴇʀ ɪᴅ :</b> <code>{Id}</code>"
    BTSEL = "\n├ <b>🦠 sᴇʟᴇᴄᴛ:</b> {Btsel}"
    CANCEL = "\n└   ❎ ᴄᴀɴᴄᴇL {Cancel}\n\n"

    ####------FOOTER--------
    FOOTER = "┌  🚧 ʙᴏᴛ sᴛᴀᴛs<i></b>\n"
    TASKS = "├  <b>🤖 ᴛᴀsᴋs :</b> {Tasks}\n"
    BOT_TASKS = "├  <b>🤖 ᴛᴀsᴋs :</b> {Tasks}/{Ttask} |  <b>👷 ᴀᴠᴀɪʟᴀʙʟᴇ :</b> {Free}\n"
    Cpu = "├  <b>🖥 ᴄᴘᴜ :</b> {cpu}%  "
    Ram = "\n├  <b>🎮 ʀᴀᴍ :</b> {ram}%"
    FREE = "\n├  <b>💿 ғʀᴇᴇ :</b> {free} [{free_p}%]"
    uptime = "\n├  <b>🟢 ᴜᴘᴛɪᴍᴇ :</b> {uptime}"
    DL = "\n└  <b>🔻 ᴅʟ :</b> {DL}/s  "
    UL = "|  <b>🔺 ᴜʟ :</b> {UL}/s"

    ###--------BUTTONS-------
    PREVIOUS = " ↻  ʙᴀᴄᴋ "
    REFRESH = "| {Page} |"
    NEXT = "ɴᴇxᴛ ↻"
    # ---------------------

    # STOP_DUPLICATE_MSG: ---> clone.py, aria2_listener.py, task_manager.py
    STOP_DUPLICATE = (
        "𝗙𝗶𝗹𝗲/𝗙𝗼𝗹𝗱𝗲𝗿 𝗶𝘀 𝗮𝗹𝗿𝗲𝗮𝗱𝘆 𝗮𝘃𝗮𝗶𝗹𝗮𝗯𝗹𝗲 𝗶𝗻 𝗗𝗿𝗶𝘃𝗲.\𝗻𝗛𝗲𝗿𝗲 𝗮𝗿𝗲 {content} 𝗹𝗶𝘀𝘁 𝗿𝗲𝘀𝘂𝗹𝘁𝘀:"
    )
    # ---------------------

    # async def countNode(_, message): ----> gd_count.py
    COUNT_MSG = "<b>Counting:</b> <code>{LINK}</code>"
    COUNT_NAME = "{COUNT_NAME}</i></b>\n┃\n"
    COUNT_SIZE = "┠ <b>Size: </b>{COUNT_SIZE}\n"
    COUNT_TYPE = "┠ <b>Type: </b>{COUNT_TYPE}\n"
    COUNT_SUB = "┠ <b>SubFolders: </b>{COUNT_SUB}\n"
    COUNT_FILE = "┠ <b>Files: </b>{COUNT_FILE}\n"
    COUNT_CC = "┖ <b>By: </b>{COUNT_CC}\n"
    # ---------------------

    # LIST ---> gd_list.py
    LIST_SEARCHING = "<b>Searching for <i>{NAME}</i></b>"
    LIST_FOUND = "<b>Found {NO} result for <i>{NAME}</i></b>"
    LIST_NOT_FOUND = "No result found for <i>{NAME}</i>"
    # ---------------------

    # async def mirror_status(_, message): ----> status.py
    NO_ACTIVE_DL = """<i>No Active Downloads!</i>
    
⌬ Bot Stats</i></b>
┠ <b>CPU:</b> {cpu}% | <b>F:</b> {free} [{free_p}%]
┖ <b>RAM:</b> {ram} | <b>UPTIME:</b> {uptime}
    """
    # ---------------------

    # USER Setting --> user_setting.py
    # USER Setting --> user_setting.py
    USER_SETTING = """㊂ <b><u>User Settings :</u></b>
        
┎<b> Name :</b> {NAME} ( <code>{ID}</code> )
┠<b> Username :</b> {USERNAME}
┠<b> Telegram DC :</b> {DC}
┖<b> Language :</b> {LANG}

➲<b> Leech Thumb :</b> {THUMB}


➲ <u><b>Available Args:</b></u>
• <b>-s</b> or <b>-set</b>: Set Directly via Arg"""

    UNIVERSAL = """㊂ <b><u>Universal Settings : {NAME}</u></b>

┎<b> YT-DLP Options :</b> <b><code>{YT}</code></b>
┠<b> Daily Tasks :</b> <code>{DT}</code> per day
┠<b> Last Bot Used :</b> <code>{LAST_USED}</code>
┠<b> User Session :</b> <code>{USESS}</code>
┠<b> MediaInfo Mode :</b> <code>{MEDIAINFO}</code>
┠<b> Save Mode :</b> <code>{SAVE_MODE}</code>
┖<b> User Bot PM :</b> <code>{BOT_PM}</code>"""

    MIRROR = """㊂ <b><u>Mirror/Clone Settings : {NAME}</u></b>

┎<b> RClone Config :</b> <i>{RCLONE}</i>
┠<b> Mirror Prefix :</b> <code>{MPREFIX}</code>
┠<b> Mirror Suffix :</b> <code>{MSUFFIX}</code>
┠<b> Mirror Remname :</b> <code>{MREMNAME}</code>
┠<b> DDL Server(s) :</b> <i>{DDL_SERVER}</i>
┠<b> User TD Mode :</b> <i>{TMODE}</i>
┠<b> Total User TD(s) :</b> <i>{USERTD}</i>
┖<b> Daily Mirror :</b> <code>{DM}</code> per day"""

    LEECH = """㊂ <b><u>Leech Settings for {NAME}</u></b>

┎<b> Daily Leech : </b><code>{DL}</code> per day
┠<b> Leech Type :</b> <i>{LTYPE}</i>
┠<b> Custom Thumbnail :</b> <i>{THUMB}</i>
┠<b> Leech Split Size :</b> <code>{SPLIT_SIZE}</code>
┠<b> Equal Splits :</b> <i>{EQUAL_SPLIT}</i>
┠<b> Media Group :</b> <i>{MEDIA_GROUP}</i>
┠<b> Leech Caption :</b> <code>{LCAPTION}</code>
┠<b> Leech Metadata :</b> <code>{METADATA_KEY}</code>
┠<b> Leech Prefix :</b> <code>{LPREFIX}</code>
┠<b> Leech Suffix :</b> <code>{LSUFFIX}</code>
┠<b> Leech Dumps :</b> <code>{LDUMP}</code>
┖<b> Leech Remname :</b> <code>{LREMNAME}</code>"""
