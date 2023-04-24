# Spanish Poems Dataset

Dataset of Spanish Poems from [ciudadseva.com](https://ciudadseva.com/biblioteca/indice-autor-poemas/)

Using BeautifulSoup, the website was scrapped and a poem's corpus was generated:  

1) `ciudadseva.csv`: index of all authors:  
| name | link | country | date |
| --- | --- | --- | --- |
| manuel-acuna | https://ciudadseva.com/autor/manuel-acuna/poemas/ | México	| 1849-1873 |  

2) `poems.csv`: list of links to all poems from each author:  
| name | title | link |
| --- | --- | --- |
| manuel-acuna | A Asunción | https://ciudadseva.com/texto/a-asuncion/ |  

3) 'corpus' directory containing all poems in txt format.
```
corpus
├── author1
│   ├── poem1.txt
│   ├── poem2.txt
├── author2
│   ├── poem1.txt
├── author295
│   ├── poem1.txt
│   ├── poem2.txt
│   ├── poem3.txt
```

4) `corpus.csv`: main file with all poems from each author in the following format:  
| name | title | stanza | texto |  
| --- | --- | --- | --- |  
manuel-acuna | A Asunción.txt | 1 | Mire usted, Asunción: aunque algún ángel
manuel-acuna | A Asunción.txt | 1 | Metiéndose envidioso,
manuel-acuna | A Asunción.txt | ... | ...
manuel-acuna | A Asunción.txt | 2 | No vaya usted a rendirse
manuel-acuna | A Asunción.txt | 2 | Ante el ruego o las lágrimas y a irse…
manuel-acuna | A Asunción.txt | ... | ...
manuel-acuna | A Asunción.txt | 3 | Conque mucho cuidado
manuel-acuna | A Asunción.txt | 3 | Si siente usted un ángel a su lado,

Refer to `scrape_poems.py` for further details.  

# Dataset's Statistics



# Libraries

- beautifulsoup4 == 4.12.0  
- requests == 2.28.2  
- pandas == 1.5.3  



