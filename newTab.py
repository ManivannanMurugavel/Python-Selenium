import selenium.webdriver as webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.keys import Keys
from time import sleep
import time
from selenium.webdriver.common import action_chains, keys

 
'''options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument("--test-type")
#options.binary_location = "/usr/bin/chromium-browser"
options.binary_location = "/usr/lib/chromium-browser/chromedriver"
'''
driver = webdriver.Chrome("./chromedriver")

from selenium.webdriver.common.action_chains import ActionChains


driver.get('http://google.com')

time.sleep(3)


element = driver.find_element_by_link_text('About')

ActionChains(driver).key_down(Keys.CONTROL).send_keys('t').key_up(Keys.CONTROL).perform()

time.sleep(10) # Pause to allow you to inspect the browser.

driver.quit()

#import os
#os.system("./script.ahk")

'''first_result = ui.WebDriverWait(browser, 15).until(lambda browser: browser.find_element_by_class_name('rc'))
first_link = first_result.find_element_by_tag_name('a')

# Save the window opener (current window, do not mistaken with tab... not the same)
main_window = browser.current_window_handle

# Open the link in a new tab by sending key strokes on the element
# Use: Keys.CONTROL + Keys.SHIFT + Keys.RETURN to open tab on top of the stack 
#first_link.send_keys(Keys.CONTROL + Keys.RETURN)

# Switch tab to the new tab, which we will assume is the next one on the right
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + Keys.SHIFT + 'i')
    
# Put focus on current window which will, in fact, put focus on the current visible tab
browser.switch_to_window(main_window)

# do whatever you have to do on this page, we will just got to sleep for now
sleep(2)
print("sdcsdcds")
# Close current tab
browser.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w')

# Put focus on current window which will be the window opener
browser.switch_to_window(main_window)'''
