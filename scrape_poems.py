#!/usr/bin/env python3

import os
import re
import time
import pandas as pd
import requests
from bs4 import BeautifulSoup


def scrape_ciudadseva_index(output):
    if os.path.exists(output): raise NameError(f'file {output} already exists.')

    site = requests.get('https://ciudadseva.com/biblioteca/indice-autor-poemas/')
    soup = BeautifulSoup(site.text, 'html.parser')
    #print(soup)
    indice = soup.find('div', class_='row xs-center')
    authors = indice.find_all('div', class_='col-sm-6')
    ciudadseva = {}
    for author in authors:
        try:
            link = author.find('a', href=True)['href']
            name = re.match(r'https://ciudadseva.com/autor/(.*?)/poemas/', link).group(1)
            details = author.find('span', class_='text-smaller')
            details = details.text.strip().split(': ')
            country = details[0]
            date = details[1]
            #print(name, country, date, link)
            ciudadseva[name] = [name, link, country, date]
            
        except Exception as e:
            print(f'Error with {author}\n{e}\n\n')

    df = pd.DataFrame.from_dict(ciudadseva, orient='index', columns=['name', 'link', 'country', 'date'])
    df = df.reset_index()
    df = df.drop(['index'], axis=1)
    df.to_csv(output, index=False)

def scrape_author_index(index, output):
    if os.path.exists(output): raise NameError(f'file {output} already exists.')

    df = pd.read_csv(index)
    print(df.head())
    authors = []
    for i in df.index:
        print(i)
        try:
            site = requests.get(df.loc[i, 'link'])
            soup = BeautifulSoup(site.text, 'html.parser')
            poems = soup.find_all('li', class_='text-center')
            for poem in poems:
                link = poem.find('a', href=True)['href']
                title = poem.text.strip()
                #print(link)
                #print(title)
                authors.append([df.loc[i, 'name'], title, link])
        except Exception as e:
            print(f'Error with {df.loc[i, "link"]}\n{e}\n\n')
        time.sleep(2)

    df = pd.DataFrame(authors, columns=['name', 'title', 'link'])
    df = df.reset_index()
    df = df.drop(['index'], axis=1)
    df.to_csv(output, index=False)

def scrape_poems(poems, output):
    df = pd.read_csv(poems)
    print(df.head())

    for i in df.index:
        print(i)
        try: 
            site = requests.get(df.loc[i, 'link'])
            soup = BeautifulSoup(site.text, 'html.parser')
            poem = soup.find('table', class_='table-center')
            stanzas = poem.find_all('p')
            
            for j, stanza in enumerate(stanzas):
                with open(output, 'a') as file:
                    file.write(f'{df.loc[i, "name"]},{df.loc[i, "title"]},{j+1},{repr(stanza.text)}\n')

        except Exception as e:
            with open('log.txt', 'a') as file:
                file.write(f'Error with {df.iloc[i]}\n{e}\n\n')
            print(f'Error with {df.iloc[i]}\n{e}\n\n')
        time.sleep(2)
    

if __name__ == '__main__':
    """
    it scrapes ciudad seva's index and outputs a csv file ('ciudadseva.csv')
    format: name, link, country, date
    """
    #scrape_ciudadseva_index('ciudadseva.csv')
    
    """
    it scrapes links to poems from each author and outputs a csv file ('poems.csv')
    format: name, title, link
    """
    #scrape_author_index('ciudadseva.csv', 'poems.csv')

    """
    it scrapes each poem from each author and outputs a csv file ('corpus.csv')
    format: name, title, stanza, text
    any errors are logged to 'log.txt'
    """
    #scrape_poems('poems.csv', 'corpus.csv')
