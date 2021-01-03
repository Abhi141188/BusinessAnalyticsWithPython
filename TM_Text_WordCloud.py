# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:11:20 2020

@author: Abhinav
"""

#Import the following python libraries.
from wordcloud import WordCloud, STOPWORDS
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

#Add the text that you want to use for your word cloud. I used details about Actor: SSR.
Wds = 'In June 2009, Rajput began starring in Pavitra Rishta as Manav Deshmukh, a serious and mature character working as a mechanic to support his family. His work in this serial received wide appreciation, and Rajput received three major television awards for best male actor and most popular actor.He was also famous for his relationship with Ankita Lokhande. Rajput auditioned for Abhishek Kapoor movie: Kai Po Che! and was selected to play one of the three leads, along with Rajkumar Rao and Amit Sadh. Based on the Chetan Bhagat novel The 3 Mistakes of My Life, the film proved to be a critical and commercial success.Rajput was in a publicised relationship with his Pavitra Rishta co-star Ankita Lokhande for six years. They broke up in 2016. Lately, he was suffering from depression. People say he felt prey to Nepotism. And many consider the reason of his death as Nepotism only.' 

#To get the custom shape for the word cloud, look for an image that you want to use as a mask.
#I used the following image as an outline "yellow-house-hi.png"
Msk = np.array(Image.open('F:/pyWork/pyData/yellow-house-hi.png'))

Stpwrds = STOPWORDS
Stpwrds

#This function takes in your text and your mask to generate a custom wordcloud.
def generate_wordcloud(words, mask):
    word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=Stpwrds, mask=mask).generate(words)
    plt.figure(figsize=(10,8),facecolor = 'white', edgecolor='blue')
    plt.imshow(word_cloud)
    plt.axis('off')
    plt.tight_layout(pad=0)
    plt.show()
    
#Run the following line of code to call the generate_wordcloud function above.
generate_wordcloud(Wds, Msk)

#To save this wordcloud in a separate PNG file:
word_cloud = WordCloud(width = 512, height = 512, background_color='white', stopwords=STOPWORDS).generate(Wds)
plt.imshow(word_cloud)
wc = word_cloud
wc.to_file("F:/pyWork/pyData/WC_3Jan.png")