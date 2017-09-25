
# coding: utf-8

# # vocabdr
# Yet another vocabulary builder

# In[2]:


import pandas as pd
import sys
import math
# import urwid

# import sys
# #in case there are special characters in names
# reload(sys)
# sys.setdefaultencoding("utf-8")


# In[37]:


# if len(sys.argv) > 1:
#     word_dict = sys.argv[1]
# else:
#     word_dict = "barrons_333"


# In[42]:


class color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


# In[115]:


def dict_read(word_dict):
    df = pd.read_csv("../dict/" + word_dict + ".csv")
    df['REVIEW'] = True
    return df


# In[116]:


def dict_select():
    print("Select one dictionary to study")
    print("\t1. G3000")
    print("\t2. Barron's 333")
    selection = raw_input("Dictionary number? [1]").strip()
    if selection.startswith("2"):
        print("Your choice is Barron's 333.")
        return "barrons_333"
    else:
        print("your choice is G3000.")
        return "g3000"


# In[117]:


def unit_select(df):
    last_unit = int(math.ceil(len(df) / 25.0))
    answer = raw_input("Which unit to learn? (1 ~ {}): ".format(str(last_unit))).strip()
    if answer.isdigit():
        if int(answer) in range(1, last_unit + 1):
            return int(answer)
    return 1


# In[156]:


def unit_learn(df, unit):
    print("Let's learn unit {}!".format(unit))
    df = df.iloc[25*(unit-1): 25*unit]
    while len(df) > 0:
        for index, row in df.iterrows():
            word, meaning, desc = map(lambda x: x.strip(), 
                                      [row.WORD, row.MEANING, row.DESC])
            if len(word) >= 4:
                word_hint = word[0] + '␣' * (len(word) - 2) + word[-1]
            else:
                word_hint = word[0] + '␣' * (len(word) - 1)
                
            print(color.BOLD + word_hint + color.END)
            print(meaning)
            word_input = raw_input().lower().strip()
            if word_input == ":q":
                print("Exiting...\n")
                break
            if word_input == word:
                sys.stderr.write("\x1b[2J\x1b[H")
                print(color.DARKCYAN + color.BOLD + word + color.END)
                print(desc)
                df.at[index, 'REVIEW'] = False
            else:
                sys.stderr.write("\x1b[2J\x1b[H")
                print(color.RED + color.BOLD + word + color.END)
                print(desc)
            raw_input("Press enter to continue...")
            sys.stderr.write("\x1b[2J\x1b[H")
        df = df[df.REVIEW]          


# In[ ]:


def main():
    df = dict_read(dict_select())
    unit = unit_select(df)
    unit_learn(df, unit)

if __name__ == "__main__":
    main()

