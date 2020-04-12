from eng_to_hin import eng2hin
import pyperclip

# Initialize word count
word_count = input()

# Initialize empty result
result = []

# Iterate through all lines in the 
lines = list(map(str.strip, [input() for _ in range(6)]))

# Append output to result
result.append(f'*{word_count}. {lines[0]}*')

# Convert english pronounciation to hindi
lines[1] = eng2hin(lines[1])

# These are the titles in the vocabulary card
titles = ['Pronounciation', 'Definition', 'Self Definition',
          'Mnemonic', 'Example Sentence']

# For all the titles append output to result
for j, title in enumerate(titles, start=1):
  result.append(f'*{title}: *{lines[j]}')

# Copy the result to clipboard
pyperclip.copy('\n'.join(result))