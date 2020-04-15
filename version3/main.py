from eng_to_hin import eng2hin
import pyperclip

# Initialize empty result
result = []

# Take all inputs
print('Enter your inputs:')
lines = list(map(str.strip, [input() for _ in range(7)]))

# Append output to result
result.append(f'*{lines[0]}. {lines[1]}*')

# Convert english pronounciation and self defintion to hindi
lines[2] = eng2hin(lines[2])
lines[4] = eng2hin(lines[4])

# These are the titles in the vocabulary card
titles = ['Pronounciation', 'Definition', 'Self Definition',
          'Mnemonic', 'Example Sentence']

# For all the titles append output to result
for j, title in enumerate(titles, start=2):
  result.append(f'*{title}:*\n{lines[j]}')

# Copy the result to clipboard
pyperclip.copy('\n\n'.join(result))