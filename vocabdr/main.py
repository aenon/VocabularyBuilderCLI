
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


# In[14]:

row = df_barron.iloc[0]


# In[151]:

def vocatest(df):
    for index, row in df.iterrows():
        meaning = str(row.MEANING)
        word_input = raw_input(meaning + "\n: ").lower().strip()
        if word_input == ":q":
            print("Exiting...\n")
            break
        if word_input == row.WORD:
            print("Correct!\n")
        else:
            print("Incorrect!\n")
            print("Answer: " + row.WORD + "\n")


# In[145]:

# df_g3000 = pd.read_json('../dict/g3000.json')
# df_g3000.rename(columns = {'word': 'WORD'}, 
#                 inplace=True)
# df_g3000['MEANING'] = df_g3000.desc.apply(lambda desc: '\n'.join([x for x in desc.split('\n') if x.upper().startswith('[MEANING')]))
# df_g3000[['WORD', 'MEANING']].to_csv('../dict/g3000.csv', index=0)


# In[146]:

df_g3000 = read_word_dict('g3000')


# In[96]:

row = df_g3000.iloc[0]


# In[ ]:



