#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
import numpy as np
import pandas as pd
import scipy
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


import pandas as pd

df=pd.read_csv('insurance_csv.csv')
series1=df.charges
series1.dtypes


# In[3]:


len(series1)


# In[5]:


df.shape


# In[6]:


df.dtypes


# In[7]:


df.head()


# In[8]:


df.info()


# In[9]:


df['sex'].value_counts()


# In[10]:


sns.countplot(df['sex'])


# In[11]:


df['smoker'].value_counts()


# In[12]:


sns.countplot(df['smoker'])
plt.show()


# In[13]:


df['children'].value_counts()


# In[14]:


sns.countplot(df['children'])
plt.show()


# In[15]:


sns.countplot(df['region'])
plt.show()


# In[16]:


pd.crosstab(df['children'],df['smoker'])


# In[17]:


sns.countplot(df['children'],hue=df['smoker'])
plt.show()


# In[18]:


df.describe()


# In[19]:


sns.distplot(df['age'])
plt.show()


# In[20]:


sns.distplot(df['children'])
plt.show()


# In[21]:


sns.distplot(df['children'])
plt.show()


# In[22]:


sns.boxplot(x='bmi',data=df), 
plt.show()
sns.boxplot(x='age',data=df)
plt.show()
sns.boxplot(x='charges',data=df)
plt.show()


# In[23]:


sns.pairplot(df[['age', 'sex', 'bmi', 'children', 'smoker', 'region', 'charges']])


# In[24]:


df[['sex', 'bmi', 'children']]


# In[25]:


df.smoker.value_counts()


# In[26]:


sns.scatterplot(x="bmi", y="charges", data=df)


# In[27]:


sns.boxplot(df['charges'], df['smoker'])


# In[28]:


sns.boxplot(df['bmi'], df['sex'])


# In[29]:


print("Total count of smokers is ", df[df['smoker']=='yes'].shape[0])
print("Total count of male smokers is ", df[df['sex']=='male'].shape[0])
print("Total count of female smokers is ", df[df['sex']=='female'].shape[0])


# In[30]:


sns.boxplot (df['bmi'],df[df['sex']=='female']['children'])

