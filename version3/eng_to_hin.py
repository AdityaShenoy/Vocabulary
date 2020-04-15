vowels = {
  'a': chr(0x0905),
  'aa': chr(0x0906),
  'i': chr(0x0907),
  'ii': chr(0x0908),
  'u': chr(0x0909),
  'uu': chr(0x090A),
  'ae': chr(0x090D),
  'e': chr(0x090F),
  'ai': chr(0x0910),
  'aw': chr(0x0911),
  'o': chr(0x0913),
  'au': chr(0x0914),
}

consonants = {
  'k': chr(0x0915),
  'kh': chr(0x0916),
  'g': chr(0x0917),
  'gh': chr(0x0918),
  'ch': chr(0x091A),
  'chh': chr(0x091B),
  'j': chr(0x091C),
  'jh': chr(0x091D),
  't.': chr(0x091F),
  'th.': chr(0x0920),
  'd.': chr(0x0921),
  'dh.': chr(0x0922),
  'n.': chr(0x0923),
  't': chr(0x0924),
  'th': chr(0x0925),
  'd': chr(0x0926),
  'dh': chr(0x0927),
  'n': chr(0x0928),
  'p': chr(0x092A),
  'f': chr(0x092B),
  'b': chr(0x092C),
  'bh': chr(0x092D),
  'm': chr(0x092E),
  'y': chr(0x092F),
  'r': chr(0x0930),
  'l': chr(0x0932),
  'l.': chr(0x0933),
  'v': chr(0x0935),
  'sh': chr(0x0936),
  's': chr(0x0938),
  'h': chr(0x0939),
  'z': chr(0x095B),
  'zh': chr(0x091D)+chr(0x093C),
}

vowels_for_consonants = {
  'aa': chr(0x093E),
  'i': chr(0x093F),
  'ii': chr(0x0940),
  'u': chr(0x0941),
  'uu': chr(0x0942),
  'ae': chr(0x0945),
  'e': chr(0x0947),
  'ai': chr(0x0948),
  'aw': chr(0x0949),
  'o': chr(0x094B),
  'au': chr(0x094C),
}

# Put all vowels in final mapping
all_letters = {k: v for k, v in vowels.items()}

# For all consonants
for ck, cv in consonants.items():

  # ka, kha, ...
  all_letters[ck + 'a'] = cv

  # Half letters
  all_letters[ck] = cv + chr(0x094D)

  # For all half vowels
  for vk, vv in vowels_for_consonants.items():

    # kaa, ki, kii, ...
    all_letters[ck + vk] = cv + vv

# Write all the mappings to output file for future reference
with open('eng_to_hin_map.txt', 'w', encoding='utf8') as f:
  for k, v in all_letters.items():
    f.write(f'{k}: {v}\n')

# Sort the keys in reverse length order to avoid common prefix issues
# Eg. chhaa can be coded to chh + aa or chhaa if we do not do this
keys = list(all_letters.keys())
keys.sort(key=len, reverse=True)

# Store the above keys' values in the same order
values = [all_letters[k] for k in keys]

# Zip all the mappings to a list
e2h = list(zip(keys, values))

# This function converts text from english to hindi using e2h mapping
def eng2hin(text: str):

  # Initialize empty result
  result = []

  # Current start index
  i = 0

  # While there are letters to be scanned in the text
  while i < len(text):

    # Greedy current end index
    for j in range(len(text), i, -1):

      # If the current sub string is in all_letters
      if text[i:j] in all_letters:

        # Append the hindi translation
        result.append(all_letters[text[i:j]])

        # Move the start index forwards
        i += j-i

        break
    
    # If there is no match
    else:

      # Append the letter as it is and increment the start index
      result.append(text[i])
      i += 1

  # Return result
  return ''.join(result)

# Testing section
inp = 'aaditya'
with open('test.txt', 'w', encoding='utf8') as f:
  f.write(eng2hin(inp))