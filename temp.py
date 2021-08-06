from dotenv import load_dotenv
load_dotenv()


import os
import telebot
import geopy.distance
from telegram import Location, KeyboardButton
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton



API_key = os.environ.get('aedAPI_KEY')
bot = telebot.TeleBot(API_key)


aedDict = {}


class AED:
    def __init__(self, location):
        self.latitude = location.latitude
        self.longitude = location.longitude
       

locations = {
    "nsdc": {
        1: (1.4055524, 103.8182829),
        2: (1.4067986, 103.8192924),
        3: (1.4091958,103.8186530)

    }

}












@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, """ 
    Use the /aed command followed by the camp name to find where AED's are located!

    Kranji Camp 2 = /aed kc2
    Kranji Camp 3 = /aed kc3
    Nee Soon Driclad Center = /aed nsdc
    
    """)
    #bot.send_chat_action(message.chat.id, 'find_location')


@bot.message_handler(commands=['start'])
def start(message):
    loc = telebot.types.KeyboardButton(text='Nearest AED', request_location=True)
    not_loc = telebot.types.KeyboardButton(text='Static Map')
    start = telebot.types.ReplyKeyboardMarkup(resize_keyboard = True, one_time_keyboard = True)
    start.row(loc)
    start.row(not_loc)
    bot.send_message(message.chat.id, text='Hello, would you like to see your nearest AED or a static map?', reply_markup=start)

    #bot.send_message(message.chat.id, "Welcome to AED Location Bot, How Can I Help?")
    



    

@bot.message_handler(content_types=['location'])
def currentLocation(message):
    try:
        chat_id = message.chat.id
        

        if message.location:
            aed = AED(message.location)
            aedDict[chat_id] = aed
            print(message.location)
            closestAED = (0,0)
            minDist = 100000000000
            for coords in locations["nsdc"].values():
                #dist = geopy.distance.distance((aed.latitude, aed.longitude), coords).m
                dist = geopy.distance.distance((1.408879, 103.818540), coords).m
                print(dist)
                if dist < minDist:
                    minDist = dist
                    closestAED = coords

            bot.send_location(message.chat.id, closestAED[0], closestAED[1])
            sendString = "The closest AED is at the above location, approximately " + str(round(minDist)) + "m away"
            bot.send_message(message.chat.id,sendString )
    except Exception as e:
        bot.reply_to(message, 'oooops')


def checker (message):
    if message.text == "Static Map" and message.content_type == 'text':
        return True
    else:
        return False



@bot.message_handler(func=checker)
def staticMap(message):
    try:
        msg = bot.reply_to(message, """\
        Which camp would you like a map for?

        Options are:
        1. nsdc
        2. kc2
        3. kc3
        4. hendon
        5. mowbray
        6. clementi
        7. maju
        8. mandai hill
        9. gombak
        10. gedong
        """)
        bot.register_next_step_handler(msg, returnImage)
    except Exception as e:
        bot.reply_to(message, 'oooops')

def returnImage(message):
    try:
       
        url = "https://lh3.googleusercontent.com/-78QT2XudDyQlv84s3sJRs4e2A2CWoXLTX9n6sUM9Wc8SU6JO07PjMuvjhF41Iz47vEhI0OjQxtv6kM8X85pRl92xCPz3w9Faws-hEqSCtnT7DoCpJD1PosHvohVXItHoI4a53V0mgaMaI0t9Pj69hYO1NP5edwNLWbNw19ij4B8B0KR329nXgJEqt0hhdNKoPEemcjBsrpNNINMByGxDFGFmcZk8uLw0bspdiIuHrgDgGTfCFKGjA_DS7NJm_tc9j86cyFk-BsJncUpcPpjVJXmlikJGltQRxRJpljrlfxcK8svzIRlVYRYSXavzmkesyF80bjmLsYYD4Ht5O1dVbnc-JNCZPIL3c1f0EC9_ccZNf9K9DVjYvVVabbeUsobGMuf2y9bW0LePusAxXssPeXwcMuFO9UU7q-lGoRSaWrKxwfHWCvDG5b6YQ4RllE72iwT-eDrmlTG-RzV3vT9JSG3g_XOgY4XMJDCzUMMnH-Jh2duaqdBuQxyj7_iav9SEhPPjCtVSvVnJtDefsteeplOlziQleooo89pSML1mWz5tBUKcEtX8WRfA4cJeT6joam4a4BTi2BpaDDqNzisyc7RfbHu7y5o9TICNk-GnYxw873-FqT1DBN_tErjlOGfG4WFRw_hM_mrQnfJZndg98-H40s5XpigQAwIiECdLHudEdkeGcEDDmpOwRSIN16acUzNvYP7anwn8tfY7-eCh534WQ=w828-h775-no?authuser=1"
        chat_id = message.chat.id
        bot.send_photo(chat_id=chat_id, photo=url)
    except Exception as e:
        bot.reply_to(message, 'oooops')

bot.polling()