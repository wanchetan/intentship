#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re


# In[2]:


#- Write a Python program to replace all occurrences of a space, comma, or dot with a colon.
text = 'Python Exercises, PHP exercises.'
x=re.sub("[\s.,]", ":", text)
print(x)
         


# In[3]:


#-  Create a dataframe using the dictionary below and remove everything (commas (,), !, XXXX, ;, etc.) from the columns except words.
data =  {'SUMMARY' : ['hello, world!', 'XXXXX test', '123four, five:; six...']}
df= pd.DataFrame(data)
for x in df['SUMMARY']:
    y=re.sub('[^a-z\s]','',x)
    print(y)


# In[4]:


#Create a function in python to find all words that are at least 4 characters long in a string. The use of the re.compile() method is mandatory

def find(text):
   pattern = re.compile(r'\w{4}')
   match   = pattern.findall(text)
   return match 
text ="Nagpur is a large city in the central Indian state of Maharashtra."
result = find(text)
print(result)


# In[5]:


#Create a function in python to find all three, four, and five character words in a string. The use of the re.compile() method is mandatory.

def finds(string):
  pattern = re.compile(r'\w{3,5}')
  match = pattern.findall(string)
  return match 
string ="Nagpur is a large city in the central Indian state of Maharashtra."
result = finds(string)
print(result)


# In[6]:


#- Create a function in Python to remove the parenthesis in a list of strings. The use of the re.compile() method is mandatory.

def remove(text):
    pattern = re.compile(r"[()]") 
    for x in text:
        A = re.sub(pattern,"",x)
        return A


text= ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]
y= remove(text)  
print(y)


# In[7]:


# Write a python program to remove the parenthesis area from the text stored in the text file using Regular Expression.
T = ["example (.com)", "hr@fliprobo (.com)", "github (.com)", "Hello (Data Science World)", "Data (Scientist)"]

for i in T:
    B=re.sub(r'[()]','',i)
    print(B)


# In[8]:


#Write a regular expression in Python to split a string into uppercase letters.
str = "ImportanceOfRegularExpressionsInPython"
pattern= re.findall(r'[A-Z][a-z]*',str)
print(pattern)


# In[9]:


#Create a function in python to insert spaces between words starting with numbers.
D = 'RegularExpression1IsAn2ImportantTopic3InPython'
def insert(D):
    pattern = r'(\d)[A-z0-9]'
    result = re.sub(pattern,r' \1', D)
    return result 
x = insert(D)
print(x)


# In[10]:


#Create a function in python to insert spaces between words starting with capital letters or with numbers.
E = "RegularExpression1IsAn2ImportantTopic3InPython"
def space(E):
    pattern = r'(\d)[A-Z0-9]'
    result = re.sub(pattern,r' \1 ',E)
    return result 
z = space(E)
print(z)


# In[11]:


#qustion10
data = pd.read_csv(r"C:\Users\CHETAN\Downloads\happiness_score_dataset.csv")
df = pd.DataFrame(data)
pattern = re.compile(r'\w{6}')
for name in df['Country']:
    first = re.findall(pattern,name)
    return first


df.insert(0,'first_five_letters',first)
df[first_five_letters]


# In[12]:


#- Write a Python program to match a string that contains only upper and lowercase letters, numbers, and underscores.

strings = "Write a Python program  lowercase letters, number234, and under_scores"
x = re.match(r'[a-zA-Z0-9_]+',strings)
print(x)



# In[ ]:





# In[ ]:




