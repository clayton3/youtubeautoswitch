import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import playsound
import pyautogui
import math


#Main Driver function
def main():
    browser = setup("https://www.youtube.com/watch?v=DksSPZTZES0&list=PLpuDUpB0osJmZQ0a3n6imXirSu0QAZIqF")
    powerHour(browser)
    browser.close()

def gui(url):
    browser = setup(url)
    powerHour(browser)
    browser.close()

#Setup funcion for all the browsers core functionality
def setup(url):
    options = Options()
    options.add_extension("extension/ublock.crx")
    options.add_experimental_option('detach', True)

    browser = webdriver.Chrome(options=options)
    browser.get(url)

    time.sleep(2)

    browser.refresh()

    return browser

#Function to drive power hour
def powerHour(browser):
    closeCaption = browser.find_elements(By.CSS_SELECTOR, '.ytp-subtitles-button.ytp-button')
    if(closeCaption):
        closeCaption[0].click()
    else:
        print("Close Caption not available")

    fullscreen = browser.find_elements(By.CSS_SELECTOR, '.ytp-fullscreen-button.ytp-button')
    if(fullscreen):
        fullscreen[0].click()
    else:
        print("Fullscreen button not found")
    
    skip = browser.find_elements(By.CSS_SELECTOR, '.ytp-next-button.ytp-button')
    if(skip):
        playGame = True
        while(playGame):
            if(browser.find_elements(By.CSS_SELECTOR, "div.reason.style-scope.ytd-player-error-message-renderer")):
                skip[0].click()

            playsound.playsound("sounds/beer.wav")
            browser.execute_script('document.getElementsByTagName("video")[0].currentTime += 60;')
            time.sleep(60)
            skip[0].click()
            move()
    else:
        print("Skip button not found")

def move():
    screen_width, screen_height = pyautogui.size()
    target_x = 0
    target_y = screen_height // 2
    pyautogui.moveTo(target_x, target_y)

main()