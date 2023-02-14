from selenium import webdriver

driver = webdriver.Chrome()

driver.get('https://www.example.com')

assert 'Example Domain' in driver.title

driver.quit()


# Cria uma instância do driver do Chrome

# Abre a página que deseja testar

# Verifica se a página carregou corretamente

# Encerra o driver
