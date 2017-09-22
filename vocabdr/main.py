
# coding: utf-8

# In[1]:

import pandas as pd
import sys


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


# In[ ]:



