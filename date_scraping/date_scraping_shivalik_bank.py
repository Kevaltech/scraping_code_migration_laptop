import requests
from bs4 import BeautifulSoup
import datefinder
from selenium import webdriver

from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)

url = "https://shivalikbank.com/interest-rate#savings-account"
bcode = 307


def get_date():
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        cn = soup.find("div", class_="card-body table_sec")
        content = cn.find_all("h3")
        info = ""
        for i in content:
            info += i.text 
        
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")
        driver.quit()
        return redate,  bcode

    except:
        return "",  bcode
    
# print(get_date())