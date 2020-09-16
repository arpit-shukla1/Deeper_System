#!/usr/bin/env python
# coding: utf-8

# In[52]:


import json
import pandas as pd


# In[53]:


js=pd.read_json('./source_file_2.json')


# In[54]:


js.sort_values(by='priority',inplace=True)


# In[55]:


watchers=dict()
managers=dict()


# In[56]:


for i in range(js.shape[0]):
    for j in js.iloc[i,0]:
        try:
            managers[j].append(js.iloc[i,1])
        except:
            managers[j]=[js.iloc[i,1]]
    
    for j in js.iloc[i,3]:
        try:
            watchers[j].append(js.iloc[i,1])
        except:
            watchers[j]=[js.iloc[i,1]]


# In[57]:


temp=[]
for i,j in managers.items():
    temp.append({'name':i,'project':j})

with open('manager.json','w') as f:
    json.dump(temp,f,indent=2)


# In[58]:


temp=[]
for i,j in watchers.items():
    temp.append({'name':i,'project':j})

with open('watchers.json','w') as f:
    json.dump(temp,f,indent=2)


# In[ ]:




