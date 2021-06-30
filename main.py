from dotenv import load_dotenv
load_dotenv()

import os
import telebot


API_key = os.environ.get('API_KEY')
bot = telebot.TeleBot(API_key)

@bot.message_handler(commands="aed")
def aed(message):
    words = message.text
    wordsWithoutCommand = words.replace("/aed ", "").split()
    camp = wordsWithoutCommand[0].lower()
    url = ""
    print(camp)
    if camp == "nsdc":
        url ="https://lh3.googleusercontent.com/uYRsIwxwJ4aaQV5DKWIh6Pr3duUiL5xAmJnXl8_K-Tt0NFINmgfAUdi89ZjYPAYyk77iPpOinspDJ9JPajPUoKoYBY248HTTO2eMJo2UxuF8E4exNq4ABv0pNMRDXBt1G7ShWNkiKc7hGHBH6FTaTTBCPeBGe5InfymR-4_sFUqSXIGRU8BiIn1XHvVUUW61gohjP3dlCJwzTaAyxjExLtQevIKiMBDam0wnq8TubTkmSOtDfLC_xvMuNVpw3T7GGMZKuxZ07cOHpRenlKTd1l4NpZOR-2-1IikI_Fa65QT9OFGDxp9PknCWB6fYOTiJk40PtKi0Thl4TeAamT3cPVGDmv7YHDh6dHupgxFJV8d-kZzhR20LnhRve917DYJxhAUU0fp3X3K3WbbdBXdm8eS3sooV55Ppu_vORVhnB0DbvtGZt9hQ3ufVNXPnFA9hCAFLY7jcOVWUnokQd5ZuZLvDWsBylSt1l_MiwCgjm4bW9fgjPr6dNewU3SspWnq2Ga_cMuDSivhq-Lkaj6_BkC-BGr8fw0B5HzIonIIWrod1nUYDWUEgKHcsGFVujX2I9jP7toDa4izRXumRZYoTl7sYyeCO6r6doVfUKBvS6hFr01b2tG9SwyHjHdofbDkx8kmZeCYUWEpTjTFim_GlXUNe4iwVMiZBeZ0jItjBUYcSLHh8o7-DqA_E87CZDCuiby4Vi1a-7HzG-OhX8Sm9Ub32HQ=w828-h501-no?authuser=1"
    elif camp == "kc3":
        url = "https://lh3.googleusercontent.com/-78QT2XudDyQlv84s3sJRs4e2A2CWoXLTX9n6sUM9Wc8SU6JO07PjMuvjhF41Iz47vEhI0OjQxtv6kM8X85pRl92xCPz3w9Faws-hEqSCtnT7DoCpJD1PosHvohVXItHoI4a53V0mgaMaI0t9Pj69hYO1NP5edwNLWbNw19ij4B8B0KR329nXgJEqt0hhdNKoPEemcjBsrpNNINMByGxDFGFmcZk8uLw0bspdiIuHrgDgGTfCFKGjA_DS7NJm_tc9j86cyFk-BsJncUpcPpjVJXmlikJGltQRxRJpljrlfxcK8svzIRlVYRYSXavzmkesyF80bjmLsYYD4Ht5O1dVbnc-JNCZPIL3c1f0EC9_ccZNf9K9DVjYvVVabbeUsobGMuf2y9bW0LePusAxXssPeXwcMuFO9UU7q-lGoRSaWrKxwfHWCvDG5b6YQ4RllE72iwT-eDrmlTG-RzV3vT9JSG3g_XOgY4XMJDCzUMMnH-Jh2duaqdBuQxyj7_iav9SEhPPjCtVSvVnJtDefsteeplOlziQleooo89pSML1mWz5tBUKcEtX8WRfA4cJeT6joam4a4BTi2BpaDDqNzisyc7RfbHu7y5o9TICNk-GnYxw873-FqT1DBN_tErjlOGfG4WFRw_hM_mrQnfJZndg98-H40s5XpigQAwIiECdLHudEdkeGcEDDmpOwRSIN16acUzNvYP7anwn8tfY7-eCh534WQ=w828-h775-no?authuser=1"
    chat_id = message.chat.id
    bot.send_photo(chat_id=chat_id, photo=url)



#===========================================================




def templateChecker(message):
    request = message.text.split()
    if len(request) < 8:
        return False
    else:
        return True
def isNumericOrSpace (message):
    retVal = True
    for char in message:
        if not(char.isdigit() or char == " "):
            retVal = False
    return retVal

@bot.message_handler(func=templateChecker) #takes a string and outputs the templated inspection summary
def template(message):
    words = message.text
    words = words.replace("/template ", "")
    counter = 0
    camp = ""
    print (words)
    while not isNumericOrSpace(words[counter:]):
        if counter == len(words):
            break
        camp = camp + words[counter]
        counter += 1
        print(counter)
    splitText = words[counter:].split()
    print(camp)
    inspectionSummary = "*INSPECTION SUMMARY*" + "\n"
    camp = camp.upper() + "\n\n"
    quantityBooked = "QUANTITY BOOKED: " + "[" + str(splitText[0]) + "]" + "\n"
    quantityChecked = "QUANTITY CHECKED: " + "[" + str(splitText[1]) + "]" + "\n\n"
    oddQuantity = "ODD QUANTITY: " + "[" + str(splitText[2]) + "]" + "\n"
    oddRectified = "ODD QUANTITY: " + "[" + str(splitText[3]) + "]" + "\n\n"
    totalUS = "*NO OF US WEAPONS:" + "[" + str(splitText[4]) + "]*" + "\n"
    outstandingUS = "*NO OF OUTSTANDING US WEAPONS:" + "[" + str(splitText[5]) + "]*" + "\n\n"
    remarks = "REMARKS: \nTools and gauges accounted for."

    returnStatement = inspectionSummary + camp + quantityBooked + quantityChecked + oddQuantity + oddRectified + totalUS + outstandingUS + remarks
    bot.send_message(message.chat.id, returnStatement)


bot.polling()