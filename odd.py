from dotenv import load_dotenv
load_dotenv()

import os
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


API_key = os.environ.get('oddAPI_KEY')
bot = telebot.TeleBot(API_key)

oddDict = {}


class Odd:
    def __init__(self, unitNum):
        self.unitNum = unitNum
        self.wpnType = "SAR21" #use button options
        self.buttNum = ""
        self.oddCode = ""
        self.rmk = ""


#turn this dictionary into numbers or make a secondary dictionary to transform into numbers (SAR21:1, SAW:2, etc)
oddTypes = {
    "SAR21": {
        "BARREL":{
            1:"1. Bent or curved",
            2:"2. Cracked",
            3:"3. Others"
        },
        "SCOPE":
        {
            1:"1. Cracked",
            2:"2. Blurry",
            3:"3. Scratched",
            4:"4. Carrying Handle Torn",
            5:"5. Others"
        },
        "CHARGING HANDLE":
        {
            1:"1. Others"
        },
        "LAD":
        {
            1:"1. Battery Cap Missing",
            2:"2. LAD Buffle Cracked or Missing",
            3:"3. Switch not clicking properly",
            4:"4. Laser weak/not functioning with battery inside",
            5:"5. Others"
        },
        "MUZZLE AND WASHER":{
            1:"1. Muzzle cracked or worn out",
            2:"2. Washer deficient",
            3:"3. Others"
        },
        "OTHER": {
            1:"Input ODD Location"
        }

    }
}

SAR21Map = {1: "SCOPE", 2: "BARREL", 3: "CHARGING HANDLE", 4:"LAD", 5:"MUZZLE AND WASHER", 6:"OTHER"}

#=============================================================
# Handle '/start' and '/help'
@bot.message_handler(commands=['ODD' and 'odd'])
def send_welcome(message):
    msg = bot.reply_to(message, """\
Hi there, I am the ODD Feedback Bot. What unit are you from?
""")
    bot.register_next_step_handler(msg, unitStep)

def unitStep(message):
    try:
        chat_id = message.chat.id
        unit = message.text
        odd = Odd(unit)
        oddDict[chat_id] = odd

        msg = bot.reply_to(message, 'What is the butt number?')
        bot.register_next_step_handler(msg, buttStep)
    except Exception as e:
        bot.reply_to(message, 'oooops')

#enter weapon type here
#enter date here

def buttStep(message):
    try:
        chat_id = message.chat.id
        buttNum = message.text
        odd = oddDict[chat_id]
        odd.buttNum = buttNum
        url = "https://lh3.googleusercontent.com/V0ItwRUHvmcQ22XlCzeIeviA6kuMfUspJHgHbwkA8nD09SjesgQYt3RdFB1nvM63kYSs8TgTwk-1KTiJBt8gbRJZlZQVWzKEWDh3a1w51A2m2j-Qt31PrJbR3viWlMFMyar4TOTZS8eXGiX0itB4B-dTDCoJZnZONHwzhHGo_YetJlSpfE1ohVWpeQrj34TmOSGJSz48O-tkzMLKbuYsXIjKuolALQsM961r2N08HcBz0GQ03gxJkrV5Q5IOOwhvoAeK_z-lwf1gQb1GBpQ9gf0vQqG9KPYBuzljdBVlwqYzytihp-1gK7nlEYmeERYYK6ubpFX3NA4jkRujjaqY0df9AC7xsx5q0sbp-hboAlA1jM3bQLxvRicU5usSimVY6RCBFgrJ3LbLKNLNlxgYoLIe88eDpLVRVemMGqNURQBSzi-uKi8pe_BZuxOw3pMSQoOR0JELkjbIBRS9e3mP53Sb4eCflk1hQrwroiEBJDdN5tmfctqbY3ha9N0sJ9ng3wXSgBIWZl_tzYGVJlB4fng-vfyZhSxdsVWd1Z6Yc3pgZZJF8mz_6YG5z4jQ5SumFUEVtLeTPFXqNsR3-BhdQJK4QiZcnd8qWrIG8WoZBRIM_vp_NNvv7kInjb_SYZCz_7zvwjBYAZe_61K7XamQxrxWxIa_hOvzLmZGJk7eOPOIFT7yWJTtpvCudcGGQq8aqNW_WXluoVR6UhywwVu7N45COg=w763-h304-no?authuser=1"
        
        bot.send_photo(chat_id=chat_id, photo=url)
        msg = bot.reply_to(message, """\
Where is the ODD (input only the number)? \n
1. Barrel
2. Scope
3. Charging Handle
4. LAD
5. Muzzle
6. Other
""")
        bot.register_next_step_handler(msg, locationStep)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def locationStep(message):
    try:
        chat_id = message.chat.id
        rmk = message.text
        odd = oddDict[chat_id]
        odd.rmk = rmk
        info = oddTypes["SAR21"][SAR21Map[int(rmk)]]
        # print(info)
        sendString = ""
        for elements in info.values():
            sendString += elements + "\n" 
        bot.send_message(chat_id, sendString)

        #if "other" then next step is inputting the correct location (idk is an option)
        #if not other, then say what the issue is, or choose other and type it in

        # msg = bot.reply_to(message, 'What is the quantity booked?')
        # bot.register_next_step_handler(msg, bookedStep)
    except Exception as e:
        bot.reply_to(message, 'oooops')

bot.polling()