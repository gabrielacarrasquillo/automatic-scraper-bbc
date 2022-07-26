#!/usr/bin/env python
# coding: utf-8

# In[2]:


get_ipython().system('pip install requests')


# In[3]:


get_ipython().system('pip install bs4')


# In[24]:


import requests
from bs4 import BeautifulSoup
import pandas as pd


# In[7]:


response = requests.get("https://www.bbc.com/")
doc = BeautifulSoup(response.text)


# In[16]:


# Grab all of the titles by inspecting the page and looking at the console to see how the title data is named in the html code.
titles = doc.select(".media__title a ")
titles


# In[28]:


rows = []

for title in titles:
    row = {}
    #title
    row ['title'] = title.text.strip()
    #link 
    row['url'] = title['href']
    
    rows.append(row)
    
df = pd.DataFrame(rows)
df.head()


# In[29]:


df.to_csv("bbc.csv", index=False)


# In[ ]:




