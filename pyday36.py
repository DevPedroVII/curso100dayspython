from selenium.webdriver import Firefox

url =' https://curso-pthon-netlify.app/aula_03.html'

navegador = Firefox()
navegador.get(url) - # poderia ser :navegador.get( https://curso-pthon-netlify.app/aula_03.html)
#so que como ja foi atribuído a variável url o site não é necessário
a = nagador.find_element_by_tag_name('a')
p = nagador.find_element_by_tag_name('p')
