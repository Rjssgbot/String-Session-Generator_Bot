import os
class Config:
    API_ID = int(os.environ.get('API_ID', "19031598"))
    API_HASH = str(os.environ.get('API_HASH', "14e2d2af6e6dc769e60991cab81027d5"))
    BOT_TOKEN = str(os.environ.get('BOT_TOKEN', "5665710621:AAFP-O8AW3ekB_basaPR3A7w3YpQDMQbCDY"))
    MONGO_URI = str(os.environ.get('MONGO_URI', "mongodb+srv://Oyehoye143:Oyehoye143@cluster0.eth7a3p.mongodb.net/?retryWrites=true&w=majority"))
    UPDATES_CHANNEL = str(os.environ.get('UPDATES_CHANNEL', "RomeoBot_OP")) #Start Without @
