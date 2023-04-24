library(dplyr)
library(ggplot2)
library(maps)
library(countrycode)

df <- read.csv('melanchthon19/spanishPoemsDataset/corpus.csv', sep='\t', quote="")
cat('total number of authors:', length(unique(df$author)))
cat('total number of titles:', length(unique(df$title)))
cat('total number of versos:', nrow(df))

df$ntokens <- sapply(df$verso, function(x) lengths(strsplit(x, " ")))
dft <- df %>% group_by(author) %>% summarize(ntokens = sum(ntokens))
dft <- merge(dft,
             df %>% group_by(author) %>% summarize(ntitles = length(unique(title))),
             by='author')

dfc <- read.csv('melanchthon19/spanishPoemsDataset/ciudadseva.csv', sep=',')
dfc <- subset(dfc, select = -c(link))
colnames(dfc) = c('author', 'country', 'date')

table(dfc$country)
dft <- merge(dft, dfc, by='author', all.x=TRUE)
custom_dict <- data.frame(spanish = countrycode::codelist$cldr.name.es,
                          english = countrycode::codelist$cldr.name.en,
                          stringsAsFactors = FALSE)
custom_dict = rbind(custom_dict,
                    data.frame(
                      spanish=c('Arabia', 'Argentino', 'Austríaco', 'Boliviano', 'Español', 'Español/Mexicano', 'Francés', 'Gales', 'Grecia antigua', 'Griego', 'Inglaterra', 'Italiano', 'Palestina'), 
                      english=c('Saudi Arabia', 'Argentina', 'Austria', 'Bolivia', 'Spain', 'Spain', 'France', 'United Kingdom', 'Greece', 'Greece', 'United Kingdom', 'Italy', 'Palestine')
                    )
              )
dft$country <- countrycode(dft$country, "spanish", "english", custom_dict = custom_dict)
table(dft$country)

dft$region <- countrycode(dft$country, "country.name", "region")
table(dft$region)

dfc <- merge(dft %>% group_by(country) %>% summarize(ntokens = sum(ntokens, na.rm=TRUE)),
             dft %>% group_by(country) %>% summarize(ntitles = sum(ntitles, na.rm=TRUE)),
             )
dfc <- merge(dfc, dft %>% group_by(country) %>% summarize(nauthors = n()))

hispanos <- c('Spain', 'Mexico', 'Colombia', 'Argentina', 'Peru', 'Venezuela', 'Chile', 'Guatemala', 'Ecuador', 'Bolivia', 'Cuba', 'Dominican Republic', 'Honduras', 'Paraguay', 'El Salvador', 'Nicagarua', 'Costa Rica', 'Panama', 'Uruguay', 'Equatorial Guinea', 'Puerto Rico')
dfh <- dfc[dfc$country %in% hispanos, ]

# tokens per countries/hispanic
dfh <- arrange(dfh, desc(ntokens))
dfc <- arrange(dfc, desc(ntokens))
dfc$country <- factor(dfc$country, levels = dfc$country)
dfh$country <- factor(dfh$country, levels = dfh$country)
ggplot(dfc[1:10, ], aes(x = country, y = ntokens)) +
  geom_bar(stat = "identity", fill = "blue") +
  xlab("Country") +
  ylab("Number of tokens") +
  ggtitle("Count of tokens per country") + 
  theme(axis.text.x = element_text(angle = 45, hjust=1))

ggplot(dfh[1:10, ], aes(x = country, y = ntokens)) +
  geom_bar(stat = "identity", fill = "blue") +
  xlab("Country") +
  ylab("Number of tokens") +
  ggtitle("Count of tokens per hispanic country") + 
  theme(axis.text.x = element_text(angle = 45, hjust=1))

# titles per countries/hispanic
dfh <- arrange(dfh, desc(ntitles))
dfc <- arrange(dfc, desc(ntitles))
dfc$country <- factor(dfc$country, levels = dfc$country)
dfh$country <- factor(dfh$country, levels = dfh$country)
ggplot(dfc[1:10, ], aes(x = country, y = ntitles)) +
  geom_bar(stat = "identity", fill = "blue") +
  xlab("Country") +
  ylab("Number of poems") +
  ggtitle("Count of poems per country") + 
  theme(axis.text.x = element_text(angle = 45, hjust=1))

ggplot(dfh[1:10, ], aes(x = country, y = ntitles)) +
  geom_bar(stat = "identity", fill = "blue") +
  xlab("Country") +
  ylab("Number of poems") +
  ggtitle("Count of poems per hispanic country") + 
  theme(axis.text.x = element_text(angle = 45, hjust=1))

# authors per countries/hispanic
dfh <- arrange(dfh, desc(nauthors))
dfc <- arrange(dfc, desc(nauthors))
dfc$country <- factor(dfc$country, levels = dfc$country)
dfh$country <- factor(dfh$country, levels = dfh$country)
ggplot(dfc[1:10, ], aes(x = country, y = nauthors)) +
  geom_bar(stat = "identity", fill = "blue") +
  xlab("Country") +
  ylab("Number of authors") +
  ggtitle("Count of authors per country") + 
  theme(axis.text.x = element_text(angle = 45, hjust=1))

ggplot(dfh[1:10, ], aes(x = country, y = nauthors)) +
  geom_bar(stat = "identity", fill = "blue") +
  xlab("Country") +
  ylab("Number of authors") +
  ggtitle("Count of authors per hispanic country") + 
  theme(axis.text.x = element_text(angle = 45, hjust=1))

dfr <- merge(dft %>% group_by(region) %>% summarize(ntokens = sum(ntokens)),
             dft %>% group_by(region) %>% summarize(ntitles = sum(ntitles)),
             )
dfr <- merge(dfr, dft %>% group_by(region) %>% summarize(nauthors = n()))

# tokens and titles per region
options(scipen=999)
dfr <- arrange(dfr, desc(ntokens))
dfr$region <- factor(dfr$region, levels = dfr$region)
ggplot(na.omit(dfr), aes(x = region, y = ntokens)) +
  geom_bar(stat = "identity", fill = "blue") +
  xlab("Region") +
  ylab("Number of tokens") +
  ggtitle("Count of tokens per region") +
  theme(axis.text.x = element_text(angle = 45, hjust=1))

dfr <- arrange(dfr, desc(ntitles))
dfr$region <- factor(dfr$region, levels = dfr$region)
ggplot(na.omit(dfr), aes(x = region, y = ntitles)) +
  geom_bar(stat = "identity", fill = "blue") +
  xlab("Region") +
  ylab("Number of poems") +
  ggtitle("Count of poems per region") +
  theme(axis.text.x = element_text(angle = 45, hjust=1))

dfr <- arrange(dfr, desc(nauthors))
dfr$region <- factor(dfr$region, levels = dfr$region)
ggplot(na.omit(dfr), aes(x = region, y = nauthors)) +
  geom_bar(stat = "identity", fill = "blue") +
  xlab("Region") +
  ylab("Number of authors") +
  ggtitle("Count of authors per region") +
  theme(axis.text.x = element_text(angle = 45, hjust=1))
