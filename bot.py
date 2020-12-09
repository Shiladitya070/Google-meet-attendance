from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from time import sleep
import pause
import pynput
from pynput.keyboard import Key, Controller
import datetime
# YEAR#MONTH#DAY#HOUR#MINUTE###### DO NOT PUT ZERO BEFORE A NUMBER
# pause.until(datetime(2020, 3, 27, 11, 29))
# MAIL & PASSWORD (THE MAIL U WILL USE TO ENTER TO THE MEET)
# usernameStr = str(input("Enter your school email: "))
# passwordStr = str(input("password: "))
usernameStr = str(input("Enter your email address:"))
passwordStr = str(input("Enter your password:"))


url_meet = str(input("Enter the meeting link: "))
options = webdriver.ChromeOptions()
options.add_argument("--disable-infobars")
options.add_argument("--window-size=800,600")
options.add_experimental_option("prefs", {
    "profile.default_content_setting_values.media_stream_mic": 1,     # 1:allow, 2:block
    "profile.default_content_setting_values.media_stream_camera": 1,
    "profile.default_content_setting_values.notifications": 2
})
browser = webdriver.Chrome(chrome_options=options)


def login():
    browser.get(('https://accounts.google.com/ServiceLogin?'
                 'service=mail&continue=https://mail.google'
                 '.com/mail/#identifier'))
    username = browser.find_element_by_id('identifierId')
    username.send_keys(usernameStr)
    nextButton = browser.find_element_by_id('identifierNext')
    nextButton.click()
    sleep(5)
    keyboard = Controller()
    # keyboard.type(passwordStr)
    password = browser.find_element_by_xpath("//input[@class='whsOnd zHQkBf']")
    password.send_keys(passwordStr)
    # keyboard.type(passwordStr)
    signInButton = browser.find_element_by_id('passwordNext')
    signInButton.click()
    sleep(3)


login()

browser.get(url_meet)
sleep(10)
cam_mic_selectors = browser.find_elements_by_css_selector(
    'div.U26fgb.JRY2Pb.mUbCce.kpROve.uJNmj.HNeRed')  # camera and mic
for e in cam_mic_selectors:
    e.click()
browser.find_element_by_css_selector(
    'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()  # join now
sleep(5)
browser.find_element_by_css_selector(
    'div.uArJ5e.UQuaGc.kCyAyd.QU4Gid.foXzLb.IeuGXd').click()  # participant list
sleep(1)
names = browser.find_elements_by_css_selector(
    'div.GvcuGe')  # participants
file1 = open(f"attendence {datetime.date.today()}.txt", "w")
print(names)
for e in names:
    file1.write(f"{e.text} \n")
    print(e.text)

file1.close()
print('Attendance taken successfully!')
browser.quit()
