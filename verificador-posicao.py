import pyautogui
import time

count = 0

posicoes = [()]
while count < 15:
    for posicao in posicoes:
        pyautogui.confirm(text='posicione o mouse e após isso clique enter', title='', buttons=['OK'])
        time.sleep(1.5)
        verPos = pyautogui.position()
        print(count + 1, " - ", verPos)
        count += 1

