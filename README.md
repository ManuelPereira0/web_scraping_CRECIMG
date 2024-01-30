# Web Scraping Site CRECI MG

## Programa de coleta de dados de consultores imobiliários do estado de Minas Gerais: https://crecimg.spiderware.com.br/spw/consultacadastral/TelaConsultaPublicaCompleta.aspx

# Passo a passo para utilizar o programa
> 2 programas, que diferenciam os tipos de pessoas na hora de realizar a coleta de dados </br>
> Basta selecionar o tipo de pessoa e a cidade, logo após, teclar ENTER no terminar para prosseguir com o programa

## Configurar DB
> Atualizar as informações abaixo para o seu DB
```python
host='seu host',
user='seu user',
database='seu database',
password='sua password',
```

### No Linux
Bibliotecas para serem instaladas:
- instalar o pip: sudo apt-get install python3-pip
- pip install selenium 
- pip install pymysql
- pip install bs4 
- pip install pyautogui
- sudo apt update
- sudo apt install firefox 
> Somente se não tiver o FireFox instalado no computador

### No Windows
Para fazer a instalação da versão mais recente do Python no Windows: https://www.python.org/downloads/windows/
- pip install selenium 
- pip install pymysql
- pip install bs4 
- pip install pyautogui

### Para rodar o programa
> No Linux: python3 nome_do_arquivo.py <br>
> No Windows: python nome_do_arquivo.py