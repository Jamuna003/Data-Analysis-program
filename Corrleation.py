#!/usr/bin/env python
# coding: utf-8

# In[8]:


import numpy as np
import pandas as pd
import fix_yahoo_finance as fyf
import matplotlib.pyplot as plt


# In[9]:


correlation =pd.read_csv("C:/Users/Jamuna/Desktop/DataAnalysis_Leadbook/data_analysis/data.csv")
correlation.head()


# In[10]:


print(correlation.corr())


# In[15]:


corr = correlation.corr()
fig = plt.figure()
ax = fig.add_subplot(111)
cax = ax.matshow(corr,cmap='coolwarm', vmin=-1, vmax=1)
fig.colorbar(cax)
ticks = np.arange(0,len(correlation.columns),1)
ax.set_xticks(ticks)
plt.xticks(rotation=90)
ax.set_yticks(ticks)
ax.set_xticklabels(correlation.columns)
ax.set_yticklabels(correlation.columns)
plt.show()


# In[ ]:





# In[ ]:




