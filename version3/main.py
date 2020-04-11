import pyautogui as pag
import time
from eng_to_hin import eng2hin

# Initialize word count
word_count = 1

# Open the input file
with open('input.txt') as f:

  # Iterate through all lines in the 
  lines = list(map(str.strip, f.readlines()))

  for i in range(0, len(lines), 7):
    
    # Print output
    print(f'*{word_count}. {lines[i]}*')

    # Increment the word count
    word_count += 1

    # Convert english pronounciation to hindi
    lines[i + 1] = eng2hin(lines[i + 1])

    # These are the titles in the vocabulary card
    titles = ['Pronounciation', 'Definition', 'Self Definition',
              'Mnemonic', 'Example Sentence']

    # For all the titles print formatted output
    for j, title in enumerate(titles, start=1):
      print(f'*{title}: *{lines[i + j]}')