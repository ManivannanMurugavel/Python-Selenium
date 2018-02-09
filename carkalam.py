from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


'''options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
#options.binary_location = "/usr/bin/chromium-browser"
options.binary_location = "/usr/lib/chromium-browser/chromedriver"
'''
driver = webdriver.Chrome("./chromedriver")

#driver = webdriver.Firefox()

driver.maximize_window()
#driver.implicitly_wait(30)

#actions = ActionChains(driver)
#about = driver.find_element_by_link_text('About')
#actions.key_down(Keys.CONTROL).click(about).key_up(Keys.CONTROL).perform()

#driver.switch_to.window(driver.window_handles[-1])


driver.get('http://carkalam.in/add_seller_vehicle.php')

time.sleep(5)

cusname = driver.find_element_by_id('csd_vCustomerName')
cusname.send_keys("Hello")

mobile = driver.find_element_by_id('csd_vMobile')
mobile.send_keys(123456789)

email = driver.find_element_by_id('csd_vEmail')
email.send_keys("wel@gmail.com")

version = driver.find_elements_by_xpath('/html/body/div/div/div[2]/div/div/div/div/div/form/div[10]/div[2]/div/input')[0]
version.send_keys("hjsdv612")


second_no = driver.find_element_by_id('second_no')
second_no.send_keys(25)


third_no = driver.find_element_by_id('third_no')
third_no.send_keys("AT")

comment = driver.find_element_by_id('comment')
comment.send_keys(1234)

price = driver.find_element_by_id('csd_iPrice')
price.send_keys(12000)

photoimg = driver.find_element_by_id('photoimg')
photoimg.send_keys('/home/manivannan/pythonexamle/selenium_example/chicago.jpg')

