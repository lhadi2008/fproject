from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
# Create a WebDriver instance (e.g., Chrome, Firefox, etc.)
browser = webdriver.Chrome()

# Navigate to a web page
browser.get('https://food.jumia.ma/restaurants')

#sleep(2)
# Removing ad by clicking in button remove
remove_ad = browser.find_element("xpath", '/html/body/section/main/main/div[2]/div/main/section/div[1]/div/div[2]/div[1]/input')
remove_ad.send_keys('GOMYCODE Rabat, l’immeuble BEL AIR, Rue Zalagh')
sleep(6)
remove_ad.click()
# Writing in the search box 'Samsung' and executing the research
#search_button = browser.find_element('xpath','/html/body/div[1]/header/section/form/div/input')
#sleep(5)
#search_button.send_keys('Samsung')
click_search = browser.find_element('xpath','/html/body/section/main/main/div[2]/div/main/section/div[1]/div/div[2]/div[2]/div[1]')
click_search.click()
sleep(3)
#Click to show results
click_sear = browser.find_element('xpath','/html/body/section/main/main/div[2]/div/main/section/div[1]/button')
click_sear.click()

# click_searc = browser.find_element('xpath','/html/body/section/main/main/div[2]/div/main/section/div[1]/button')
# click_searc.click()
# sleep(3)
# click the image
# Initialize the WebDriver

sleep(30)
element = browser.find_element(By.XPATH,'/html/body/section/main/main/div/section[2]/div[2]/div/article[2]/a')
      
# Click the burger
click_burger = browser.find_element('xpath','/html/body/section/main/main/div/div/div[2]/section/div/div/section/section[1]/section/article/div/div[1]/div/a/span[3]')
click_burger.click()
#
click_burger_options = browser.find_element('xpath','/html/body/section/main/main/div[2]/div/main/section/form/div/div[1]/div/div[1]/div/label')
click_burger_options.click()
#
click_burger_option = browser.find_element('xpath','/html/body/section/main/main/div[2]/div/main/section/form/div/div[2]/div/div[1]/div/label')
click_burger_option.click()
#
click_burger_optio = browser.find_element('xpath','/html/body/section/main/main/div[2]/div/footer/div/button')
click_burger_optio.click()
#
sleep(3)
click_burger_opt = browser.find_element('xpath','/html/body/section/main/main/div/div/aside/section/div[2]/div[2]/a')
click_burger_opt.click()
#
click_burger_opt = browser.find_element('xpath','/html/body/div/div[4]/form/div[1]/div[2]/div/div[2]/label')
click_burger_opt.click()
click_burger_opt.send_keys('moolhadi2@gmail.com')







# Don't forget to close the browser when you're done
#browser.quit()
