#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np


# In[2]:


data=pd.read_excel('dataset.xlsx')


# In[3]:


print("Size of the dataset :", data.shape)


# In[4]:


data


# In[5]:


data.isnull().sum()


# In[7]:


data=data.fillna({'SUB_GENRE':'NA'})


# In[8]:


data


# In[9]:


data.columns


# In[10]:


pd.pivot_table(data,'IMDB_RATING',['YEAR','GENRE'],aggfunc=np.mean)


# In[ ]:




