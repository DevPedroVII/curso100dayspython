from selenium.webdriver import Chrome

def find_by_tag_name(browser, tag, text):
    elemento = browser.find_element_by_tag_name(tag)

    for elemento in elemento:
        if elemento.text


browser = Chrome ()

browser.get('http://selenium.dunossauro.live/aula_04_a.html')

lista_n_ordenada = browser.find_element_by_tag_name('ul')

Lis = lista_n_ordenada.browser.find_element_by_tag_name('li')

Lis [0].find_element_by_tag_name('a').text

