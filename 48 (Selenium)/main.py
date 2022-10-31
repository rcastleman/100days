from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

URL = "https://www.amazon.com/Instant-Pot-6Qt-Plus-WiFi/dp/B08TMTJZ8L?ref_=ast_sto_dp"


# chrome_driver_path = "/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# got DEPRECATION error message, so the updated method (per https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python) is:

x_path = "//*[@id='corePriceDisplay_desktop_feature_div']/div[1]/span/span[1]"
class_name = "a-offscreen"
 
s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)
# price = driver.find_element_by_class_name("a-offscreen")
price = driver.find_element(By.CLASS_NAME,class_name)
# price = driver.find_element(By.XPATH,x_path)
print(price.text)
# driver.close() #closes a tab
driver.quit() #closes the entire browser