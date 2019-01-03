#!/usr/bin/env python
# coding: utf-8

# In[41]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

plt.style.use('bmh')


# In[43]:


df =pd.read_csv("C:/Users/Jamuna/Desktop/DataAnalysis_Leadbook/data_analysis/data.csv")
df.head()


# In[3]:


pwd


# In[44]:


df.info()


# In[45]:


df2 = df[[column for column in df if df[column].count() / len(df) >= 0.3]]
del df2['Id']
print("List of dropped columns:", end=" ")
for c in df.columns:
    if c not in df2.columns:
        print(c, end=", ")
print('\n')
df = df2


# In[46]:


print(df['Employees'].describe())
plt.figure(figsize=(9, 8))
sns.distplot(df['Employees'], color='g', bins=100, hist_kws={'alpha': 0.4});


# In[47]:


df2.isnull().tail()


# In[48]:


df2.isnull().sum()


# In[53]:


df2[df2.Employees.isnull()]


# In[54]:


df2.shape


# In[60]:


df2["Revenue"].value_counts(dropna=False)


# In[62]:


df2.dropna(subset=["Employees","Revenue"],how="any").shape


# In[84]:


print(df['Revenue'].describe())
plt.figure(figsize=(14, 11))
sns.distplot(df['Revenue'], color='g', bins=100, hist_kws={'alpha': 0.4});

print(df['Employees'].describe())
plt.figure(figsize=(14, 11))
sns.distplot(df['Employees'], color='g', bins=100, hist_kws={'alpha': 0.4});


# In[72]:


df2.dropna(axis=0)


# In[82]:


cols = ['Employees', 'Revenue']
df2.dropna(subset=cols, inplace=True)
df2.shape


# In[ ]:




