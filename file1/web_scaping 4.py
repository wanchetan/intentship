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
# qus 1) & qus 2)
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


# In[11]:


#creat empty list for brand
brand = []
# fetching brand names 
for i in coffee_machines_url:
    driver.get(i)
    delay = 10
    try:
        brand_name = driver.find_element(By.XPATH,'/html/body/div[2]/div/div[5]/div[3]/div[4]/div[44]/div[1]/div[1]/div/table/tbody/tr[1]/td[2]/span')
        brand.append(brand_name.text)
    except NoSuchElementException:
        brand.append('--')        
    
    


# In[12]:


print(brand)


# In[14]:


# create empty list of price, dilivery, product, avaiblity 
prices = []
diliverys = []
products = []
avaiblitys = []
# fetching of details as per qustion 
for a in coffee_machines_url:
    driver.get(a)
    delay = 10
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
        prices.append('---')
        diliverys.append('---')
        products.append('---')
        avaiblitys.append('---')
        


# In[16]:


# create empty dataframe
df = pd.DataFrame({})
# add data in empty dataframe
df['brand'] = brand[:20]
df['product'] = products[:20]
df['price'] = prices[:20]
df['dilivery'] = diliverys[:20]
df['avaibility'] = avaiblitys[:20]
df['url'] = coffee_machines_url[:20]
df


# In[11]:


#closing driver
driver.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[12]:


# qus no. 3)
driver = webdriver.Chrome()


# In[13]:


driver.get('https://images.google.com/')


# In[16]:


search = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/textarea')
search.send_keys('cars')
find = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/button/div/span')
find.click()


# In[27]:


for _ in range(10):
    driver.execute_script("window.scrollBy(0,20)")
    
img_url = [] 
img = driver.find_elements(By.XPATH,'//img[@class="rg_i Q4LuWd"]')
for u in img:
    source = u.get_attribute('src')
    if source is not None:
        if(source[0:4]=='http'):
            img_url.append(source)
for i in range(len(img_url)):
    if i>10:
        breakBy.XPATH,
        print("downloading images".format(i,10))
        response = requests.get(img_url[i])
        file = open(r"D:\text"+str(i)+".jpg","wb")
        file.write(response.content)


# In[ ]:





# In[ ]:





# In[ ]:





# In[77]:


# qus 4)
#connect driver to chrome
driver = webdriver.Chrome()


# In[78]:


#connect to flipkart website
driver.get("https://www.flipkart.com/")


# In[79]:


#sending redmi fetching element
mobile = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/div/input')
mobile.send_keys("redmi")


# In[80]:


#clicking search botton 
C= driver.find_element(By.XPATH,"/html/body/div[1]/div/div[1]/div/div/div/div/div[1]/div/div[1]/div/div[1]/div[1]/header/div[1]/div[2]/form/div/button")
C.click()                          


# In[81]:


#create empty list
mobile_url = []
#fetching mobile data url
m= driver.find_elements(By.XPATH,'//div[@class="_2kHMtA"]/a')
for i in m:
    mobile_url.append(i.get_attribute('href'))
len(mobile_url)    


# In[92]:


# fetching back camera 
back = []
for i in mobile_url:
    driver.get(i)
    delay = 10
    z= driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
    z.click()
    try:
        b = driver.find_element(By.XPATH,'/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[4]/div/div[2]/div[1]/div[5]/table/tbody/tr[2]/td[2]/ul/li')
        back.append(b.text)
    except NoSuchElementException:
        back.append('__')


# In[93]:


back


# In[64]:


#fetching brand name 
brand_name = []
for a in mobile_url:
    driver.get(a)
    delay = 10
    z= driver.find_element(By.XPATH,'//button[@class="_2KpZ6l _1FH0tX"]')
    z.click()
    try:
        B = driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[1]/div[2]/div[9]/div[4]/div/div[2]/div[1]/div[1]/table/tbody/tr[3]/td[2]/ul/li")
        brand_name.append(B.text)
    except NoSuchElementException:
        brand_name.append('--')


# In[65]:


brand_name


# In[25]:


# fetching phone name
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
        


# In[26]:


phone_name


# In[66]:


# all neccesary data required 
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


# In[67]:


# fetching fornt camera
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
    


# In[68]:


# create dataframe and add data 
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


# In[69]:


phone_details


# In[64]:


#close driver
driver.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[44]:


# qus 5)
# importing regex
import re


# In[41]:


# connect to chrome
driver = webdriver.Chrome()


# In[42]:


# connecting  google map web site 
driver.get('https://www.google.com/maps/@21.1780481,79.0531951,15z?entry=ttu')


# In[43]:


# searching nagpur location on google map
search = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/form/input')
search.send_keys('nagpur')
click = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/div[8]/div[3]/div[1]/div[1]/div/div[2]/div[1]/button/span')
click.click()


# In[46]:


# fetching current url for langitude and longitude
try:
    url = driver.current_url
    lan_lag = re.findall(r"@(.*)data",url)
except NoSuchElementException:
    lan_lag('--')
    


# In[70]:


# convert integer to string for split langitude and longitude
x = str(lan_lag)
#split langitude and longitude
y = x.split(",")
y


# In[71]:


# store seprate varriable 
langitude = y[0]
langitude
longitude = y[1]
longitude


# In[72]:


langitude


# In[ ]:


#driver closing
driver.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[100]:


# qus 6) 
# connect automated browser 
driver = webdriver.Chrome()


# In[101]:


# connect to digit web site 
driver.get("https://www.digit.in/top-products/best-gaming-laptops-40.html")


# In[123]:


# fetching laptop url
url = []
m_url = driver.find_elements(By.XPATH,'//h3[@class="font130 mt0 mb10 mobilesblockdisplay "]/a')
for m in m_url:
    url.append(m.get_attribute('href'))
url    


# In[135]:


# create empty list which data fetching
name = []
Operating_System = []
Processor_Model = []
Storage_Drive = []
Display_Size = []
ram = []
graphics_processor = []
# fetching details
for d in url:
    driver.get(d)
    delay = 10
    try:
        n = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div/div/div/div/div[2]/div[1]/div[1]/h1')
        name.append(n.text)
        o = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[2]/td/table/tbody/tr[1]/td/p')
        Operating_System.append(o.text)
        p = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[12]/td/table/tbody/tr[6]/td/p')
        Processor_Model.append(p.text)
        s = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[14]/td/table/tbody/tr[1]/td/p')
        Storage_Drive.append(s.text)
        d = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[4]/td/table/tbody/tr/td/p')
        Display_Size.append(d.text)
        r = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[8]/td/table/tbody/tr[1]/td/p')
        ram.append(r.text)
        g = driver.find_element(By.XPATH,'/html/body/div[2]/div[3]/div[1]/div/div/div/div/div[2]/div[4]/div[3]/div[2]/table/tbody/tr[12]/td/table/tbody/tr[5]/td/p')
        graphics_processor.append(g.text)
    except NoSuchElementException:
        name.append('--')
        Operating_System.append('--')
        Processor_Model.append('--') 
        Storage_Drive.append('--')
        Display_Size.append('--')
        ram.append('--') 
        graphics_processor.append('--')


# In[137]:


# create empty dataframe and add data
df = pd.DataFrame({})
df['name'] = name[:7]
df['Operating_System'] =Operating_System[:7]
df['Processor_Model'] = Processor_Model[:7]
df['Storage_Drive']= Storage_Drive[:7]
df['ram'] = ram[:7]
df['graphics_processor']= graphics_processor[:7]
df['url'] = url
df


# In[138]:


# closing driver
driver.close()


# In[139]:


driver = webdriver.Chrome()


# In[141]:


driver.get('https://www.forbes.com/billionaires/')


# In[145]:


rank = []
Names = []
net_worth = []
age = []
country = []
source = []
industry = []

R = driver.find_elements(By.XPATH,'//div[@class="Table_rank___YBhk Table_dataCell__2QCve"]')
for r in R:
    rank.append(r.text)
    


# In[159]:


names = []
N = driver.find_elements(By.XPATH,'//div[@class="TableRow_cell__db-hv Table_cell__houv9"]')
for n in N:
    names.append(n.text)
names    


# In[160]:


# closing driver
driver.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[161]:


# qus 8)
# connect to chrome browser
driver = webdriver.Chrome()


# In[174]:


#searching song video
driver.get("https://www.youtube.com/watch?v=X3paOmcrTjQ")


# In[182]:


# scrapping all comments
for _ in range(50):
    driver.execute_script("window.scrollBy(0,500)")
    delay = 10
n_comments = [] 
n_comment = driver.find_elements(By.XPATH,'//yt-formatted-string[@class="style-scope ytd-comment-renderer"]')
for b in n_comment:
    n_comments.append(b.text)

n_comments 
    


# In[183]:


# length of comments
len(n_comments)


# In[184]:


# closing driver 
driver.close()


# In[ ]:





# In[ ]:





# In[ ]:





# In[198]:





# In[ ]:




