# Spanish Poems Dataset

Dataset of Spanish poems from [ciudadseva.com](https://ciudadseva.com/biblioteca/indice-autor-poemas/)

Using BeautifulSoup, the website was scrapped.  
Three files are generated during the process:  
`ciudadseva.csv`: index of all authors in the following format:  
name, link, country, date
`poems.csv`: list of links to all poems from each author in the following format:
name, title, link
`corpus.csv`: main file with all poems from each author in the following format:  
name, title, stanza, text  

Refer to `scrape_poems.py` for further details.
