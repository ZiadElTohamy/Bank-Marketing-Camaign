#!/usr/bin/env python
# coding: utf-8

# In[276]:


import pandas as pd


# In[277]:


import numpy as np


# In[278]:


import matplotlib as plt


# In[279]:


df=pd.read_csv('test.csv')


# In[280]:


print(df)


# In[281]:


df.index.values
#df has 4520 entries


# In[282]:


#filtering process FIRST checking for nulls and wrong data
df.isnull().sum() # no null values
#df = df.drop(df["duration" > 60].index ####################¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢¢€€€€€€€€€€


# In[283]:


averageB=df['balance'].mean() #average balance
print(averageB)


# In[314]:


#adding students with low average to subset for future plans since theh can't afford to subscribe in the meantime

df_future=df[(df['job']=="student") & (df["balance"]<averageB)].index
print(df_future)

#filtering them out from dataset to continue analysis
df.drop(df_future , inplace=True)

#downloadthem for dashboard
#####df_future.to_excel('future_plans.xls', index=False)


# In[285]:


#removing people that have loan that can't subscribe to the program
df_drop_loan = df[df['loan'] == 'yes'].index
df.drop(df_drop_loan , inplace=True)


# In[286]:


df #dataset after 


# In[287]:


#removing data of customers with house loan
df_drop_Hloan = df[df['housing'] == 'yes'].index
df.drop(df_drop_Hloan , inplace=True)


# In[288]:


df


# In[289]:


#removing data of customers with low yearly income that will porbably wont subscribe
df_drop_Balance = df[df['balance'] < 1000].index


# In[290]:


df.drop(df_drop_Balance , inplace=True)


# In[291]:


df


# In[292]:


#dropping customers with phone call that lasted less than 60 sec and haven't subscribed
df = df.drop(df[(df.duration < 60) & (df.y =='no')].index)


# In[293]:


df


# In[301]:


df_future_potential_cust =df[(df.duration > 60) & (df.y =='no')].index
df_future_potential_cust.to_excel('future_potential_cust.xls', index=False)


# In[303]:


#droping customers with unkown education 
df_unknown_education=df[df["education"]=='unknown'].index


# In[304]:


df.drop(df_unknown_education, inplace=True)


# In[305]:


#removing customers with last failed campaign to not waste this campaign on them
df_failed_campaign=df[df["poutcome"]=='failure'].index


# In[306]:


df.drop(df_failed_campaign, inplace=True)


# In[307]:


df


# In[311]:


df.to_csv('after_filter.csv', index=False)

