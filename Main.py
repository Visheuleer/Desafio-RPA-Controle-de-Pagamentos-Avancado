import sys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from Login import Login
from ExtraiDados import ExtraiDados

try:
    servico = Service(ChromeDriverManager().install())
    driver = webdriver.Chrome(service=servico)
    Login(driver)
    ExtraiDados(driver)
    driver.quit()
    sys.exit()
except(Exception) as err:
    print(f'{type(err)}, {err}')