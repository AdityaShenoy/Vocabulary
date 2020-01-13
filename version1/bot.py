import pyautogui as pag
import time

MEAN_URL = 'www.wordhippo.com/what-is/the-meaning-of-the-word/'
PLURAL_URL = 'www.wordhippo.com/what-is/the-plural-of/'
SINGULAR_URL = 'www.wordhippo.com/what-is/the-singular-of/'
PAST_URL = 'www.wordhippo.com/what-is/the-past-tense-of/'

def word_pronouncation(word):
    pag.hotkey('alt', 'tab')
    pag.hotkey('ctrl', 'l')
    pag.typewrite(MEAN_URL + word + '.html\n')
    time.sleep(10)
    pag.click(1214, 386)
    time.sleep(10)
    pag.hotkey('alt', 'tab')
    time.sleep(1)
    pag.click(x=1800, y=500)
    pron = input('Enter pronouncation: ')
    return pron

def word_part_of_speech(word):
    pag.hotkey('alt', 'tab')
    time.sleep(5)
    pag.hotkey('alt', 'tab')
    time.sleep(1)
    pag.click(x=1800, y=500)
    pos = input('Enter parts of speech: ')
    res = {}

    if pos == 'n':
        res['pos'] = 'noun'
        pag.hotkey('alt', 'tab')
        pag.hotkey('ctrl', 't')
        pag.hotkey('ctrl', 'l')
        pag.typewrite(PLURAL_URL + word + '.html\n')
        time.sleep(10)
        pag.hotkey('alt', 'tab')
        time.sleep(1)
        pag.click(x=1800, y=500)
        plural = input('Enter plural noun of the word: ')
        if plural == '.':
            plural = word
        res['plural'] = plural
        
        pag.hotkey('alt', 'tab')
        pag.hotkey('ctrl', 'l')
        pag.typewrite(SINGULAR_URL + word + '.html\n')
        time.sleep(10)
        pag.hotkey('alt', 'tab')
        time.sleep(1)
        pag.click(x=1800, y=500)
        singular = input('Enter singular noun of the word: ')
        if singular == '.':
            singular = word
        pag.hotkey('alt', 'tab')
        pag.hotkey('ctrl', 'w')
        pag.hotkey('alt', 'tab')
        res['singular'] = singular
    
    elif pos == 'v':
        res['pos'] = 'verb'
        pag.hotkey('alt', 'tab')
        pag.hotkey('ctrl', 't')
        pag.hotkey('ctrl', 'l')
        pag.typewrite(PAST_URL + word + '.html\n')
        time.sleep(10)
        pag.hotkey('alt', 'tab')
        time.sleep(1)
        pag.click(x=1800, y=500)

def find_word(word):
    pag.PAUSE = 1

    pron = word_pronouncation(word)
    pos = word_part_of_speech(word)