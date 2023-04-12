import os
import subprocess
from urllib import request

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from seleniumwire import webdriver

def findLink():
    for request in driver.requests:
        if request.response:
            if request.url.find('adaptive') != -1:
                url = request.url
                mpd = url.split("sprites")[0] + "stream.mpd"
                return mpd

print("Accedint a la web...")

options = webdriver.ChromeOptions()
options.add_argument('headless')
driver = webdriver.Chrome(options=options)
driver.get("https://www.ccma.cat/tv3/sx3/busquem-la-maria-1a-part/video/6211296/")
acceptCookiesButton = driver.find_element(By.ID, "didomi-notice-agree-button")
acceptCookiesButton.click()
titol = driver.find_element(By.XPATH, "//h1[@class='titolMedia']").text

print("Clicant al play...")

playButtonXPath = "//div[@aria-label='Reprodueix']"
try:
    playButton = WebDriverWait(driver, 10).until(expected_conditions.presence_of_element_located((By.XPATH, playButtonXPath)))
except Exception as e:
    print(e.msg)

print("Buscant el link...")

url = findLink()
print("Descarregant " + titol)
subprocess.call(["youtube-dl", url])
os.rename("./stream-stream.mp4", "./" + titol + ".mp4")

driver.quit()