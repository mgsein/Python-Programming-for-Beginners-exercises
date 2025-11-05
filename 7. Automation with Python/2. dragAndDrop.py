from selenium import webdriver
from selenium.webdriver import ActionChains

driver = webdriver.Firefox()
driver.maximize_window()
driver.get('http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html')
source = driver.find_element('xpath', '//*[@id="box3"]')
dest = driver.find_element('xpath', '//*[@id="box103"]')
actions = ActionChains(driver)
actions.drag_and_drop(source, dest).perform()

