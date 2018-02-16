
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import math 


# In[2]:


#reading the data and percentile value into dataframes don and per 
don = pd.read_csv(r"C:\Users\bnama\Desktop\Final_test\insight_DE\input\itcont.txt", sep='|', header=None)
p = open(r"C:\Users\bnama\Desktop\Final_test\insight_DE\percentile\percentile.txt")
for line in p: #to get the valueof the percentile
    h = line#dropping the columns which are of not necessary forour analysis


# In[3]:


#dropping the columns which are of not necessary forour analysis
cols = [1,2,3,4,5,6,8,9,11,12,16,17,18,19,20]
don.drop(don.columns[cols],axis=1,inplace=True)


# In[4]:


don[15].fillna(0,inplace=True) #replace all Na with zeroes in Other_ID 
don.dropna() # dropping all rows which have Na


# In[5]:


don = don[don[15] == 0] #segregating column Other_ID which contain only zeroes


# In[6]:


don_r = don.shape[0]  # no of rows after cleaning
print(don_r)


# In[7]:


temp = don[10].astype(str) #getting first five elements of zip 
for i in range(1,don_r+1):
    don[10][i] = temp[i][:5]


# In[8]:


ary = don[13].astype(str)  #getting year of transaction
for j in range(1,don_r+1):
    don[13][j] = ary[j][-4:]


# In[9]:


don[7] = don[7] + don[10].astype(str) # concatinating Name and zip to generate a unique key
don = don[don[7].duplicated(keep=False)] # list of repeat donors


# In[10]:


don = don[don[13] == 2018] # for present year '2018'


# In[11]:


don.reset_index(drop = True)


# In[12]:


# calculating the percentile
a = don.shape[0]
b = pd.to_numeric(h, errors='coerce')
c = (b/100)*a
d = math.ceil(c)


# In[13]:


# generating running total of total contributions
don[16] = don.groupby([0])[14].cumsum()


# In[14]:


# calculating the total number of donations from donors to recepient
don.sort_values([14])
don[17] = don.groupby([0])[10].cumcount()+1


# In[15]:


print(don)


# In[16]:


don.reset_index(drop = True)


# In[34]:


don[18] = (don[16][d-1])
print(don)


# In[36]:


col = [0,10,13,18,16,17]
don.to_csv(r'C:\Users\bnama\Desktop\Final_test\insight_DE\output\repeat_donors.txt',columns = col,header=None,index=None,sep='|')

