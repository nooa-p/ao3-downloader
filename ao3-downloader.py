import sys
import os
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.headless = True
options.set_preference('browser.download.folderList', 2)
options.set_preference('browser.download.manager.showWhenStarting', False)
options.set_preference('browser.download.dir', os.path.join(os.path.expanduser("~"), "Downloads\\"))
options.set_preference('browser.helperApps.neverAsk.saveToDisk', 'text/html')

driver = webdriver.Firefox(options=options)
driver.get('https://archiveofourown.org/works/22334818')

dl_button = driver.find_element_by_class_name('download')
dl_button.click()

html_button = driver.find_element_by_link_text('HTML')
html_button.click()

driver.close()