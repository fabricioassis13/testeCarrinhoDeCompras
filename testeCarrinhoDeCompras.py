import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from random import randint

def t(tempo):
    time.sleep(tempo)
m = "teste.fabricio.assis{ALEATORIO}@gmail.com".format(ALEATORIO=randint(1,10000000000000000))

driver = webdriver.Chrome(r'')  # O diretório do Chromedriver vai como parâmetro

# Redireciona para a página de um produto pré escolhido pro teste
driver.get('http://automationpractice.com/index.php?id_product=1&controller=product');

driver.set_window_size(1050, 708)
driver.find_element(By.CSS_SELECTOR, ".exclusive > span").click()
t(5) 
driver.find_element(By.CSS_SELECTOR, ".button-medium > span").click()

# Página de login, onde é escolhido criar um novo login
driver.find_element(By.CSS_SELECTOR, ".standard-checkout > span").click()
driver.find_element(By.ID, "email_create").click()
driver.find_element(By.ID, "email_create").send_keys(m)
driver.find_element(By.CSS_SELECTOR, "#SubmitCreate > span").click()
t(5)

# Preenchimento dos dados de criação de login
driver.find_element(By.ID, "id_gender1").click()
driver.find_element(By.ID, "customer_firstname").click()
driver.find_element(By.ID, "customer_firstname").send_keys("Teste")
driver.find_element(By.ID, "customer_lastname").click()
driver.find_element(By.ID, "customer_lastname").send_keys("Automático")
driver.find_element(By.ID, "passwd").click()
driver.find_element(By.ID, "passwd").send_keys("12345678")
driver.find_element(By.ID, "address1").click()
driver.find_element(By.ID, "address1").send_keys("asdasdasd")
driver.find_element(By.ID, "city").click()
driver.find_element(By.ID, "city").send_keys("asdasdasd")
driver.find_element(By.ID, "id_state").click()
dropdown = driver.find_element(By.ID, "id_state")
dropdown.find_element(By.XPATH, "//option[. = 'Kansas']").click()
driver.find_element(By.ID, "id_state").click()
driver.find_element(By.ID, "postcode").click()
driver.find_element(By.ID, "postcode").send_keys("12345")
driver.find_element(By.ID, "phone_mobile").click()
driver.find_element(By.ID, "phone_mobile").send_keys("1234567896")
driver.find_element(By.ID, "alias").click()
driver.find_element(By.ID, "center_column").click()
driver.find_element(By.ID, "alias").send_keys("asdasdasd")
driver.find_element(By.CSS_SELECTOR, "#submitAccount > span").click()

# Checagens finais da compra
driver.find_element(By.CSS_SELECTOR, ".button:nth-child(4) > span").click()
driver.find_element(By.ID, "cgv").click()
driver.find_element(By.CSS_SELECTOR, ".standard-checkout > span").click()
driver.find_element(By.CSS_SELECTOR, ".bankwire > span").click()
driver.find_element(By.CSS_SELECTOR, "#cart_navigation span").click()
t(5)

