import pyautogui as pag
import time

def find_word(word):
    url = "www.wordhippo.com/what-is/the-meaning-of-the-word/"

    pag.PAUSE = 1

    pag.hotkey('alt', 'tab')
    pag.hotkey('ctrl', 'l')
    pag.typewrite(url + word + '.html')
    pag.press('enter')
    time.sleep(5)
    pag.hotkey('ctrl', 'u')
    pag.hotkey('ctrl', 'a')
    pag.hotkey('ctrl', 'c')
    pag.hotkey('ctrl', 'w')
    pag.hotkey('alt', 'tab')
    pag.hotkey('ctrl', 'tab')
    pag.hotkey('ctrl', 'a')
    pag.hotkey('ctrl', 'v')
    pag.hotkey('ctrl', 's')
    pag.hotkey('ctrl', 'tab')