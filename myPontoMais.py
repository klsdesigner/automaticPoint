import pyautogui
from datetime import date, time, datetime, timedelta
import time

pyautogui.PAUSE = 0.5

hoje = datetime.now()

pyautogui.press('win')
pyautogui.write("google chrome")
pyautogui.press("enter")

url = "https://app2.pontomais.com.br/meu-ponto"
pyautogui.write(url)
pyautogui.press("enter")

## Verificar o horario p registro do pronto
time.sleep(2)

## ========= Entrada ======================
## ========================================
if hoje.strftime("%H:%M") == "08:00":
    pyautogui.click(x=1556, y=146) 

    time.sleep(1.5)
    pyautogui.click(x=1411, y=721)


## ========== saida para almoço ===========
## ========================================
if hoje.strftime("%H:%M") == "12:30":
    pyautogui.click(x=1556, y=146) 

    time.sleep(1.5)
    pyautogui.click(x=1411, y=721)

## retorno do almoço ======================
## ========================================
if hoje.strftime("%H:%M") == "13:30":
    pyautogui.click(x=1556, y=146) 

    time.sleep(1.5)
    pyautogui.click(x=1411, y=721)

## saida para lanche ======================
## ========================================
if hoje.strftime("%H:%M") == "16:00":
    pyautogui.click(x=1463, y=153)

    time.sleep(1.5)
    pyautogui.click(x=1411, y=561) 

## retorno do lanche ======================
## ========================================
if hoje.strftime("%H:%M") == "16:15":     
    pyautogui.click(x=1463, y=153)

    time.sleep(1.5)
    pyautogui.click(x=1411, y=561) 

## Saida ==================================
## ========================================
if hoje.strftime("%H:%M") == "17:45":     
    pyautogui.click(x=1556, y=146) 

    time.sleep(1.5)
    pyautogui.click(x=1411, y=721)

time.sleep(12)
print(f"Ponto Registrado as: {hoje.strftime("%H:%M")} ")

pyautogui.click(x=86, y=238)

time.sleep(2)
pyautogui.click(x=1629, y=453)

time.sleep(2)
pyautogui.click(x=1552, y=523)



