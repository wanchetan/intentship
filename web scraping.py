#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install requests')
get_ipython().system('pip install bs4')


# In[2]:


from bs4 import BeautifulSoup
import requests
import pandas as pd 


# In[3]:


#QUSTION 1)

page = requests.get('https://en.wikipedia.org/wiki/Main_Page')
page
soup = BeautifulSoup(page.content)
soup
header = []
for i in soup.find_all('span',class_="mw-headline"):
    header.append(i.text)
df= pd.DataFrame(header,columns=['Header'])
df


# In[4]:


#QUSTION 3)

LINK = requests.get('https://www.icc-cricket.com/rankings')
LINK
soup = BeautifulSoup(LINK.content)
matches = []
for i in soup.find_all("div",class_="si-table-data si-matches"):
    matches.append(i.text)
df = pd.DataFrame(matches)
df


# In[5]:


#QUSTION 5)

link = requests.get('https://www.cnbc.com/world/?region=world')
link
soup = BeautifulSoup(link.content)
Headline = []
Time=[]
News_Link =[]
for i in soup.find_all("a",class_="LatestNews-headline"):
    Headline.append(i.text)
for a in soup.find_all("time",class_="LatestNews-timestamp"):
    Time.append(a.text)
for b in soup.find_all("a",class_="LatestNews-headline"):
    News_Link.append(b.text)
data = {"HeadLine":Headline,"Time":Time,"News_Link":News_Link}
df = pd.DataFrame(data)
df


# In[6]:


#QUSTION 6)

link2 = requests.get('https://www.journals.elsevier.com/artificial-intelligence/most-downloaded-articles')
link2
soup = BeautifulSoup(link2.content)
soup
peper_title = []
auther = []
publish_date = []
peper_url = []
for i in soup.find_all("h2",class_="sc-1qrq3sd-1 gRGSUS sc-1nmom32-0 sc-1nmom32-1 btcbYu goSKRg"):
    peper_title.append(i.text)
for a in soup.find_all("span",class_="sc-1w3fpd7-0 dnCnAO"):
    auther.append(a.text)
for b in soup.find_all("span",class_="sc-1thf9ly-2 dvggWt"):
    publish_date.append(b.text)
for c in soup.find_all("a",class_="sc-5smygv-0 fIXTHm"):
    peper_url.append(c.text)
Data = {"PEPER_TITLE":peper_title,"AUTHER":auther,"PUBLISH_DATE":publish_date,"PEPER_URL":peper_url}
df = pd.DataFrame(Data)
df
    
    


# In[ ]:




