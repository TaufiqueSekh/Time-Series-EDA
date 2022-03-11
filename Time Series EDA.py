#!/usr/bin/env python
# coding: utf-8

# In[4]:


## Install Pandas Data Reader
get_ipython().system('pip install pandas-datareader')


# In[6]:


import pandas_datareader as pdr
import pandas as pd
import numpy as np
from datetime import datetime


# In[8]:


df_tesla=pdr.get_data_yahoo('TSLA')


# In[9]:


df_tesla.head()


# In[15]:


df_tesla["High"].plot(figsize=(9,4))


# In[20]:


df_tesla["High"].plot(xlim=['2020-01-01','2021-09-01'],ylim=[0,900],figsize=(9,4),c='green',ls="--")


# In[25]:


index=df_tesla.loc['2020-01-01':'2021-09-01'].index


# In[26]:


share_open=df_tesla.loc['2020-01-01':'2021-09-01']['Open']


# In[27]:


share_open


# In[30]:


import matplotlib.pyplot as plt


# In[38]:


fig,ax=plt.subplots()
plt.tight_layout()
fig.autofmt_xdate() ##preventing overlap
ax.plot(index,share_open)


# In[54]:


# If we want Date to be a column
df_tesla=df_tesla.reset_index()


# In[55]:


df_tesla.info()


# In[56]:


# if date was in Object format ,
#then we have to transform into datetime format
pd.to_datetime(df_tesla["Date"])


# In[57]:


df_tesla.head()


# In[58]:


# Now i want date to be Index
df_tesla=df_tesla.set_index("Date")


# In[59]:


df_tesla


# In[61]:


datetime.now()


# In[62]:


def add_num(x,y):
    return x+y


# In[63]:


x=10
y=9
start=datetime.now()
add_num(x,y)
end=datetime.now()
print(end-start)


# In[65]:


date=datetime.now()


# In[66]:


date.date()


# In[68]:


date.weekday()


# In[69]:


date.month


# In[70]:


date.day


# In[71]:


date.year


# Time resampling

# In[73]:


df_tesla.tail()


# In[75]:


df_tesla.resample(rule="A").max()


# In[80]:


df_tesla.resample(rule="A").min()["Adj Close"].plot()


# In[81]:


#Annualwise 
df_tesla.resample(rule="A").max()["Adj Close"].plot()


# In[85]:


# Quater wise
df_tesla.resample("QS").max()["High"].plot()


# In[86]:


# Busines Annual
df_tesla.resample("BA").max()


# In[88]:


# Business Quater
df_tesla.resample("BQS").max()["Adj Close"].plot(kind="bar")


# In[89]:


df_tesla.resample("M").mean()


# In[93]:


# weekly start from Monday
df_tesla.resample("W-MON").max()["Close"]


# In[95]:


df_tesla["High"].head()


# In[100]:


df_tesla["High"].rolling(2).mean()


# In[111]:


df_tesla['Open:30D rolling']=df_tesla["Open"].rolling(30).mean()


# In[112]:


df_tesla


# In[113]:


df_tesla[["Open","Open:30D rolling"]].plot(figsize=(12,5))


# In[ ]:




