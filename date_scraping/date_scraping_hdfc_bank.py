from bs4 import BeautifulSoup 
import requests
import datefinder 
from selenium import webdriver 

from selenium.webdriver.chrome.options import Options

# Set up Chrome options
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(options=chrome_options)

url = "https://www.hdfcbank.com/personal/save/accounts/savings-accounts/savings-account-interest-rate"
bcode = 207

def get_date():
    try:
        driver.get(url)
        soup = BeautifulSoup(driver.page_source, "html.parser")
        cn = soup.find("div", class_="bp-area HPD-template-hdfc-9-3--area col-lg-9 col-sm-8 large-side-scroll-fix clearfix")
        content = cn.find_all("p")
        # print(cn, content)
        # print(content)
        info = ""
        for i in content[5]:
            info += i.text 
        
        dates = datefinder.find_dates(info)
        redate = ""
        for date in dates:
            redate+= date.strftime("%d-%b-%y")

        driver.quit()
        return redate, bcode

    except:
        return "", bcode
    
# print(get_date())