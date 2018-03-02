import requests
from bs4 import BeautifulSoup
from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options

def main():
    url = "http://www.usccb.org/bible/readings"
    option = webdriver.ChromeOptions()
    option.add_argument("log-level=3")
    option.add_argument('--headless')
    option.add_argument('--disable-gpu')
    driver = webdriver.Chrome("C:\\Users\\cvo\\Desktop\\chromedriver.exe", chrome_options=option)

    driver.get(url)

    timeout = 20

    try:
        WebDriverWait(driver,timeout).until(EC.visibility_of_element_located((By.XPATH, '//*[@id="contentarea"]')))
    except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()

    print("Scraping...\n\n")
    gospel_header = driver.find_element_by_xpath('//*[@id="cs_control_3684"]/div/div[3]/h4/a').text
    gospel_element = driver.find_element_by_xpath('//*[@id="cs_control_3684"]/div/div[3]/div').text


    gospel = gospel_header + '\n\n\n' + gospel_element

    return gospel
    driver.quit()

if __name__ == "__main__":
    gospel = main()
    print (gospel)
