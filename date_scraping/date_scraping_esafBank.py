from bs4 import BeautifulSoup 
import requests
import datefinder
import html2text
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)
url = "https://www.esafbank.com/interest-rates/"
bcode = 303

def get_date():
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        table_info = soup.find("div", id="collapse-1")
        # print(table_info)
        info = table_info.find_all('th')
        # print(info)
        information =""
        for i in info[1]:
            information += i.text 
        dates = datefinder.find_dates(information)
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")

        driver.quit()
        return redate, bcode
    except:
        return "", bcode
    
# print(get_date())