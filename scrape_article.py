



import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time



url = "https://www.theguardian.com/uk"


r1 = requests.get(url)
r1.status_code


coverpage = r1.content

soup1 = BeautifulSoup(coverpage, 'html5lib')


coverpage_news = soup1.find_all('h3', class_='fc-item__title')
len(coverpage_news)


coverpage_news[4]


number_of_articles = 5



news_contents = []
list_links = []
list_titles = []

for n in np.arange(0, number_of_articles):
        
    
    if "live" in coverpage_news[n].find('a')['href']:  
        continue
    
    
    link = coverpage_news[n].find('a')['href']
    list_links.append(link)
    
    
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)
    
    
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('div', class_='content__article-body from-content-api js-article__body')
    x = body[0].find_all('p')
    
   
    list_paragraphs = []
    for p in np.arange(0, len(x)):
        paragraph = x[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)
        
    news_contents.append(final_article)


df_features = pd.DataFrame(
     {'Article Content': news_contents 
    })


df_show_info = pd.DataFrame(
    {'Article Title': list_titles,
     'Article Link': list_links})




df_features


df_show_info




def get_news_theguardian():
    
 
    url = "https://www.theguardian.com/uk"
    
    
    r1 = requests.get(url)
    r1.status_code

    
    coverpage = r1.content

    n
    soup1 = BeautifulSoup(coverpage, 'html5lib')

   
    coverpage_news = soup1.find_all('h3', class_='fc-item__title')
    len(coverpage_news)
    
    number_of_articles = 5

    
    news_contents = []
    list_links = []
    list_titles = []

    for n in np.arange(0, number_of_articles):

        
        if "live" in coverpage_news[n].find('a')['href']:  
            continue

        link = coverpage_news[n].find('a')['href']
        list_links.append(link)

        
        title = coverpage_news[n].find('a').get_text()
        list_titles.append(title)

        
        article = requests.get(link)
        article_content = article.content
        soup_article = BeautifulSoup(article_content, 'html5lib')
        body = soup_article.find_all('div', class_='content__article-body from-content-api js-article__body')
        x = body[0].find_all('p')

        
        list_paragraphs = []
        for p in np.arange(0, len(x)):
            paragraph = x[p].get_text()
            list_paragraphs.append(paragraph)
            final_article = " ".join(list_paragraphs)

        news_contents.append(final_article)

    
    df_features = pd.DataFrame(
         {'Content': news_contents 
        })

    
    df_show_info = pd.DataFrame(
        {'Article Title': list_titles,
         'Article Link': list_links,
         'Newspaper': 'The Guardian'})

    
    return (df_features, df_show_info)






