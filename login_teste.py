from selenium import webdriver
import time
from selenium.webdriver.common.by import By



driver = webdriver.Chrome()

driver.get(r'http://localhost:3000')
# driver.get(r'https://www.amazon.com.br')
time.sleep(2)
driver.find_element(By.XPATH,'//*[@id="root"]/header/div[2]/div[2]/a[1]').click()
time.sleep(1)
#buscando campo do login e preenchendo 
driver.find_element(By.XPATH, '//*[@id="root"]/header/div[2]/form/div[1]/input').send_keys("ryan.s.franca.20@gmail.com")
 #buscando campo do senha e preenchendo
driver.find_element(By.XPATH, '//*[@id="root"]/header/div[2]/form/div[2]/input').send_keys("1234@Aaa")
#botao de login e dando um click
driver.find_element(By.XPATH, '//*[@id="root"]/header/div[2]/form/input').click()
time.sleep(10)




