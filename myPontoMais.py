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
    pyautogui.click(x=1555, y=156)

    time.sleep(1.5)
    pyautogui.click(x=1415, y=715)

## ========== saida para almoço ===========
## ========================================
if hoje.strftime("%H:%M") == "12:30":
    pyautogui.click(x=1555, y=156)

    time.sleep(1.5)
    pyautogui.click(x=1415, y=715)

## retorno do almoço ======================
## ========================================
if hoje.strftime("%H:%M") == "13:30":
    pyautogui.click(x=1555, y=156)

    time.sleep(1.5)
    pyautogui.click(x=1415, y=715)

## saida para lanche ======================
## ========================================
if hoje.strftime("%H:%M") == "16:00":
    pyautogui.click(x=1465, y=150)

    time.sleep(1.5)
    pyautogui.click(x=1424, y=556)

## retorno do lanche ======================
## ========================================
if hoje.strftime("%H:%M") == "16:15":     
    pyautogui.click(x=1465, y=150)

    time.sleep(1.5)
    pyautogui.click(x=1405, y=556)

## Saida ==================================
## ========================================
if hoje.strftime("%H:%M") == "17:45":     
    pyautogui.click(x=1555, y=156)

    time.sleep(1.5)
    pyautogui.click(x=1415, y=715)

time.sleep(5.5)
print(f"Ponto Registrado as: {hoje.strftime("%H:%M")} ")

## Fecha o navegador do ponto mais
# pyautogui.click(x=1898, y=19)

