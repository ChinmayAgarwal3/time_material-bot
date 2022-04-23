import webbrowser
import pyautogui
import time
from datecheck import Init_df
import random
from datetime import date
from check_today import Check


def end():
    time.sleep(5)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    time.sleep(1)
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f4')
    pyautogui.hotkey('alt', 'f4')
    time.sleep(2)



if Check().Check_Today() == False:
    end()
    exit()

# Prompt to open Whatsapp and net on the phone before starting
reply=pyautogui.confirm(text='Please open Whatsapp and Wifi on the Phone', title='Starting Whatsapp Web', buttons=['OK', 'Cancel'])

if reply=='Cancel':
    end()
    exit()

# * OPEN WEB WHATSAPP
webbrowser.open("https://web.whatsapp.com/", new=0, autoraise=True)
time.sleep(30)
pyautogui.click(200, 220)

# * Birthday Bot Whatsapp Daily Test 
pyautogui.keyDown('alt')
pyautogui.hotkey('ctrl', '/')
pyautogui.keyUp('alt')
time.sleep(3)

pyautogui.write('Birthday', interval=0.25)
pyautogui.press('tab')
pyautogui.press('enter')
time.sleep(2)

today = date.today().strftime("%d/%m")
message = "{} Bot is up and running".format(today)
time.sleep(5)
pyautogui.write(message)
pyautogui.press('enter')
time.sleep(5)



tuple = Init_df().Birthday_Today()
if not all(tuple):
    print("No one's Birthday")
    exit() 



# * Loop for Birthday people
contact_name = tuple[0]
nickname = tuple[1]
messages= tuple[2]
for (contact,name,message) in zip(contact_name,nickname,messages):

    # * SEARCH 
    pyautogui.keyDown('alt')
    pyautogui.hotkey('ctrl', '/')
    pyautogui.keyUp('alt')
    time.sleep(3)

    pyautogui.write(contact, interval=0.25)
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)
    message_list = [
        """Happy birthday {}! I hope you have a wonderful day today and that everything goes the way you want it to.""", """{}, Another year older and wiser, you truly are growing into an amazing person. I hope you have a fabulous year up ahead.""", """This day is yours, make it unique. Happpy birthday {}!"""]
    message2=random.choice(message_list)
    message = message.format(name)
    message2=message2.format(name)
    time.sleep(5)
    pyautogui.write(message+"\n"+message2)
    pyautogui.press('enter')
    time.sleep(5)

