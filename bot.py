import shlex
import subprocess
from typing_extensions import Self
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import webbrowser
import pyautogui
import time
import random
import subprocess
import shlex
from datetime import date


class botinstance:

    def login(self):
        webbrowser.open(
            "https://www.time4education.com/login/index.php", new=0, autoraise=True)

        time.sleep(30)
        pyautogui.click(80, 360)
        time.sleep(5)
        pyautogui.write('BBCB1A147', interval=0.25)
        time.sleep(5)
        pyautogui.hotkey('enter')
        pyautogui.write('RAP33P', interval=0.25)
        pyautogui.hotkey('enter')
        time.sleep(15)
    
    def logout(self):
        webbrowser.open(
            "https://www.time4education.com/login/index.php", new=0, autoraise=True)
        time.sleep(20)
        pyautogui.click(80, 320)
        time.sleep(20)
        pyautogui.hotkey('ctrl', 'w')


    def main(botinstance):
    
        file = open('pagesource.txt', 'r')
        file_content = file.read()
        videoid_list = file_content.split()

        while(True):
            botinstance.login()

            for count,videoid in enumerate(videoid_list):
                if count<3:
                    link = "https://www.time4education.com/my/videowtest.php?videoid="+videoid
                    webbrowser.open(link, new=0, autoraise=True)
                    time.sleep(30)
                    pyautogui.press('f11')
                    time.sleep(30)
                    pyautogui.click(1285, 430)
                    time.sleep(3)
                    pyautogui.click(1285, 430)
                    time.sleep(10)
                    pyautogui.click(1285, 750)
                    time.sleep(1)
                    pyautogui.click(1285, 600)
                    time.sleep(1)
                    pyautogui.click(1285, 705)
                    time.sleep(1)
                    pyautogui.click(1285, 430)
                    time.sleep(1)
                    pyautogui.hotkey('ctrl','winleft','r')
                    time.sleep(4000)
                    pyautogui.hotkey('ctrl', 'winleft', 'f')
                    time.sleep(10)
                    pyautogui.press('f11')
                    time.sleep(3)
                    pyautogui.hotkey('ctrl','w')
                    subprocess.Popen(shlex.join(['cd']), shell=True)
                    result = subprocess.Popen(shlex.join(
                        ["mv", "ccv_00000.mp4", f"{videoid}.mp4"]), shell=True, stderr=subprocess.PIPE, text=True)
                    time.sleep(2)
                    result = subprocess.Popen(
                        ["gio", "move", f"{videoid}.mp4", "google-drive://kanika.s2019bos@srisriuniversity.edu.in/"], stderr=subprocess.PIPE, text=True)
                    time.sleep(10)
                else:
                    break
            videoid_list.pop(0)
            videoid_list.pop(0)
            videoid_list.pop(0)
            botinstance.logout()



botinstance().main()

