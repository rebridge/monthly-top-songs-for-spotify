#spotify automation

import time

#print('Enter username: ')
#userlogin = str(input())
#print('Enter password: ')
#passwordlogin = str(input())
#time.sleep(1)

import selenium
import pyautogui
from selenium import webdriver


PATH = "/users/rebridge/Spotify Automation/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://accounts.spotify.com/en/authorize?client_id=09793e3afafa4797bf853f2ad5db72f3&redirect_uri=http://107.170.81.187:8080/SpotifyLoginCallback/&response_type=code&scope=user-read-recently-played+user-library-read+user-top-read&show_dialog=false&state=34fFs29kd09")

#username = driver.find_element_by_id('login-username')


username = driver.find_element_by_id('login-username')
username.send_keys("lincbradthom")
time.sleep(1)

password = driver.find_element_by_id('login-password')
password.send_keys("fortnitepro69")
time.sleep(1)

login = driver.find_element_by_id('login-button')
login.click()

#if statement for first time (shoould only fire if certain url is active)
#this section is onlt needed for a new log in

if driver.current_url == 'https://accounts.spotify.com/en/authorize?client_id=09793e3afafa4797bf853f2ad5db72f3&redirect_uri=http:%2F%2F107.170.81.187:8080%2FSpotifyLoginCallback%2F&response_type=code&scope=user-read-recently-played%20user-library-read%20user-top-read&show_dialog=false&state=34fFs29kd09' :
    time.sleep(3)
    agree = driver.find_element_by_id('auth-accept')
    agree.click()
else :
    time.sleep(7)

#refreshes webpage
pyautogui.keyDown('command')
pyautogui.press('r')
pyautogui.keyUp('command')
time.sleep(5)

# searches for "Top tracks -- Short Term"
#pyautogui.keyDown('command')
#pyautogui.press('f')
#pyautogui.keyUp('command')
#pyautogui.write('Top tracks -- Short Term')
#time.sleep(2)

tracks_element = driver.find_element_by_xpath('/html/body/ol[4]')
tracks = tracks_element.text
print(tracks)
