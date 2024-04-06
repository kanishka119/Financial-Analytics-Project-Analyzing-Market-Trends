#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[4]:


df = pd.read_csv(r'C:\Users\lata6\Downloads\Financial Analytics data (1).csv')


# In[5]:


df


# In[6]:


df.head(5) #displaying first 5 rows 


# In[7]:


missing_values = df.isnull().sum() #checking for missing values


# In[8]:


#checking data types
df.dtypes


# In[9]:


#cleaning the data


# In[10]:


#filling missing value


# In[11]:


missing_values


# In[12]:


df = df.dropna(subset=['Mar Cap - Crore', 'Sales Qtr - Crore'], how='any')


# In[13]:


df = df.fillna(0)


# In[14]:


df.columns = df.columns.str.strip()


# In[15]:


df.columns = [col.lower().replace(" ", "_") for col in df.columns]


# In[16]:


df.head()


# In[17]:


df.isnull().sum()


# In[20]:


top_market_cap = df.sort_values(by='mar_cap_-_crore', ascending=False).head(10)


# In[21]:


top_market_cap
# Top companies by market capitalization


# In[22]:


top_sales = df.sort_values(by='sales_qtr_-_crore', ascending=False).head(10)


# In[23]:


top_sales
# Top companies by quarterly sales


# In[24]:


df.plot.scatter(x='mar_cap_-_crore', y='sales_qtr_-_crore')
# Relationship between market capitalization and quarterly sales


# In[28]:


df['mar_cap_-_crore'].corr(df['sales_qtr_-_crore'])
# Correlation between market capitalization and quarterly sales


# In[30]:


# Industry analysis
industry_groups = df.groupby(df['name'].str.split().str[-1])
print(industry_groups['mar_cap_-_crore'].sum().sort_values(ascending=False).head(10))


# In[31]:


plt.figure(figsize=(10, 6))
sns.scatterplot(x='mar_cap_-_crore', y='sales_qtr_-_crore', data=df)
plt.title('Relationship between Market Capitalization and Quarterly Sales')
plt.xlabel('Market Capitalization (Crore)')
plt.ylabel('Quarterly Sales (Crore)')
plt.show()


# In[ ]:





# In[ ]:




