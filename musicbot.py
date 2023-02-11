#day42


from selenium import webdriver

# Inicialize o driver do navegador
driver = webdriver.Chrome()

# Acesse o site de música
driver.get("https://www.youtube.com/")

# Localize a caixa de pesquisa no site
search_box = driver.find_element_by_xpath('//input[@id="search"]')

# Digite a música que você deseja reproduzir
search_box.send_keys("music name")
search_box.submit()

# Localize o primeiro vídeo na lista de resultados de pesquisa
video = driver.find_element_by_xpath('//a[@id="video-title"]')

# Clique no vídeo para reproduzí-lo
video.click()
