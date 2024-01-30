from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import pymysql.cursors
from bs4 import BeautifulSoup
import pyautogui

def criar_conexao():
    return pymysql.connect(
        host='1seu host',
        user='seu user',
        database='seu database',
        password='sua password',
        cursorclass=pymysql.cursors.DictCursor
    )
    
def iniciar_driver():
    driver = webdriver.Firefox()
    driver.get("https://crecimg.spiderware.com.br/spw/consultacadastral/TelaConsultaPublicaCompleta.aspx")
    return driver

def capturar_conteudo():
    return driver.page_source

contador_registro = 1
conexao = criar_conexao()
cursor = conexao.cursor()

driver = iniciar_driver()

input("Faça as interações manuais: (Logo após tecle ENTER)")

sleep(2)
pyautogui.press("pagedown")

pyautogui.moveTo(1247, 624)
sleep(0.5)

pyautogui.click()
sleep(0.2)

pyautogui.moveTo(1227, 591)
sleep(0.5)
pyautogui.click()
sleep(4)

while True:
    sleep(10)
    pyautogui.press("pagedown")
    sleep(0.5)
    
    page_source = driver.page_source
    soup = BeautifulSoup(page_source, 'html.parser')
    table = soup.find('table', {'id': 'ContentPlaceHolder1_Callbackconsulta_gridconsultaempresa_DXMainTable'})
    
    if table:
        print("Tabela encontrada")
        trs = table.find_all('tr')
        
        for tr in trs[1:]:
            tds = tr.find_all('td')
            print(len(tds))
            if len(tds) >= 4:
                registro = tds[0].text.strip()
                nome = tds[1].text.strip()
                nome_fantasia = tds[2].text.strip()
                situacao = tds[3].text.strip()
                
                registro = registro.replace('"', "'")
                nome = nome.replace('"', "'")
                nome_fantasia = nome_fantasia.replace('"', "'")
                situacao = situacao.replace('"', "'")
                
                inserir_dados = f"""insert into 20231108_creci 
                (numero_registro, nome, situacao, tipo_pessoa, uf, nome_fantasia)
                values ("{registro}", "{nome}", "{situacao}", "PJ", "MG", "{nome_fantasia}")"""

                cursor.execute(inserir_dados)
                conexao.commit()
                print(f'Dados inseridos no DB, registro Nº: {contador_registro}')
                contador_registro += 1
            else:
                print("Alguns dos campos não estão presentes nesta linha")
            
        cursor.close()
        conexao.close()

        conexao = criar_conexao()
        cursor = conexao.cursor()

    try:
        proxima_pagina = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".dxWeb_pNext_MetropolisBlue"))
        )
        proxima_pagina.click()
    except NoSuchElementException:
        print("Acabou")
        break