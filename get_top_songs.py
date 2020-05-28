#spotify automation
# saves top songs of the month to a text file

import time
import numpy as np
import selenium
import pyautogui
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

#import google_auth_oauthlib.flow
#import googleapiclient.discovery
#import googleapiclient.errors
#import requests
#import youtube_dl
#from exceptions import ResponseException
#from exceptions import ResponseException
#from secrets import spotify_token, spotify_user_id



userlogin = input('Enter username: ') # reb1221
passwordlogin = input('Enter password: ') # Xq3Ws5m@5U2D
time.sleep(1)


driver = webdriver.Chrome(ChromeDriverManager().install())

PATH = "/users/rebridge/Spotify Automation/chromedriver"

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
#print('[%s]' % ', '.join(map(str, songs)))
#print(tracks)

# collect sorngs into an array
np.savetxt("top_songs_of_the_month.txt", np.array(songs), fmt="%s")
driver.close()
