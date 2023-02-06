from selenium.webdriver import Chrome

browser = Chrome ()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

lista_n_ordenada = browser.find_element_by_tag_name('ul')
