#!/usr/bin/python3

import pyautogui
import time

def clicar_olho():

    location = pyautogui.locateOnScreen('imgs/olho.png', confidence=0.9,
                                grayscale=True, region=(1500, 0, 300, 1200))
    if location:
        print('Achou olho')
        # print(location)
        pyautogui.moveTo(location.left + 10, location.top + 5)
        time.sleep(0.3)
        pyautogui.click(location.left + 10, location.top + 5)
        print('\t Clicou!')
    else:
        print('Olho nada')

def clicar_voltar():
    location = pyautogui.locateOnScreen('imgs/voltar.png', confidence=0.9,
                                grayscale=False, region=(0, 50, 100, 100))
    if location:
        print('Achou voltar')
        pyautogui.moveTo(location.left + 10, location.top + 8)
        time.sleep(0.3)
        pyautogui.click(location.left + 10, location.top + 8)
        print('\t Clicou!')
    else:
        print('Nada')

def clicar_turma():
    location = pyautogui.locateOnScreen('imgs/turma.png', confidence=0.9,
                                grayscale=False, region=(0, 50, 150, 250))
    if location:
        print('Achou turma')
        pyautogui.moveTo(location.left + 10, location.top + 8)
        time.sleep(0.3)
        pyautogui.click(location.left + 10, location.top + 8)
        print('\t Clicou!')
    else:
        print('Turma nada')

def clicar_topico():
    location = pyautogui.locateOnScreen('imgs/topicos.png', confidence=0.9,
                                grayscale=False, region=(0, 50, 150, 350))
    if location:
        print('Achou turma')
        pyautogui.moveTo(location.left + 20, location.top + 8)
        time.sleep(0.3)
        pyautogui.click(location.left + 20, location.top + 8)
        print('\t Clicou!')
    else:
        print('Topicos Nada')


if __name__ == "__main__":
    while True:
        clicar_olho()
        time.sleep(3)
        # clicar_voltar()
        clicar_turma()
        time.sleep(0.5)
        clicar_topico()
        time.sleep(3)
