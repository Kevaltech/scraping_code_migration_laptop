import requests
from bs4 import BeautifulSoup
import datefinder
import html2text
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)

url = 'https://www.aubank.in/interest-rates/savings-account-interest-rates'
bcode = 300

def get_date():
    try:
        driver.get(url)
        # print(response)
        # if response.status_code == 200:
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        # print(soup)
        table_info = soup.find('div', class_="container padbt0")
        content = table_info.find_all('h3')
        # print(content)
        info = ""
        for i in content:
            info += i.text
        # print(info)
        dates = datefinder.find_dates(info)
        redate = ""
        driver.quit()
        for date in dates:
            redate+= date.strftime("%d-%b-%y")
        return redate, bcode
        
    except:
        return "",bcode
    
# val = get_date()
# print(val)