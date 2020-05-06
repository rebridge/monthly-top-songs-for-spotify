#spotify automation

import time
print('Enter username: ')
userlogin = str(input())
print('Enter password: ')
passwordlogin = str(input())
time.sleep(1)
import numpy as np
#userlogin = np.loadtxt("usertext.txt", delimiter=",")
#print(userlogin[0])
#passwordlogin = np.loadtxt("password.txt", delimiter=",")
#print(passwordlogin[0])
import selenium
import pyautogui
from selenium import webdriver


PATH = "/users/rebridge/Spotify Automation/chromedriver"

driver = webdriver.Chrome(PATH)

driver.get("https://accounts.spotify.com/en/authorize?client_id=09793e3afafa4797bf853f2ad5db72f3&redirect_uri=http://107.170.81.187:8080/SpotifyLoginCallback/&response_type=code&scope=user-read-recently-played+user-library-read+user-top-read&show_dialog=false&state=34fFs29kd09")


username = driver.find_element_by_id('login-username')
username.send_keys(str(userlogin))
time.sleep(1)

password = driver.find_element_by_id('login-password')
password.send_keys(str(passwordlogin)) #what a poopy password
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
time.sleep(3)

tracks_element = driver.find_element_by_xpath('/html/body/ol[4]')
tracks = tracks_element.text
songs = [tracks]
songnumber = len(songs)
i = 0
#print('[%s]' % ', '.join(map(str, songs)))  #cole got this from google
#print(tracks)

np.savetxt("top_songs_of_the_month.txt", np.array(songs), fmt="%s")

while i < songnumber:
    print(songs[i])
    i += 1

driver.get("https://open.spotify.com/search")
time.sleep(5)
pyautogui.write("Passenger Let Her Go")
pyautogui.hotkey("return")
pyautogui.moveTo(750,190)
time.sleep(1)
pyautogui.click(button='right')
time.sleep(.5)
pyautogui.moveTo(753,275)
pyautogui.click(button='left')
time.sleep(3)
pyautogui.moveTo(60,450)
