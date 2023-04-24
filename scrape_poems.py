#!/usr/bin/env python3

import os
from os.path import isdir, isfile, join
import sys
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

def scrape_poems(poems, log):
    if not isdir('corpus'): os.mkdir('corpus')

    df = pd.read_csv(poems)
    print(df.head())

    for i in df.index:   
        folder = join('corpus', df.loc[i, 'name'])
        if not isdir(folder): os.mkdir(folder)

        title = re.sub(r'[^ a-záéíóúüñA-Z0-9]', '', df.loc[i, 'title'])
        output = join(folder, title + '.txt')
        if isfile(output): continue
        
        print(i, output)

        try: 
            site = requests.get(df.loc[i, 'link'])
            soup = BeautifulSoup(site.text, 'html.parser')
            poem = soup.find('table', class_='table-center')
            stanzas = poem.find_all('p')
            
            for stanza in stanzas:
                stanza = re.sub('\xa0', '', str(stanza))
                stanza = re.split(r'<.*?>', stanza)
                stanza = [t.strip() for t in stanza if t]
                stanza = '\n'.join([st for st in stanza])

                with open(output, 'a') as file:
                    file.write(f'{stanza}\n\n')
        
        except Exception as e:
            with open(log, 'a') as file:
                file.write(f'Error with {df.iloc[i]}\n{e}\n\n')
            print(f'Error with {df.iloc[i]}\n{e}\n\n')
        
        time.sleep(2)
        #if i == 5: break

def scrape_html(author, title, link):
    if not isdir('corpus'): os.mkdir('corpus')

    folder = join('corpus', author)
    if not isdir(folder): os.mkdir(folder)

    title = re.sub(r'[^ a-záéíóúüñA-Z0-9]', '', title)
    output = join(folder, title + '.txt')
    print(output)

    # change code here to adjust for specific websites
    site = requests.get(link)
    soup = BeautifulSoup(site.text, 'html.parser')
    poem = soup.find('table', class_='table-center')
    stanzas = poem.find_all('td')
    
    for stanza in stanzas:
        stanza = re.sub('\xa0', '', str(stanza))
        stanza = re.split(r'<.*?>', stanza)
        stanza = [t.strip() for t in stanza if t]
        stanza = '\n'.join([st for st in stanza])
        stanza = re.sub(r'\n\[L\d+\]', '', stanza)
        #print(stanza)
        with open(output, 'a') as file:
            file.write(f'{stanza}\n\n')


if __name__ == '__main__':
    """
    scrape_ciudadseva_index() scrapes ciudad seva's index and outputs a csv file ('ciudadseva.csv')
    format: name, link, country, date
    """
    #scrape_ciudadseva_index('ciudadseva.csv')
    
    """
    scrape_author_index() scrapes links to poems from each author and outputs a csv file ('poems.csv')
    format: name, title, link
    """
    #scrape_author_index('ciudadseva.csv', 'poems.csv')

    """
    scrape_poems() scrapes each poem from each author.
    corpus folder is created: corpus --> author --> poems in txt files.
    any errors are logged to 'log.txt'
    """
    #scrape_poems('poems.csv', 'log2.txt')

    """
    scrape_html() scrapes a given link and adds poems to corpus folder.
    function should be called from command line passing author title link
    """
    #scrape_html(sys.argv[1], sys.argv[2], sys.argv[3])

