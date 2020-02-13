from bs4 import BeautifulSoup
from urllib.request import urlopen
from re import sub

# This is the word whose data will be crawled and scraped from the web
word = input('Enter a word: ')


# =======================================================================================
# DATA CRAWLING

# These are the URLs to crawl
urls = {
  'meaning': 'https://www.wordhippo.com/what-is/the-meaning-of-the-word/{}.html',
  'sentence': 'https://www.wordhippo.com/what-is/sentences-with-the-word/{}.html',
}

# Initialize empty html_data dictionary
html_data = {}

# For all key value pairs in urls dictionary
for k, v in urls.items():

  # Showing progress of the web crawling to user
  print(f'Loading data for the {k} of the word "{word}"...')

  # Open the URL with the word placed in the curly braces
  fp = urlopen(v.format(word))

  # Read the bytes of the html data and decode it to string using utf8
  data = fp.read().decode('utf8')

  # Close the connection
  fp.close()

  # Store the string html data in the dictionary
  html_data[k] = data

# Showing progress of the web crawling to user
print(f'\nAll data for the word "{word}" loaded successfully...')


# =======================================================================================
# DATA SCRAPING


# Scrapes data for the meaning of the word
def scrape_meaning():

  # Create a soup object
  soup = BeautifulSoup(html_data['meaning'], features='html.parser')

  # The parts of the speech of the word is located in div.defv2wordtype
  all_pos = soup.find_all('div', class_='defv2wordtype')

  # The meanings are stored in ol.topleveldefinition
  all_meanings = soup.find_all('ol', class_='topleveldefinition')

  # Print output
  print(f'\n\nWord: {word}')

  # Read all pos and meaning alternatively
  for pos, meaning_list in zip(all_pos, all_meanings):

    # Print output
    print(f'\nPart of speech: {pos.string}\n\nMeanings:')

    # For all meanings in the meaning list
    for meaning in meaning_list:

      # Extract inner HTML of the meaning
      innerHTML = str(meaning)

      # Remove newlines from text
      innerHTML = innerHTML.replace('\n', '')

      # If the innerHTML is not empty
      if innerHTML:

        # Remove all tags from the innerHTML
        innerHTML = sub('<.*?>', '', innerHTML)

        # Print output
        print(f'\t• {innerHTML}')


# Scrapes data for the sentences of the word
def scrape_sentence():

  # Create a soup object
  soup = BeautifulSoup(html_data['sentence'], features='html.parser')

  # The sentences are printed in td tags of table having id mainsentencestable
  all_sentences = soup.select('#mainsentencestable td[id^=exv2]')

  # Print output
  print(f'\nSentences:')

  # For all sentences max 10
  for sentence in all_sentences[:10]:

    # Extract the innerHTML of the sentence
    innerHTML = str(sentence)

    # Remove all tags in the innerHTML
    innerHTML = sub('<.*?>', '', innerHTML)

    # Print output
    print(f'\t• {innerHTML}')


scrape_meaning()
scrape_sentence()