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


driver.get('https://www.junglescout.com/estimator/')
time.sleep(10)
popup = driver.find_elements_by_xpath('/html/body/div[6]/div/div[3]/div[1]/button[1]')

if(len(popup) > 0):
  popup[0].click()
#driver.refresh()

#driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
 
# click radio button
#python_button = driver.find_elements_by_xpath('//*[@id="x-section-2"]/div/div/div/section/div[2]/div[34]/div')[0]
divs = driver.find_element_by_class_name('marketplace-categories')
all_children_by_css = divs.find_elements_by_tag_name("div")
for all_children_by_cs in all_children_by_css:
  if "Home & Kitchen" == all_children_by_cs.text.strip():
    print(all_children_by_cs.text.strip())
    driver.execute_script("arguments[0].click();", all_children_by_cs)
    #all_children_by_cs.click()

print ('len(all_children_by_css): ' + str(len(all_children_by_css)))

#print(python_button)

#python_button.click()


#type Value
text_area = driver.find_elements_by_xpath('//*[@id="x-section-2"]/div/div/div/div[1]/div/div/input')[0]
print(text_area)
text_area.send_keys("50")


#Button Click

#find = driver.find_element_by_id('magicBtn')
#popup = driver.find_elements_by_xpath('/html/body/div[6]/div/div[3]/div[1]/button[1]')[0]
#popup.click()

#time.sleep(10)

find = driver.find_element_by_id('magicBtn')
find.click()


#Get Value

time.sleep(10)


sales_value = driver.find_elements_by_xpath('//*[@id="magicResult"]')[0].text

print(sales_value)
#sales_value.text = "12345"



#print(sales_value.text)
driver.quit()
print('--------------------------------')
''' 
# type text
text_area = driver.find_element_by_id('textarea')
text_area.send_keys("print('Hello World')")
 
# click submit button
submit_button = driver.find_elements_by_xpath('//*[@id="editor"]/table/tbody/tr[3]/td/table/tbody/tr/td/div/table/tbody/tr/td[3]/input')[0]
submit_button.click()
'''
