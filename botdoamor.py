


#crie um bot que diga: "te amo meu amor" usando python e selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
time.sleep(10)

name = input("Digite o nome do contato:")
msg = input("Digite a mensagem: ")
count = int(input("Digite a quantidade de vezes que deseja enviar: "))

input("Aperte qualquer tecla para continuar...")

user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
user.click()

msg_box = driver.find_element_by_class_name('_3u328')

for i in range(count):
    msg_box.send_keys(msg)
    button = driver.find_element_by_class_name('_3M-N-')
    button.click()
