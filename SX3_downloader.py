import os
import subprocess
import sys
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver

def Usage():
    print("Usage: $python SX3_downloader.py urlsFile")
    exit(1)

def NavigateUrl(url, cookieDismiss = False):
    print("Accedint a la web...")
    driver.get(url)

    #Cookies dismiss
    if cookieDismiss:
        acceptCookiesButton = driver.find_element(By.ID, "didomi-notice-agree-button")
        acceptCookiesButton.click()


    print("Clicant al play...")
    playButtonXPath = "//div[@aria-label='Reprodueix']"
    try:
        WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, playButtonXPath)))
    except Exception as e:
        print(e.msg)

    print("Buscant el link...")

def FindLink():
    for request in driver.requests:
        if request.response:
            if request.url.find('adaptive') != -1:
                url = request.url
                mpd = url.split("sprites")[0] + "stream.mpd"
                return mpd
            
def GetTitol():
    titol = driver.find_element(By.XPATH, "//h1[@class='titolMedia']").text
    titol = titol.replace('\"', '')
    titol = titol.replace('?', '')
    titol = titol.replace(':', '')
    return titol

if len(sys.argv) != 2:
    Usage()

fileName = sys.argv[1]
file = open(fileName)
urls = file.read().split('\n')

#Driver setup
options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)

for i in range(0, len(urls)):
    numberAttempts = 0
    url = urls[i]
    
    if i == 0: NavigateUrl(url, True)
    else: NavigateUrl(url)

    titol = GetTitol()

    while numberAttempts < 10:
        mpdUrl = FindLink()
        del driver.requests
        if mpdUrl == None:
            print("No s'ha trobat link mpd per " + titol + " a l'intent " + str(numberAttempts + 1))
            sleep(5)
            numberAttempts = numberAttempts + 1
            NavigateUrl(url)
        else:
            print("Descarregant " + titol + " de " + mpdUrl)
            subprocess.call(["youtube-dl", mpdUrl], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
            if not os.path.exists("./output/"):
                os.mkdir("./output/")
            os.rename("./stream-stream.mp4", "./output/" + titol + ".mp4")
            break

    
driver.quit()