from dotenv import load_dotenv
load_dotenv()


import os
import telebot
from telegram import Location
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, KeyboardButton



API_key = os.environ.get('aedAPI_KEY')
bot = telebot.TeleBot(API_key)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Welcome to AED Location Bot, How Can I Help?")
    

@bot.message_handler(commands=['help'])
def start(message):
    bot.send_message(message.chat.id, """ 
    Use the /aed command followed by the camp name to find where AED's are located!

    Kranji Camp 2 = /aed kc2
    Kranji Camp 3 = /aed kc3
    Nee Soon Driclad Center = /aed nsdc
    
    """)

@bot.message_handler(commands=['aed'])
def aed(message):
    words = message.text
    wordsWithoutCommand = words.replace("/aed ", "").split()
    camp = wordsWithoutCommand[0].lower()
    url = ""
    print(camp)
    if camp == "nsdc":
        url ="https://lh3.googleusercontent.com/vLivZ4rpe4zjyGQTaMxCCw_uHopmaWdVePKjc_O7ifGsy8VK4IXbqIGkkAKBNCo0AsSTJ4mAjdouQdzodLjx1G2_6ebqnv-IzYsqgcrmy1teTwLTLo09MqFjDBXdrrz3JdCeOx6Kiy7BeNYvUvKatO7Jc0H0GL8PMoYrNeAdRfK-W1gPPqKoD-4c6d2KCGew8L_8a0wQIp7RfY7DbJDEKs2jC1TOZ4eIj89wrwrxFjYix3lvG2IZlvMLIjaAvP4LvHK5CH4iVJD881RyWDeSn56b_aCKca7wGck8a6eumUNsnrrWGvCK3SIxaukA8FbE027DrnezBLi8xZP2EQFJy7ULoaFMPadEjrPEKi2xRZ8ctfczWGvr-rCORsVbcMEZQWKq3Zd6c0ZI_PVI54XvxNL6jrVYtRDK-s4ebI3ckp18LXBPB0DNM-qOKyWbtnqdyZ0ddJXYiqqB_OQ7yOjzGzx4EcC_TAcFykZz1fOK9ksl2fQvqDXFgYFHdC9rM5ei_Jd3a6g_J193DTKlvrbRA2yTKFIF0jQfGIsrTpyB71vTjs-0kZ2oVufO_4qGGiHL2CPgAHQ1tzwk7zdL3IfI3OJP3h9osgN-74I5fOefhE01kWKtJiRPXiHdxOniibKWQH8UXbRxWOuefPy9VFq9oDuzZc50EHC9eDSUcPo7CLtoUYVZdf73NxHvIf563m2UQDDp6KM1IW60qmVa8Il8p-xD0g=w599-h796-no?authuser=1"
    elif camp == "kc3":
        url = "https://lh3.googleusercontent.com/-78QT2XudDyQlv84s3sJRs4e2A2CWoXLTX9n6sUM9Wc8SU6JO07PjMuvjhF41Iz47vEhI0OjQxtv6kM8X85pRl92xCPz3w9Faws-hEqSCtnT7DoCpJD1PosHvohVXItHoI4a53V0mgaMaI0t9Pj69hYO1NP5edwNLWbNw19ij4B8B0KR329nXgJEqt0hhdNKoPEemcjBsrpNNINMByGxDFGFmcZk8uLw0bspdiIuHrgDgGTfCFKGjA_DS7NJm_tc9j86cyFk-BsJncUpcPpjVJXmlikJGltQRxRJpljrlfxcK8svzIRlVYRYSXavzmkesyF80bjmLsYYD4Ht5O1dVbnc-JNCZPIL3c1f0EC9_ccZNf9K9DVjYvVVabbeUsobGMuf2y9bW0LePusAxXssPeXwcMuFO9UU7q-lGoRSaWrKxwfHWCvDG5b6YQ4RllE72iwT-eDrmlTG-RzV3vT9JSG3g_XOgY4XMJDCzUMMnH-Jh2duaqdBuQxyj7_iav9SEhPPjCtVSvVnJtDefsteeplOlziQleooo89pSML1mWz5tBUKcEtX8WRfA4cJeT6joam4a4BTi2BpaDDqNzisyc7RfbHu7y5o9TICNk-GnYxw873-FqT1DBN_tErjlOGfG4WFRw_hM_mrQnfJZndg98-H40s5XpigQAwIiECdLHudEdkeGcEDDmpOwRSIN16acUzNvYP7anwn8tfY7-eCh534WQ=w828-h775-no?authuser=1"
    else:
        url = "https://lh3.googleusercontent.com/-78QT2XudDyQlv84s3sJRs4e2A2CWoXLTX9n6sUM9Wc8SU6JO07PjMuvjhF41Iz47vEhI0OjQxtv6kM8X85pRl92xCPz3w9Faws-hEqSCtnT7DoCpJD1PosHvohVXItHoI4a53V0mgaMaI0t9Pj69hYO1NP5edwNLWbNw19ij4B8B0KR329nXgJEqt0hhdNKoPEemcjBsrpNNINMByGxDFGFmcZk8uLw0bspdiIuHrgDgGTfCFKGjA_DS7NJm_tc9j86cyFk-BsJncUpcPpjVJXmlikJGltQRxRJpljrlfxcK8svzIRlVYRYSXavzmkesyF80bjmLsYYD4Ht5O1dVbnc-JNCZPIL3c1f0EC9_ccZNf9K9DVjYvVVabbeUsobGMuf2y9bW0LePusAxXssPeXwcMuFO9UU7q-lGoRSaWrKxwfHWCvDG5b6YQ4RllE72iwT-eDrmlTG-RzV3vT9JSG3g_XOgY4XMJDCzUMMnH-Jh2duaqdBuQxyj7_iav9SEhPPjCtVSvVnJtDefsteeplOlziQleooo89pSML1mWz5tBUKcEtX8WRfA4cJeT6joam4a4BTi2BpaDDqNzisyc7RfbHu7y5o9TICNk-GnYxw873-FqT1DBN_tErjlOGfG4WFRw_hM_mrQnfJZndg98-H40s5XpigQAwIiECdLHudEdkeGcEDDmpOwRSIN16acUzNvYP7anwn8tfY7-eCh534WQ=w828-h775-no?authuser=1"
    chat_id = message.chat.id
    bot.send_photo(chat_id=chat_id, photo=url)



bot.polling()