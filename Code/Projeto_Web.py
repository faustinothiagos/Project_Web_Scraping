# IMPORTANDO OS MÓDULOS
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from time import sleep
from datetime import datetime
import os

# VERIFICANDO E BAIXANDO A VERSÃO ATUAL DO DRIVERMANAGER PARA O CHROME
servico = Service(ChromeDriverManager().install())

# NAVEGADOR RECONHECENDO A VERSÃO MAIS RECENTE DO DRIVEMANAGER PARA O CHROME
navegador = webdriver.Chrome(service=servico)

# CRIAR A PASTA DE ARQUIVO
pasta_alvo = 'transparencia.al.gov.br/' 
if(not os.path.exists(pasta_alvo)):
     os.mkdir(pasta_alvo)

# ABRINDO O NAVEGADOR NA PÁGINA SERVIDOR ATIVO:
navegador.get("https://transparencia.al.gov.br/portal/download-de-dados/pessoal/servidor-ativo")

# BAIXANDO O ARQUIVO ZIP DA PAGINA
navegador.find_element('xpath', '//*[@id="lista-arquivos"]/a[1]').click()

# TEMPO DE ESPERA  DE 7s PARA FECHAR A PÁGINA
sleep(7)

# ABRINDO O NAVEGADOR NA PÁGINA SERVIDOR INATIVO:
navegador.get("https://transparencia.al.gov.br/portal/download-de-dados/pessoal/servidor-inativo")

# BAIXANDO O ARQUIVO ZIP DA PAGINA
navegador.find_element('xpath', '//*[@id="lista-arquivos"]/a[1]').click()

# TEMPO DE ESPERA  DE 7s PARA FECHAR A PÁGINA
sleep(7)

# ABRINDO O NAVEGADOR NA PÁGINA ÓRGÃO FOLHA :
navegador.get("https://transparencia.al.gov.br/portal/download-de-dados/pessoal/orgao-folha")

# BAIXANDO O ARQUIVO ZIP DA PAGINA
navegador.find_element('xpath', '//*[@id="lista-arquivos"]/a[1]').click()

# TEMPO DE ESPERA  DE 7s PARA FECHAR A PÁGINA
sleep(7)

# FECHANDO O NAVEGADOR.
navegador.quit()