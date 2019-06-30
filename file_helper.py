import re

def filter_file():
    f = open('web_scrape_temp.txt', 'r')
    text = ''.join(f.readlines())
    f.close()

    text = re.sub('(.|\n)*?<div class="defv2wordtype">','<div class="defv2wordtype">', text, count=1)
    
    text = re.sub('(\n)*<div id="searchagaincontainer">(.|\n)*', '', text)
    
    f = open('web_scrape_filtered.txt', 'w')
    f.write(text)
    f.close()