#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
array_np = np.array([(1,2,3),(4,5,6)])
print(array_np.shape)



# In[4]:


import numpy as np
# create matrix with function
import numpy as np
array_np = np.arange(6).reshape(2,3)
print(array_np)


# In[7]:


#how to add numpy

arr_np1 = np.array([10,10,10])
arr_np2 = np.array([4,4,4])

arr_np3 = arr_np1+arr_np2
arr_np3


# In[8]:


#how to sub numpy

arr_np1 = np.array([10,10,10])
arr_np2 = np.array([4,4,4])

arr_np3 = arr_np1-arr_np2
arr_np3


# In[9]:


#how to mul numpy

arr_np1 = np.array([10,10,10])
arr_np2 = np.array([4,4,4])

arr_np3 = arr_np1*arr_np2
arr_np3


# In[10]:


#how to dev numpy array output will be float

arr_np1 = np.array([10,10,10])
arr_np2 = np.array([4,4,4])

arr_np3 = arr_np1/arr_np2
arr_np3


# In[11]:


#how to get remonder

arr_np1 = np.array([10,10,10])
arr_np2 = np.array([4,4,4])

arr_np3 = arr_np1%arr_np2
arr_np3


# In[12]:


#add any value to array

arr_np1 = np.array([10,10,10])
arr_np1+=5
arr_np1


# In[13]:


#sub any value to array

arr_np1 = np.array([10,10,10])
arr_np1-=5
arr_np1


# In[15]:


#get minimum number

arr_np1 = np.array([10,12,9])
arr_np1.min()


# In[16]:


#get maximum number

arr_np1 = np.array([10,12,9])
arr_np1.max()


# In[17]:


#get sum of array numbers

arr_np1 = np.array([10,12,9])
arr_np1.sum()


# In[ ]:




