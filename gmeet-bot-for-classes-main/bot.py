
# TODO Desired outcome: A bot which can attend my classes in google meet background without it showing up at all

# * Features:
# * 1. Runs all the time in background, synced with calendar to attend any classes, can be turned on and off
# * 2. Gets in class 2 mins late and no need to leave as teacher ends the class 
# * 3. Replies "Yes Sir" listening thru voice recognition


# ! For this I will need to control, browser and calendar and google meet shortcuts if any.


# import required modules
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

class botinstance:

	def runInstance(self,link):
	    	# create chrome instance
		opt = Options()
		opt.add_argument('--disable-blink-features=AutomationControlled')
		opt.add_argument('--start-maximized')

		opt.add_experimental_option("prefs", {
			"profile.default_content_setting_values.media_stream_mic": 1,
			"profile.default_content_setting_values.media_stream_camera": 1,
			"profile.default_content_setting_values.geolocation": 0,
			"profile.default_content_setting_values.notifications": 1
		})
		driver = webdriver.Chrome(options=opt)
		
		mail_address = 'chinmay.a2019bds@srisriuniversity.edu.in'
		password = 'RBTXreader001'
	
		driver.get(
			'https://accounts.google.com/signin/v2/identifier?ltmpl=meet&continue=https%3A%2F%2Fmeet.google.com%3Fhs%3D193&&flowName=GlifWebSignIn&flowEntry=ServiceLogin')

		# input Gmail
		driver.find_element_by_id("identifierId").send_keys(mail_address)
		driver.find_element_by_id("identifierNext").click()
		driver.implicitly_wait(100)

		# input Password
		driver.find_element_by_xpath(
			'//*[@id="password"]/div[1]/div/div[1]/input').send_keys(password)
		driver.implicitly_wait(100)
		driver.find_element_by_id("passwordNext").click()
		driver.implicitly_wait(100)

		# go to google home page
		driver.get('https://google.com/')
		driver.implicitly_wait(100)



		driver.get(link)



		# * Turns off Mic AND Camera
		time.sleep(2)
		driver.find_element_by_class_name('GKGgdd').click()
		driver.implicitly_wait(3000)

		# turn off camera
		time.sleep(1)
		driver.find_element_by_class_name('GOH7Zb').click()
		driver.implicitly_wait(3000)

		# * Joins the meeting 

		print(1)
		time.sleep(5)
		driver.implicitly_wait(2000)
		driver.find_element_by_css_selector(
			'div.uArJ5e.UQuaGc.Y5sE8d.uyXBBb.xKiqt').click()
		print(1)

		time.sleep(5)
		driver.implicitly_wait(2000)
		driver.find_element_by_xpath(
			'/html/body/div[1]/c-wiz/div/div/div[9]/div[3]/div/div/div[4]/div/div/div[2]/div/div[2]/div/div[1]/div[1]/span/span').click()
		

botinstance().runInstance(link= 'https://meet.google.com/vha-vraf-kea')
