from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.common.by import By
def Preenche_Campos(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(('id', 'user'))).send_keys('aluno')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(('id', 'pass'))).send_keys('desafiosrapa')

def Pega_Expressao(driver):
    expressao = WebDriverWait(driver, 10).until(EC.presence_of_element_located(('id', 'lbltipAddedComment'))).get_attribute('innerText')
    return expressao

def CalculaExpressao(expressao):
    return eval(expressao)

def PreencheExpressao(driver, resultado):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(('id', 'cap'))).send_keys(resultado)

def Login(driver):
    driver.get('https://desafiosrpa.com.br/login.html')
    Preenche_Campos(driver)
    expressao = Pega_Expressao(driver)
    resultado = CalculaExpressao(expressao)
    PreencheExpressao(driver, resultado)
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath', '//*[@id="corpo-desafio"]/div/form/fieldset/button'))).click()






