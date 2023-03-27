# Spanish Poems Dataset

Dataset of Spanish Poems from [ciudadseva.com](https://ciudadseva.com/biblioteca/indice-autor-poemas/)

Using BeautifulSoup, the website was scrapped.  
Three files are generated during the process:  

`ciudadseva.csv`: index of all authors:  
| name | link | country | date |
| --- | --- | --- | --- |
| manuel-acuna | https://ciudadseva.com/autor/manuel-acuna/poemas/ | México	1849-1873 |  

`poems.csv`: list of links to all poems from each author:  
| name | title | link |
| --- | --- | --- |
| manuel-acuna | A Asunción | https://ciudadseva.com/texto/a-asuncion/ |  

`corpus.csv`: main file with all poems from each author:  
| name | title | stanza | texto |  
| --- | --- | --- | --- |  
manuel-acuna | A Asunción | 1 | 'Mire usted, Asunción: aunque algún ángel\nMetiéndose envidioso,\nConciba allá en el cielo el mal capricho\nDe venir por la noche a hacerle el oso\nY en un acto glorioso\nLlevársela de aquí, como le ha dicho\nNo sé qué nigromante misterioso,\nNo vaya usted, por Dios, a hacerle caso,\nNi a dar con el tal ángel un mal paso;\nEstese usted dormida,\nDebajo de las sábanas metida,\nY deje usted que la hable\nY que la vuelva a hablar y que se endiable,\nQue entonces con un dedo\nPuesto sobre otro en cruz, ¡afuera miedo!' |  

Refer to `scrape_poems.py` for further details.  

# Dataset's Statistics


