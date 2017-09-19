
# coding: utf-8

# In[26]:

import pandas as pd
import sys


# In[27]:

# if len(sys.argv) > 1:
#     word_dict = sys.argv[1]
# else:
#     word_dict = "barrons_333"


# In[28]:

def read_word_dict(word_dict):
    df_dict = pd.read_csv("../dict/" + word_dict + ".csv")
    return df_dict


# In[29]:

df_barron = read_word_dict("barrons_333")


# In[33]:

for index, row in df_barron.iterrows():
    print(row.WORD)
    user_input = raw_input("Press Enter to continue...")
    if user_input == "q":
        break
    print(row.MEANING)
    user_input = raw_input("Press Enter to continue...")
    if user_input == "q":
        break
    print("\033[H\033[J")


# In[ ]:



