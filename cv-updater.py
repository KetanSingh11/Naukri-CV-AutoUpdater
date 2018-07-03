from selenium import webdriver
from selenium.webdriver.firefox.options import Options
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


options = Options()
# options.set_headless(headless=True)
## options.add_argument("--headless")

browser = webdriver.Firefox(firefox_options=options, executable_path="geckodriver/geckodriver.exe", log_path="geckodriver/geckodriver.log")
# assert options.headless  # operating in headless mode
print("Firefox Headless Browser Invoked")
# browser.implicitly_wait(10) # seconds

print("Opening: {}".format("https://login.naukri.com/nLogin/Login.php"))
browser.get("https://login.naukri.com/nLogin/Login.php")

try:
	element = WebDriverWait(browser, timeout=10, poll_frequency=3).until(EC.presence_of_element_located((By.ID, "usernameField")))
	element = WebDriverWait(browser, timeout=10, poll_frequency=3).until(EC.presence_of_element_located((By.ID, "passwordField")))
except Exception as e:
	print(e)
finally:
	browser.find_element_by_id('usernameField').send_keys('abc@def.com')
	# time.sleep(4)
	passwd = browser.find_element_by_id('passwordField')
	passwd.send_keys('123456')

	time.sleep(3)
	# passwd.submit()
	# browser.find_element_by_xpath('/html/body/div[2]/div/div/div/div/div/div/div[2]/div/form/div[5]/div/button').click()
	browser.find_element_by_id("loginForm").submit()


try:
	# wait till you find a search box i.e. page has loaded completely
	element = WebDriverWait(browser, timeout=10, poll_frequency=2).until(EC.presence_of_element_located((By.ID, "qsb-keyskill-sugg")))
except Exception as e:
	print(e)

print("Opening: {}".format("https://my.naukri.com/Profile/edit?id=&altresid"))
browser.get("https://my.naukri.com/Profile/edit?id=&altresid")
browser.find_element_by_xpath("/html/body/div[2]/div/div/span/div/div/div/div/div[2]/div[1]/div/div/ul/li[12]/a").click()

# scroll to bottom of the page to load ajax elements
browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
time.sleep(5)

try:
	element = WebDriverWait(browser, timeout=10, poll_frequency=2).until(EC.presence_of_element_located((By.ID, "attachCV")))
except Exception as e:
	print(e)
finally:
	# time.sleep(4)
	browser.find_element_by_id("attachCV").send_keys("Resume.docx")
	# time.sleep(2)


# browser.close()
# browser.quit()