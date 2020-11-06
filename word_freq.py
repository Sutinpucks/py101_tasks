

"""
Программа считает Топ-100 слов для переданного ей текстого файла.

Путь до текстового файла передается программе в виде аргумента
В выводе не должно быть стоп-слов (междометий, союзов, местоимений и т.д.)
Список стоп-слов можно взять из популярного пакета nltk

Тебе может понадобится модуль os, модуль argparse, цикл и словарь
"""

if __name__ == '__main__':
    pass

import sys
import argparse 
import nltk
nltk.download('stopwords')
from nltk.corpus import stopwords
#Create an empty dictionary for words occurancies
d = dict() 
def remove_stopwords(textfile):
#function open file and exclude stopwords
    with open(file_name, "r", encoding="UTF-8") as textfile:
        filtered_text = [word for word in textfile if word not in stopwords.words('english')]

def clean_words(filtered_text)
#Remove the leading and newline character
#Convert to lowercase
#Split lines into words
for line in filtered_text:
    line = line.strip()
    line = line.lower()
    words = line.split(' ')
#check if word is in dictionary. Add count if it is in, add word with count 1 if it is new
    for word in words:
        if word in d:
            d[word] = d[word] + 1
        else:
            d[word] = 1
def top100(clean_words):
#Sort dictionary 
    sorted_dict = sorted(clean_words.items(), key=lambda x: x[1])
    n = 0 #Count
    n_items = take(100, sorted_dict.items())
    for k, v in n_items.items():
        print(key, ":", d[key]) 


 
    


