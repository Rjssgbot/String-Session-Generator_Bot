from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Hey {}

Welcome to {}

I can generate pyrogram and telethon string session . 
Use the below button and go ahead !

By @Rjssgbot
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("π· Start Generating Session π·", callback_data="generate")],
        [InlineKeyboardButton(text="π  Return Home π ", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("π· Start Generating Session π·", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("π· Start Generating Session π·", callback_data="generate")],
        [
            InlineKeyboardButton("How to Use β", callback_data="help"),
            InlineKeyboardButton("πͺ About πͺ", callback_data="about")
        ],
    ]

    # Help Message
    HELP = """
β¨ **Available Commands** β¨

/about - About The Bot
/help - To display current Message
/start - Start the Bot
/generate - Generate String Session
/cancel - Cancel the process
/restart - Cancel the process
"""

    # About Message
    ABOUT = """
**About This Bot** 

A telegram bot to generate pyrogram and telethon string session by @Rjssgbot

Framework : [Pyrogram](docs.pyrogram.org)

Language : [Python](www.python.org)

Developer : πΎπ‘οΈποΈποΈπΎ
    """
