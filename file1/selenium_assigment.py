#!/usr/bin/env python
# coding: utf-8

# In[1]:


# first install selenium tool

get_ipython().system('pip install selenium')


# In[2]:


# import all required liaberies 

import pandas as pd 
import selenium
from selenium import webdriver 
import warnings 
warnings.filterwarnings('ignore')
from selenium.webdriver.common.by import By


# In[3]:


# QUSTION 1)

# connect driver to chrome browser 

driver = webdriver.Chrome()


# In[4]:


#Opening the shine.com on automated chrome 
driver.get("https://www.shine.com")


# In[6]:


# fetching element of Data Analyst

designation = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input")
designation.send_keys("Data Analyst")

# fetching element of location 

location = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys("Bangalore")

# clicking search botton 

search = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[9]:


# create empty list 

Company = []
job_title =[]
job_location = []
experiance_required = []

# fetching titles as per qustion

titles = driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for a in titles:
    job_title.append(a.text)

# feching company name as per qustion 

    company= driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]/span')
    for b in company:
        Company.append(b.text)
        
# fetching experiance as per qustion         
        
    experiance = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
    for c in experiance:
        experiance_required.append(c.text)    
        
# fetching location as per qustion
      
    location = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
    for d in location:
        job_location.append(d.text)
        
# create empty dataframe        

df = pd.DataFrame({})

# adding data as per qustion 

df['company']= Company[:11]
df['job_title']= job_title[:11]
df['experiance']= experiance_required[:11]
df['location']= job_location[:11]

df


# In[ ]:





# In[ ]:





# In[3]:


#QUSTION 2)

# connect to chrome browser 
driver = webdriver.Chrome()


# In[4]:


# opining the shine.com in chrome browser 
driver.get('https://www.shine.com')


# In[10]:


# fetching element of Data science 
D = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[1]/div/input") 
D.send_keys("Data Scientist")

# fetching element of location
location = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[1]/ul/li[2]/div/input")
location.send_keys("Bangalore")

# clicking element 
search = driver.find_element(By.XPATH,"/html/body/div/div[4]/div/div[2]/div[2]/div/form/div/div[2]/div/button")
search.click()


# In[30]:


# create empty list 
Job_title = []
company = []
experiance = []
location = []

# fetching first job title name as per qustion
title = driver.find_elements(By.XPATH,'//h2[@itemprop="name"]')
for T in title:
    Job_title.append(T.text)
        
# fetching comapny name as per qustion         
Company = driver.find_elements(By.XPATH,'//div[@class="jobCard_jobCard_cName__mYnow"]')
for C in Company:
    company.append(C.text)
    
# fetching experiance as per qustion 
Experiance = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_jobIcon__3FB1t"]')
for E in Experiance:
    experiance.append(E.text)
    
# fetching location as per qustion 
Location = driver.find_elements(By.XPATH,'//div[@class=" jobCard_jobCard_lists_item__YxRkV jobCard_locationIcon__zrWt2"]')
for L in Location:
    location.append(L.text)
    

# create empty DataFrame 
data = pd.DataFrame({})

# adding data as per qustion 
data["title"]= Job_title[:11]
data["company"]= company[:11]
data["experiance"]= experiance[:11]
data["location"]= location[:11]

data
    


# In[ ]:




