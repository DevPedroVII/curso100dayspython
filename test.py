from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.example.com')

assert 'Example Domain' in driver.title
