# -*- coding: utf-8 -*-
"""
Created on Wed Apr 29 17:15:01 2020

@author: Abhinav
"""
#Project-1
from textblob import TextBlob

Feedback1 = 'Starbucks Coffee is awesome.'
Feedback2 = 'Starbucks Coffee was worst.'
Feedback3 = 'Starbucks Coffee was Ok.'
Feedback4 = 'Starbucks loves customers.'
Feedback5 = 'Starbucks Coffee is fine.'

b1 = TextBlob(Feedback1)
b2 = TextBlob(Feedback2)
b3 = TextBlob(Feedback3)
b4 = TextBlob(Feedback4)
b5 = TextBlob(Feedback5)

print(b1.sentiment)
print(b2.sentiment)
print(b3.sentiment)
print(b4.sentiment)
print(b5.sentiment)

#Note:
#Polarity: It simply means emotions expressed in a sentence.
#Emotions are closely related to sentiments. They can be positive, negative or neural.

#Subjectivity: Subjective sentence expresses some personal feelings, views, or beliefs.
#A subjective sentence may not express any sentiment. For example, “I think that he went home” 
#and “I want a camera that can take good photos” are a subjective sentences, but does not express any sentiment.  

#Project-2
#Import Library
import pandas as pd

#Load data
dataset = pd.read_csv('F:/WORK/pyWork/Text_Mining/PresidentSpeechs/Bush.txt')
#Converting data into string format
dataset = dataset.to_string(index = False) 
type(dataset)

b1 =TextBlob(dataset)
print(b1.sentiment)

#-------------------Cleaning the data-----------------------------------
import re
dataset = re.sub("[^A-Za-z0-9]+"," ",dataset)
#sub is used to substitute......here we substitute all element in bracket with space.
# ^ is used for negation so it means accept these all ranges convert it to space. 
# + signify that atleast one should be converted.

#----------------------Tokenization--------------------------------------------
import nltk
#nltk.download()
    
from nltk.tokenize import word_tokenize
Tokens = word_tokenize(dataset)
print (Tokens)

#No. of tokens in the dataset
len(Tokens)

#Freq of occurence of distinct elements
from nltk.probability import FreqDist
fdist = FreqDist()

for word in Tokens:
    fdist[word] += 1
fdist
fdist.plot(20)

#-------------------------Stemming----------------------------------------
from nltk.stem import PorterStemmer
pst=PorterStemmer()
pst.stem("having")


#-------------Remove the Stop Words---------------------
import nltk.corpus

#Enlisting the stopwords present in English lang
stopwords = nltk.corpus.stopwords.words('english')
stopwords[0:10]

#Getting rid of stopwords
#filtered_sentence = [FinalWord for FinalWord in Tokens if FinalWord not in stopwords]
filtered_sentence = []   
for FinalWord in Tokens:
    if FinalWord not in stopwords:
        filtered_sentence.append(FinalWord)  

print(filtered_sentence)  
len(filtered_sentence)
len(Tokens)

#Classification of words as Positive, Negative & Neutral

#Calculating final Sentiment Score
b2 =TextBlob(filtered_sentence)
#We need to convert "filtered sentence" list into string for applying: Textblob fxn.
# Python program to convert a list 
# to string using list comprehension using list comprehension 
filtered_sentence = ' '.join([str(elem) for elem in filtered_sentence]) 
print(filtered_sentence)

b2 =TextBlob(filtered_sentence)
print(b2.sentiment)

from wordcloud import WordCloud
word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=stopwords).generate(filtered_sentence)
import matplotlib.pyplot as plt
plt.imshow(word_cloud)

