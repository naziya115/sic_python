import requests
from bs4 import BeautifulSoup
import pandas as pd
from time import sleep
import random
import requests

headers = {'Server': 'nginx', 'Date': 'Mon, 27 Mar 2023 11:20:06 GMT', 'Content-Type': 'text/html; charset=UTF-8', 'Transfer-Encoding': 'chunked', 'Connection': 'keep-alive', 'Set-Cookie': 'klssid=2j91cv2g0jhktalrt3cjlk9k3l; expires=Mon, 27-Mar-2023 11:50:06 GMT; Max-Age=1800; path=/; domain=.kolesa.kz; secure; HttpOnly, old_ssid=deleted; expires=Thu, 01-Jan-1970 00:00:01 GMT; Max-Age=0; path=/; secure, is_returning=0; path=/; secure', 'Expires': 'Thu, 19 Nov 1981 08:52:00 GMT', 'Cache-Control': 'no-store, no-cache, must-revalidate', 'Pragma': 'no-cache', 'X-Bug-Bounty': 'Please report bugs and vulnerabilities to bugs@kolesa.kz', 'Vary': 'Accept-Encoding, User-Agent', 'Strict-Transport-Security': 'max-age=31536000; preload', 'X-Frame-Options': 'SAMEORIGIN', 'Content-Security-Policy': "frame-ancestors 'self' https://webvisor.com", 'Alt-Svc': 'h3=":443"; ma=2592000,h3-29=":443"; ma=2592000,h3-Q050=":443"; ma=2592000,h3-Q046=":443"; ma=2592000,h3-Q043=":443"; ma=2592000,quic=":443"; ma=2592000; v="46,43"', 'Content-Encoding': 'gzip'}
response = requests.get('https://app.kolesa.kz/adverts/149948600/phones', headers=headers)
print(response.text)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager
#
# driver = webdriver.Chrome(ChromeDriverManager.install())
# driver.maximize_window()
# driver.get("https://kolesa.kz/a/show/150795982")
# driver.implicitly_wait(10)
# driver.find_element(By.XPATH, "").click()
