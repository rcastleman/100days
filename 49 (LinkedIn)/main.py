from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from dotenv import load_dotenv
import os

load_dotenv()

URL = 'https://www.linkedin.com/jobs/search/?currentJobId=3344172382&f_AL=true&f_C=21836&f_E=1&f_WT=2&geoId=103644278&keywords=python%20developer&location=United%20States&refresh=true&sortBy=R'

sign_in_URL = 'https://www.linkedin.com/login?emailAddress=&fromSignIn=&fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs%2Fsearch%2F%3FcurrentJobId%3D3344172382%26f_AL%3Dtrue%26f_C%3D21836%26f_E%3D1%26f_WT%3D2%26geoId%3D103644278%26keywords%3Dpython%2520developer%26location%3DUnited%2520States%26refresh%3Dtrue%26sortBy%3DR&trk=public_jobs_nav-header-signin'

sign_in_1_x_path = '/html/body/div[1]/header/nav/div/a[2]'
sign_in_2_x_path = '//*[@id="username"]'
password_x_path = '//*[@id="password"]'
sign_in_2_button_x_path = '//*[@id="organic-div"]/form/div[3]/button'


user_id= os.environ.get("USER_ID")
password = os.environ.get("PASS")

#----- open initial pages ------#

s = Service("/Users/randycastleman/Dropbox/Mac/Documents/local_code/chrome/chromedriver")
driver = webdriver.Chrome(service = s)
driver.get(URL)

#----- click on Sign In ------#

sign_in = driver.find_element(By.XPATH,sign_in_1_x_path)
sign_in.click()

# #---------enter login credentials on sign in page ---------- #

sign_in_2 = driver.find_element(By.XPATH,sign_in_2_x_path)
sign_in_2.send_keys(user_id)

pass_entry = driver.find_element(By.XPATH,password_x_path)
pass_entry.send_keys(password)

sign_in_2_button = driver.find_element(By.XPATH,sign_in_2_button_x_path)
sign_in_2_button.click()

#---------- store jobs --------------------- #

all_listings = driver.find_elements(By.CSS_SELECTOR,".job-card-container--clickable")

job_list = []

for element in all_listings:
    job_list.append(element.get_attribute("value"))

with open("jobs_list.txt",mode='w') as file:
    file.write(job_list)

# follow_button = driver.find_element(By.XPATH,'//*[@id="ember354"]/section/div[1]/div[1]/button/span')
# follow_button.click()