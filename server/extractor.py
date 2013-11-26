import sys
import dateutil.parser as dparser
import nltk
from urllib import urlopen
import timex
import re
import json
from bs4 import BeautifulSoup

START = 000
END = 2100

def get_sentence_dates(url):

    # Extract sentences from the html
    response = urlopen(url)
    content = response.read()

    # Get only relevant text
    soup = BeautifulSoup(content)
    split = [elm.text.encode("utf-8") for elm in soup.findAll('p')]
    content = ' '.join(split)
    raw = nltk.clean_html(content)

    # Strip raw
    raw = re.sub(r'(\n)|\[.*?\] ?', "", raw)
    #raw = re.sub(r'(\n)|\(.*?\) ?', "", raw)
    raw = re.sub(r"\r\n", ".", raw)
    #raw = re.sub(r";", ".", raw)
    #raw = re.sub(r"\"", ".", raw)    
    
    sent_detector = nltk.data.load('tokenizers/punkt/english.pickle')
    sentences = sent_detector.tokenize(raw.strip())

    more_sentences = []
    for sentence in sentences:
        sentence = sentence.strip().split(".")
        more_sentences += sentence

    sentences = more_sentences

    #Clean sentences
    for index, sentence in enumerate(sentences):
        split_up = sentence.split()
        sentences[index] = ' '.join(split_up)

    sentence_date_maps = {}

    # Assign a date to each sentence
    for index, sentence in enumerate(sentences):    
        timed_sentence = timex.tag(str(sentence))
        for result in re.finditer(".*<TIMEX2>(.*)</TIMEX2>.*", timed_sentence):
            for r in result.groups():
                if r not in sentence_date_maps:
                    sentence_date_maps[r] = []
                sentence_date_maps[r].append(sentence)

    sentence_dates = []
    for date, sentences in sentence_date_maps.items():
        try:
            year = int(date)
            if year > START and year < END:
                #for sentence in sentences:
                #    res = []
                #    print(sentence)
                #    if len(sentence) > 10 and  len(sentence) < 500:
                #        res.append(sentence)
                #if res != []:
                #    sentence_dates.append((year, res))
                sentence_dates.append((year, sentences))
                        
        except:
            continue

    sentence_dates = sorted(sentence_dates, key=lambda x:x[0])

    return json.dumps(sentence_dates)
