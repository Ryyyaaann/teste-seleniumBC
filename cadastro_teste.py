from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


driver = webdriver.Chrome()

driver.get(r'http://localhost:3000')
# driver.get(r'https://www.amazon.com.br')
time.sleep(2)
#botao de cadastro e dando um click
driver.find_element(By.XPATH,'//*[@id="root"]/header/div[2]/div[2]/a[2]').click()
time.sleep(2)

def slow_type(element, text):
    for char in text:
        element.send_keys(char)
        time.sleep(0.2)  # 200ms entre cada caractere
#buscando os demais campos e preenchendo
#busca realizada pelo nome do elemento
driver.find_element(By.NAME, 'nome').send_keys("Ryan")

driver.find_element(By.NAME, 'sobrenome').send_keys("Franca")

driver.find_element(By.NAME, 'email').send_keys("ryan@gmail.com")

driver.find_element(By.NAME, 'username').send_keys("Ryan")

cpf_input = driver.find_element(By.NAME, 'cpf')


cpf_input = driver.find_element(By.NAME, 'cpf')
cpf = "123.456.789-10"
actions = ActionChains(driver)
actions.move_to_element(cpf_input)
actions.click()
for digit in cpf:
    actions.send_keys(digit)
    actions.pause(0.1)  # Add a small pause between each character
actions.perform()

driver.find_element(By.NAME, 'password').send_keys("ran123")
driver.find_element(By.NAME, 'confirmaPassword').send_keys("ran123")

data_nascimento_input = driver.find_element(By.NAME, 'dataNascimento')
slow_type(data_nascimento_input, "20041225")
# driver.find_element(By.NAME, 'dataNascimento').send_keys("15252004")
# Preenchendo o CPF via JavaScript

# Preenchendo a data de nascimento via JavaScript




#botao de emissão e dando um click
#busca realizada pela tag do elemento pois é unica
driver.find_element(By.XPATH, '//*[@id="root"]/header/form/input[9]').click()

#aguardando 2 segundos para ver se a pagina foi redirecionada
time.sleep(2)