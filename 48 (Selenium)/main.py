from selenium import webdriver
from selenium.webdriver.chrome.service import Service


# chrome_driver_path = "/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
# got DEPRECATION error message, so the updated method (per https://stackoverflow.com/questions/64717302/deprecationwarning-executable-path-has-been-deprecated-selenium-python) is:
 
s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get("https://amazon.com")
