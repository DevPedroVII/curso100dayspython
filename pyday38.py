from selenium.webdriver import Chrome


def find_by_tag_name(browser, tag, text):
    elemento = browser.find_element_by_tag_name(tag)

    for elemento in elemento:
        if elemento.text == text:
            return elemento



def find_by_href(browser, tag, text):
browser.get('http://selenium.dunossauro.live/aula_04_a.html')


elemento_Cho = find_by_text(browser,"a","Chrome")



lista_n_ordenada = browser.find_element_by_tag_name('ul')

Lis = lista_n_ordenada.browser.find_element_by_tag_name('li')

Lis [0].find_element_by_tag_name('a').text

#day 39
