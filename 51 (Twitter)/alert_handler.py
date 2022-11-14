
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

svce = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")

driver = webdriver.Chrome(service = svce)

location = 'file:///Users/randycastleman/Dropbox/Mac/Documents/local_code/100_days/51%20(Twitter)/simple_alert.html'
driver.get(location)

#Click on the "Alert" button to generate the Simple Alert
button = driver.find_element(By.NAME,'alert')
button.click()

#Switch the control to the Alert window
obj = driver.switch_to.alert

#Retrieve the message on the Alert window
msg=obj.text
print ("Alert shows following message: "+ msg )

time.sleep(2)

#use the accept() method to accept the alert
# obj.accept()
obj.dismiss()

print(" Clicked on the OK Button in the Alert Window")

driver.close