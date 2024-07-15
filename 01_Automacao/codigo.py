# Passo a passo do projeto

# 1. Abrir o sistema da empresa
    # https://dlp.hashtagtreinamentos.com/python/intensivao/login

# Para instalar: pip install autogui
import pyautogui
import time

pyautogui.PAUSE = 0.8

# pyautogui.click -> clicar com o mouse
# pyautogui.write -> escrever um texto
# pyautogui.press -> pressionar uma tecla do teclado
# pyautogui.hotkey -> apertar um conjunto de teclas (ctrl C, ctrl V, alt tab)

# Abrir o navegador (chrome)
pyautogui.press('win')
pyautogui.write("chrome")
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=600, y=435)


# Entrar no sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# Aqui pode ser que ele demore alguns segundos para carregar o site
time.sleep(3)

# 2. Fazer login
pyautogui.click(x=493, y=402)
pyautogui.write('python@gmail.com')

pyautogui.press('tab')
pyautogui.write('Sua senha aqui')

pyautogui.press('tab')
pyautogui.press('enter')

time.sleep(3)

# 3. Abrir/Importar a base de dados do produto para cadastar
# pip install pandas numpy openpyxl
import pandas as pd
# tabula transforma pdf em pandas

tabela = pd.read_csv("produtos.csv")

print(tabela)

# 4. Cadastrar um produto

for linha in tabela.index:
    codigo = str(tabela.loc[linha, 'codigo'])
    # clicar no campo do código do produto
    pyautogui.click(x=543, y=295)
    # preencher o código
    pyautogui.write(codigo)
    # passar para o próximo campo
    pyautogui.press('tab')
    # marca
    pyautogui.write(str(tabela.loc[linha, 'marca']))
    # passar para o próximo campo
    pyautogui.press('tab')
    # tipo
    pyautogui.write(str(tabela.loc[linha, 'tipo']))
    # passar para o próximo campo
    pyautogui.press('tab')
    # categoria
    pyautogui.write(str(tabela.loc[linha, 'categoria']))
    # passar para o próximo campo
    pyautogui.press('tab')
    # preço
    pyautogui.write(str(tabela.loc[linha, 'preco_unitario']))
    # passar para o próximo campo
    pyautogui.press('tab')
    # custo
    pyautogui.write(str(tabela.loc[linha, 'custo']))
    # passar para o próximo campo
    pyautogui.press('tab')
    # obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != 'nan':
        pyautogui.write(obs)
    # passar para o próximo campo
    pyautogui.press('tab')
    # apertar o botão
    pyautogui.press('enter')
    pyautogui.scroll(5000) # pyautogui.press('home')

# piperclip -> caracteres especiais
# 5. Repetir isso tudo até acabar a lista de produtos