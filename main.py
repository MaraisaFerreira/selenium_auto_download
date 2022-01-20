from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

from time import sleep

url = 'https://fonts.google.com/'
font_name = 'Klee One'

browser = webdriver.Edge()
browser.get(url)

elem = WebDriverWait(browser, 5).until(
    ec.presence_of_element_located((By.ID, 'mat-input-0')))
elem.send_keys(font_name + Keys.ENTER)

font = WebDriverWait(browser, 5).until(
    ec.presence_of_element_located((By.PARTIAL_LINK_TEXT, font_name)))
font.click()

btn = WebDriverWait(browser, 5).until(
    ec.presence_of_element_located(
        (By.CSS_SELECTOR, '#main-content > gf-sticky-header >\
         div > div > button')))
btn.click()

sleep(20)
browser.quit()
