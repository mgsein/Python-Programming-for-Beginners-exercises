from selenium import webdriver
driver = webdriver.Firefox()
driver.get('https://demo.seleniumeasy.com/basic-first-form-demo.html')

messageField = driver.find_element('xpath','//*[@id="user-message"]')
messageField.send_keys('Hello Mg Sein!')
showMessageButton = driver.find_element('xpath','/html/body/div[2]/div/div[2]/div[1]/div[2]/form/button')
showMessageButton.click()

additionField1 = driver.find_element('xpath', '//*[@id="sum1"]')
additionField1.send_keys('20')
additionField2 = driver.find_element('xpath', '//*[@id="sum2"]')
additionField2.send_keys('21')
getTotalButton = driver.find_element('xpath', '/html/body/div[2]/div/div[2]/div[2]/div[2]/form/button')
getTotalButton.click()