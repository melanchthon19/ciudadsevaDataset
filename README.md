# Spanish Poems Dataset

Dataset of Spanish Poems from [ciudadseva.com](https://ciudadseva.com/biblioteca/indice-autor-poemas/). It comprises a total of 295 authors, and 12,555 poems (more statistics below).

Using BeautifulSoup, [ciudadseva.com](https://ciudadseva.com/biblioteca/indice-autor-poemas/) was scrapped and a poem's corpus was generated.  

**Main files:**  
- `scrape_poems.py`: generates 
    - (1) index of all authors
    - (2) list of links to all poems
    - (3) a corpus directory.  
- `reformat.py`: creates (4) corpus.csv.  

**Corpus:**
Available in `corpus`directory or `corpus.csv` file.

(1) `ciudadseva.csv`: index of all authors.  

| name | link | country | date |
| --- | --- | --- | --- |
| manuel-acuna | https://ciudadseva.com/autor/manuel-acuna/poemas/ | México	| 1849-1873 |  

(2) `poems.csv`: list of links to all poems from each author.  

| name | title | link |
| --- | --- | --- |
| manuel-acuna | A Asunción | https://ciudadseva.com/texto/a-asuncion/ |  

(3) `corpus` directory containing all poems in txt format.
```
corpus
├── author1
│   ├── poem1.txt
│   ├── poem2.txt
├── author2
│   ├── poem1.txt
├── author3
│   ├── poem1.txt
│   ├── poem2.txt
│   ├── poem3.txt
```

(4) `corpus.csv`: main file with all poems from each author in the following format:  

| name | title | stanza | texto |  
| --- | --- | --- | --- |  
manuel-acuna | A Asunción | 1 | Mire usted, Asunción: aunque algún ángel
manuel-acuna | A Asunción | 1 | Metiéndose envidioso,
manuel-acuna | A Asunción | ... | ...
manuel-acuna | A Asunción | 2 | No vaya usted a rendirse
manuel-acuna | A Asunción | 2 | Ante el ruego o las lágrimas y a irse…
manuel-acuna | A Asunción | ... | ...
manuel-acuna | A Asunción | 3 | Conque mucho cuidado
manuel-acuna | A Asunción | 3 | Si siente usted un ángel a su lado,


# Dataset's Statistics

| Type | Count |
| --- | --- |
authors | 295 
poems | 12,555
verses | 419,865
tokens | 2,640,674

Given that the dataset is in Spanish, the majority of poems belong to Spanish speakers countries. There are, however, considerable translations from other languages, specially of literature's classics.  

Most of the poems come from Europe and Latin America (~5,800 poems each). Spain is the country with more poets (85), more poems (3,779), and more tokens (776,423). Within Latin America, Mexico, Puerto Rico, and Argentina account for the first three majorities.

The following plots summarizes the number of authors, poems, and tokens per region, country, and hispanic countries only.

<img src="https://user-images.githubusercontent.com/61199264/234113284-e9c4c342-de38-4b83-823d-d7081eb354a0.png" 
width=600 />
<img src="https://user-images.githubusercontent.com/61199264/234111160-13c7921f-0b15-4ef5-a69d-b88e591b9f2a.png" width=600 />
<img src="https://user-images.githubusercontent.com/61199264/234111146-4f3dae59-4b18-4dca-b785-db4139c78ad8.png" width=600 />
<img src="https://user-images.githubusercontent.com/61199264/234111157-9ca056fe-10a4-4666-a685-69cdfa8d2dbd.png" width=600 />
<img src="https://user-images.githubusercontent.com/61199264/234111163-461022da-5490-4b34-ae86-a28004df4036.png" width=600 />

# Libraries

- beautifulsoup4 == 4.12.0  
- requests == 2.28.2  
- pandas == 1.5.3  



