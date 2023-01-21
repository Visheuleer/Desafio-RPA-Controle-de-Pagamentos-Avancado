import datetime
import pandas as pd
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

def NavegarPagamentos(driver):
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath', '//*[@id="navcol-1"]/ul/li[2]/div/a/strong'))).click()
    WebDriverWait(driver, 10).until(EC.presence_of_element_located(('xpath', '//*[@id="navcol-1"]/ul/li[2]/div/div/a[1]'))).click()

def AumentaEntries(driver):
    entries = Select(WebDriverWait(driver, 10).until(EC.presence_of_element_located(('name', 'example_length'))))
    entries.select_by_visible_text('100')

def PegaTabela(url):
    return pd.read_html(url)

def ConverteListaDf(lista):
    return lista[0]

def IdentificaMoedaEstrangeira(df):
    return df.loc[(df['Moeda'] != 'BRL')]

def FormataData(df):
    datas = [datetime.datetime.strptime(data, '%d/%m/%Y').date() for data in df['Data']]
    return [data.strftime('%Y%m%d') for data in datas]

def BuscaCotacaoDia(moeda, dia):
    req = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{moeda}?start_date={dia}&end_date={dia}')
    if len(req.json())<=0:
        json = [{'low': 0}]
    else:
        json = req.json()
    return json

def FormataCotacao(json):
    cotacoes = []
    for j in json:
        for i in j:
            cotacoes.append(i['low'])
    return cotacoes

def AdicionaColunaCotacao(df, cotacoes):
    return df.assign(cotacao_dia=[round(float(cotacao),2) for cotacao in cotacoes])

def ConversaoValorReal(df):
    df['valor_em_real'] = df['Valor'] * df['cotacao_dia']
    return df

def GravaExcel(df):
    return df.to_excel('tabela.xlsx')

def ExtraiDados(driver):
    NavegarPagamentos(driver)
    AumentaEntries(driver)
    lista = PegaTabela(driver.current_url)
    df = ConverteListaDf(lista)
    df = IdentificaMoedaEstrangeira(df)
    datas = FormataData(df)
    json = [BuscaCotacaoDia('USD-BRL', data) for data in datas]
    cotacoes = FormataCotacao(json)
    df = AdicionaColunaCotacao(df, cotacoes)
    df = ConversaoValorReal(df)
    GravaExcel(df)


