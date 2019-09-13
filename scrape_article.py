
# coding: utf-8

# # Web Scraping: The Guardian

# In[1]:


import requests
from bs4 import BeautifulSoup
import numpy as np
import pandas as pd
import time


# ### Obtain list of news from the coverpage

# URL definition:

# In[2]:


# url definition
url = "https://www.theguardian.com/uk"


# List of news:

# In[3]:


# Request
r1 = requests.get(url)
r1.status_code

# We'll save in coverpage the cover page content
coverpage = r1.content

# Soup creation
soup1 = BeautifulSoup(coverpage, 'html5lib')

# News identification
coverpage_news = soup1.find_all('h3', class_='fc-item__title')
len(coverpage_news)


# Now we have a list in which every element is a news article:

# In[4]:


coverpage_news[4]


# ### Let's extract the text from the articles:

# First, we'll define the number of articles we want:

# In[5]:


number_of_articles = 5


# In[6]:


# Empty lists for content, links and titles
news_contents = []
list_links = []
list_titles = []

for n in np.arange(0, number_of_articles):
        
    # We need to ignore "live" pages since they are not articles
    if "live" in coverpage_news[n].find('a')['href']:  
        continue
    
    # Getting the link of the article
    link = coverpage_news[n].find('a')['href']
    list_links.append(link)
    
    # Getting the title
    title = coverpage_news[n].find('a').get_text()
    list_titles.append(title)
    
    # Reading the content (it is divided in paragraphs)
    article = requests.get(link)
    article_content = article.content
    soup_article = BeautifulSoup(article_content, 'html5lib')
    body = soup_article.find_all('div', class_='content__article-body from-content-api js-article__body')
    x = body[0].find_all('p')
    
    # Unifying the paragraphs
    list_paragraphs = []
    for p in np.arange(0, len(x)):
        paragraph = x[p].get_text()
        list_paragraphs.append(paragraph)
        final_article = " ".join(list_paragraphs)
        
    news_contents.append(final_article)


# Let's put them into:
# * a dataset which will the input of the models (`df_features`)
# * a dataset with the title and the link (`df_show_info`)

# In[7]:


# df_features
df_features = pd.DataFrame(
     {'Article Content': news_contents 
    })

# df_show_info
df_show_info = pd.DataFrame(
    {'Article Title': list_titles,
     'Article Link': list_links})


# In[8]:


df_features


# In[9]:


df_show_info


# ### Time Elapsed

# We are interested in how much time the script takes to get the news because this will impact directly on user experience. For this, we'll put it all into a single function and then call it:

# In[10]:


def get_news_theguardian():
    
    # url definition
    url = "https://www.theguardian.com/uk"
    
    # Request
    r1 = requests.get(url)
    r1.status_code

    # We'll save in coverpage the cover page content
    coverpage = r1.content

    # Soup creation
    soup1 = BeautifulSoup(coverpage, 'html5lib')

    # News identification
    coverpage_news = soup1.find_all('h3', class_='fc-item__title')
    len(coverpage_news)
    
    number_of_articles = 5

    # Empty lists for content, links and titles
    news_contents = []
    list_links = []
    list_titles = []

    for n in np.arange(0, number_of_articles):

        # We need to ignore "live" pages since they are not articles
        if "live" in coverpage_news[n].find('a')['href']:  
            continue

        # Getting the link of the article
        link = coverpage_news[n].find('a')['href']
        list_links.append(link)

        # Getting the title
        title = coverpage_news[n].find('a').get_text()
        list_titles.append(title)

        # Reading the content (it is divided in paragraphs)
        article = requests.get(link)
        article_content = article.content
        soup_article = BeautifulSoup(article_content, 'html5lib')
        body = soup_article.find_all('div', class_='content__article-body from-content-api js-article__body')
        x = body[0].find_all('p')

        # Unifying the paragraphs
        list_paragraphs = []
        for p in np.arange(0, len(x)):
            paragraph = x[p].get_text()
            list_paragraphs.append(paragraph)
            final_article = " ".join(list_paragraphs)

        news_contents.append(final_article)

    # df_features
    df_features = pd.DataFrame(
         {'Content': news_contents 
        })

    # df_show_info
    df_show_info = pd.DataFrame(
        {'Article Title': list_titles,
         'Article Link': list_links,
         'Newspaper': 'The Guardian'})

    
    return (df_features, df_show_info)


# In[11]:


start = time.time()
x, y = get_news_theguardian()
end =time.time()
te = end-start
print("The time elapsed is %f seconds" %(te))

