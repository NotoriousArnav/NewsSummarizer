from nltk.corpus import stopwords
from bs4 import BeautifulSoup
import feedparser
import requests
import heapq
import nltk
import json
import re

def article_extracter(link):
    try:
        data = requests.get(link)
        soup = BeautifulSoup(data.content, 'lxml')
    except:
        return 
    title = soup.find('title').text
    article = soup.find_all('article')[0].text
    return title, article

def get_feed(link):
    try:
        feed = feedparser.parse(link)
    except:
        return None
    return [x.link for x in feed.entries]

def summarize(article):
    sentence_list = nltk.sent_tokenize(article.replace("\n",''))
    stopwrds = stopwords.words("english")
    word_frequencies = {}
    for word in nltk.word_tokenize(article):
        if word not in stopwrds:
            if word not in word_frequencies.keys():
                word_frequencies[word] = 1
            else:
                word_frequencies[word] += 1

    maximum_frequncy = max(word_frequencies.values())

    for word in word_frequencies.keys():
        word_frequencies[word] = (word_frequencies[word]/maximum_frequncy)

    sentence_scores = {}
    for sent in sentence_list:
        for word in nltk.word_tokenize(sent.lower()):
            if word in word_frequencies.keys():
                if len(sent.split(' ')) < 30:
                    if sent not in sentence_scores.keys():
                        sentence_scores[sent] = word_frequencies[word]
                    else:
                        sentence_scores[sent] += word_frequencies[word]

    summary_sentences = heapq.nlargest(7, sentence_scores, key=sentence_scores.get)

    summary = ' '.join(summary_sentences)
    return str(summary)
