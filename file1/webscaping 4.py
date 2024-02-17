#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install selenium')


# In[1]:


#import neccesary liaberies
import pandas as pd 
import selenium 
from selenium import webdriver
from selenium.webdriver.common.by import By


# In[2]:


from selenium.common.exceptions import NoSuchElementException
import time


# In[3]:


from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# In[4]:


#connect driver to chrome 
driver = webdriver.Chrome()


# In[5]:


#opening amazon.in in automated browser 
driver.get("https://www.amazon.in/")


# In[6]:


#fetching details of coffee machines
X= driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[2]/div[1]/input")
X.send_keys("coffe machine")
# searching coffee machines
y= driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div[2]/div/form/div[3]/div/span/input")
y.click()


# In[7]:


# fetching coffee machine url 
coffee_machines_url = []
C =driver.find_elements(By.XPATH,'//h2[@class="a-size-mini a-spacing-none a-color-base s-line-clamp-2"]/a')
for i in C:
    coffee_machines_url.append(i.get_attribute('href'))
# print lenghth of machine url    
len(coffee_machines_url)


# In[10]:


#creat empty list for brand
brand = []
# fetching brand names 
for i in coffee_machines_url:
    driver.get(i)
    time.sleep(5)
    try:
        brand_name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[4]/div[44]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/span')
        brand.append(brand_name.text)
    except NoSuchElemnentException:
         brand.append('--')        
    
    


# In[11]:


print(brand)


# In[13]:


# create empty list of price, dilivery, product, avaiblity 
prices = []
diliverys = []
products = []
avaiblitys = []
# fetching of details as per qustion 
for a in coffee_machines_url:
    driver.get(a)
    time.sleep(5)
    try:
        p = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[1]/div[3]/div/div[1]/div/div/div/form/div/div/div/div/div[3]/div/div[1]/div/div/span[1]/span[2]/span[2]')
        prices.append(p.text)
        d = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[1]/div[3]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[3]/div[10]/div[1]/div/div/div/span/span[1]')
        diliverys.append(d.text)
        product = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[4]/div[1]/div/h1/span')
        products.append(product.text)
        A = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[1]/div[3]/div/div[1]/div/div/div/form/div/div/div/div/div[4]/div/div[5]/div/div[1]/span')
        avaiblitys.append(A.text)
    except NoSuchElementException:
        price.append('---')
        


# In[19]:


# create empty dataframe
df = pd.DataFrame({})
# add data in empty dataframe
df['brand'] = brand
df['product'] = products
df['price'] = prices
df['dilivery'] = diliverys
df['avaibility'] = avaiblitys
df['url'] = coffee_machines_url
df


# In[18]:


#closing driver
driver.close()


# In[4]:


#connect driver to chrome
driver = webdriver.Chrome()


# In[5]:


#connect to flipkart website
driver.get("https://www.flipkart.com/")


# In[6]:


#sending redmi fetching element
mobile = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
mobile.send_keys("redmi")


# In[7]:


#clicking search botton 
C= driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button")
C.click()                          


# In[8]:


#create empty list
mobile_url = []
#fetching mobile data url
m= driver.find_elements(By.XPATH,'//div[@class="_2kHMtA"]/a')
for i in m:
    mobile_url.append(i.get_attribute('href'))
len(mobile_url)    


# In[12]:


back = []
for i in mobile_url:
    driver.get(i)
    delay = 10
    z= driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
    z.click()
    try:
        b = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[5]/table/tbody/tr[2]/td[2]/ul/li")
        back.append(b.text)
    except NoSuchElementException:
        back.append('__')


# In[13]:


back


# In[14]:


brand_name = []
for a in mobile_url:
    driver.get(a)
    delay = 10
    z= driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
    z.click()
    try:
        B = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[1]/table/tbody/tr[3]/td[2]/ul/li")
        brand_name.append(B.text)
    except NoSuchElementException:
        brand_name.append('--')


# In[15]:


brand_name


# In[21]:


phone_name = []
for b in mobile_url:
    driver.get(b)
    delay = 10
    z= driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
    z.click()
    try:
        p = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[1]/h1/span")
        phone_name.append(p.text)
    except NoSuchElementException:
        phone_name.append('--')
        


# In[22]:


phone_name


# In[17]:


colour = []
ram = []
display = []
Rom = []
price = []
for c in mobile_url:
    driver.get(c)
    delay = 10
    z= driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
    z.click()
    try:
        c = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[1]/table/tbody/tr[4]/td[2]/ul/li")
        colour.append(c.text)
        R = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[4]/table/tbody/tr[2]/td[2]/ul/li")
        ram.append(R.text)
        D = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[2]/table/tbody/tr[1]/td[2]/ul/li")
        display.append(D.text)
        rom = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[4]/table/tbody/tr[1]/td[2]/ul/li")
        Rom.append(rom.text)
        p = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[2]/div/div[4]/div[1]/div/div[1]")
        price.append(p.text)
    except NoSuchElementException:
        colour.append('--')
        ram.append('--')
        display.append('--')
        Rom.append('--')
        price.append('--')


# In[9]:


front = []
for f in mobile_url:
    driver.get(f)
    delay = 10
    z = driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
    z.click()
    try:
        f = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[5]/div/div[2]/div[1]/div[5]/table/tbody/tr[5]/td[2]/ul/li")
        front.append(f.text)
    except NoSuchElementException:
        front.append('--')
    


# In[23]:


phone_details = pd.DataFrame({})
phone_details['phone name'] = phone_name
phone_details['brand name'] = brand_name
phone_details['colour'] = colour 
phone_details['primery_camera'] = front
phone_details['secondary_camera'] = back
phone_details['display_size'] = display
phone_details['battery_capacity'] = Rom
phone_details['price'] = price
phone_details['url'] = mobile_url


# In[24]:


phone_details


# In[6]:


driver.close()


# In[4]:


driver = webdriver.Chrome()


# In[5]:


driver.get("https://images.google.com/")


# In[29]:


find = ['cars','fruits','machine learning','guitar','cakes']


# In[14]:


car = driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea")
car.send_keys("cars")
Cl= driver.find_element(By.XPATH,"/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div/span")
Cl.click()


# In[15]:


cars = []
c = driver.find_element(By.XPATH,'/html/body/div[2]/c-wiz/div[3]/div[1]/div/div/div/div/div[1]/div[1]/span/div[1]/div[1]/div[1]/a[1]/div[1]/img')
cars.append(c.get_attribute('src'))


# In[17]:


driver.close()


# In[7]:


driver = webdriver.Chrome()


# In[8]:


driver.get("https://www.digit.in/")


# In[9]:


laptop = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div/div/div[2]/form/input[1]")
laptop.send_keys(" gaming laptop")
search = driver.find_element(By.XPATH,"/html/body/div[1]/header/div/div[1]/div/div/div[2]/form/button")
search.click()


# In[10]:


laptop_url = []
laptop = driver.find_elements(By.XPATH,'//h3[@class=" text-clamp text-clamp-2"]/a')
for l in laptop:
    laptop_url.append(l.get_attribute('href'))


# In[30]:


name = []
operating_system = []
display_size = []
ram = []
ram_type = []
graphics_processor = []
processor = []
Storage_drive = []
battery_type = []
price = []

for L in laptop_url:
    driver.get(L)
    delay = 10
    try:
        n = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div[1]/h1')
        name.append(n.text)
        
        o = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/p')
        operating_system.append(o.text)
        
        D = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[4]/td/table/tbody/tr/td/p')
        display_size.append(D.text)
        
        R = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[8]/td/table/tbody/tr[1]/td/p')
        ram.append(R.text)
        
        G = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[10]/td/table/tbody/tr[3]/td/p')
        graphics_processor.append(G.text)
        
        P = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[10]/td/table/tbody/tr[4]/td/p')
        processor.append(P.text)
        
        S = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[12]/td/table/tbody/tr[1]/td/p')
        Storage_drive.append(S.text)
        
        B = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[14]/td/table/tbody/tr[1]/td/p')
        battery_type.append(B.text)
        
        pri = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div[4]/div[9]/div[1]/div/div[2]/div[3]/div/div[1]')
        price.append(pri.text)
    except NoSuchElementException:
        name.append('--')
        operating_system.append('--')
        display_size.append('--')
        ram.append('--')
        graphics_processor.append('--')
        processor.append('--')
        Storage_drive.append('--')
        battery_type.append('--')
        price.append('--')
        


# In[11]:


Storage_drive = []

for L in laptop_url:
    driver.get(L)
    delay = 10
    try:
        S = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[12]/td/table/tbody/tr[1]/td')
        Storage_drive.append(S.text)
    except NoSuchElementException:
         Storage_drive.append('--')


# In[12]:


Storage_drive


# In[13]:


name = []

for L in laptop_url:
    driver.get(L)
    delay = 10
    try:
        n = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div/div/div/div/div[2]/div[1]/div[1]/h1')
        name.append(n.text)
    except NoSuchElementException:
        name.append('--')    


# In[14]:


name


# In[15]:


battery_type = []

for L in laptop_url:
    driver.get(L)
    delay = 10
    try:
        B = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[14]/td/table/tbody/tr[1]/td/p')
        battery_type.append(B.text)
    except NoSuchElementException:
        battery_type.append('--')
        
        


# In[ ]:


battery_type


# In[16]:


operating_system = []

for L in laptop_url:
    driver.get(L)
    delay = 10
    try:
        o = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/p')
        operating_system.append(o.text)
    except NoSuchElementException:
        operating_system.append('--')


# In[ ]:


operating_system 


# In[17]:


ram = []

for L in laptop_url:
    driver.get(L)
    delay = 10
    try:
        R = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[8]/td/table/tbody/tr[1]/td/p')
        ram.append(R.text)
    except NoSuchElementException:
        ram.append('--')


# In[ ]:


ram


# In[18]:


display_size = []

for L in laptop_url:
    driver.get(L)
    delay = 10
    try:
        D = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[4]/td/table/tbody/tr/td/p')
        display_size.append(D.text)
    except NoSuchElementException:  
        display.append('--')


# In[ ]:


display_size


# In[19]:


graphics_processor = []

for L in laptop_url:
    driver.get(L)
    delay = 10
    try:
        G = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[10]/td/table/tbody/tr[3]/td/p')
        graphics_processor.append(G.text)
    except NoSuchElementException:  
        display_size.append('--')


# In[ ]:


graphics_processor


# In[20]:


processor = []

for L in laptop_url:
    driver.get(L)
    delay = 10
    try:
        P = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[10]/td/table/tbody/tr[4]/td/p')
        processor.append(P.text)
    except NoSuchElementException:  
         processor.append('--')


# In[ ]:


processor


# In[21]:


price = []

for L in laptop_url:
    driver.get(L)
    delay = 10
    try:
        pri = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div/div/div/div/div[2]/div[1]/div[4]/div[9]/div[1]/div/div[2]/div[3]/div/div[1]')
        price.append(pri.text)
    except NoSuchElementException: 
        price.append('--')


# In[ ]:


price


# In[25]:


laptop_data = pd.DataFrame({})
laptop_data['laptop_name'] = name[:10]
laptop_data['operating_system'] = operating_system[:10]
laptop_data['processor'] = processor[:10]
#laptop_data['graphics_processor'] = graphics_processor[:10]
laptop_data['Storage_drive'] = Storage_drive[:10]
laptop_data['battery_type'] = battery_type[:10]
laptop_data['ram'] = ram[:10]
laptop_data['display_size'] = display_size[:10]
laptop_data['price'] = price[:10]
laptop_data['url'] = laptop_url[:10]


# In[26]:


laptop_data


# In[ ]:




