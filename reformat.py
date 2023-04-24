#!/usr/bin/env python3

import os
from os.path import join

authors = os.listdir('corpus')
#print(authors)
stats = {}

for author in authors:
    try:
        titles = os.listdir(join('corpus', author))
    except NotADirectoryError:
        continue
    stats[author] = {'titles':[], 'versos':[]}
    stats[author]['titles'] = titles

    for title in titles:
        with open(join('corpus', author, title), 'r') as file:
            versos = file.readlines()
        versos = [v.strip() for v in versos]
        versos = [v for v in versos]
        stats[author]['versos'].append(versos)

# header
with open('corpus.csv', 'w') as file:
    file.write('author\ttitle\tstanza\tverso\n')

for author in stats.keys():
    for i in range(len(stats[author]['versos'])):
        stanza = 0
        for verso in stats[author]['versos'][i]:
            if not verso:
                stanza += 1
                continue
            # author, titlepoem, stanza, verso
            print(author, stats[author]['titles'][i], stanza+1, verso)
            with open('corpusreformat.csv', 'a') as file:
                file.write(f'{author}\t{stats[author]["titles"][i]}\t{stanza+1}\t{verso}\n')


