
# coding: utf-8

# In[36]:

import pandas as pd
import sys
# in case there are special characters in names
reload(sys)
sys.setdefaultencoding("utf-8")


# In[2]:

# if len(sys.argv) > 1:
#     word_dict = sys.argv[1]
# else:
#     word_dict = "barrons_333"


# In[3]:

def read_word_dict(word_dict):
    df_dict = pd.read_csv("../dict/" + word_dict + ".csv")
    return df_dict


# In[12]:

df_barron = read_word_dict("barrons_333")
df_barron.WORD = df_barron.WORD.str.lower()


# In[13]:

df_barron.head()


# In[14]:

row = df_barron.iloc[0]


# In[25]:

for index, row in df_barron.iterrows():
    word_input = raw_input(row.MEANING + ": ").lower().strip()
    if word_input == ":q":
        print("Exiting...")
        break
    if word_input == row.WORD:
        print("Correct!")
    else:
        print("Incorrect!")
        print("Answer: " + row.WORD)


# In[57]:

data = open('../dict/g3000.json').read()


# In[60]:

data = open('../dict/g3000.txt').read()


# In[63]:

data.decode("utf-8")


# In[ ]:




# In[64]:

import json
from pprint import pprint
import codecs


# In[65]:

with open('../dict/g3000.json') as data_file:    
    data = json.load(data_file)


# In[67]:

print(data[0]['desc'])


# In[ ]:




# In[44]:

with codecs.open('../dict/g3000.json', 'r', 'utf-8') as data_file:
    data = json.load(data_file, 'utf-8')


# In[49]:

data[0]['desc']


# In[ ]:



