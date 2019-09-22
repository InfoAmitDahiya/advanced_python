#!/usr/bin/env python
# coding: utf-8

# In[5]:


# install and upgrade numpy library
get_ipython().system('pip install numpy --upgrade')


# In[23]:


#import numpy library
import numpy as np

#Define an numpy 1D array
first_numpy_array = np.array([1,2,3])

#print an array
first_numpy_array


# In[11]:


# Print 2D array
twoD_array = np.array([[1,2,2],[2,3,4]]) 

print(twoD_array)


# In[47]:


# 2d Float array
arr=np.array([1.2,1.2],[1.3,1.5])

# change the dtype to 'float64' 
arr = arr.astype('float64') 
  
# Print the array after changing 
# the data type 
print(arr) 


# In[44]:


# Get datatype of an array
b=np.array([1,1],[1,1])
print(b.dtype)


# In[48]:


# find array shape

b=np.array([1,2,3],[5,6,7])

print(dtype(b))


# In[26]:


#list ot numpy array

number=[1,2,3,4]
np.array(number)


# In[29]:


#create array with 0 values
array_with_zeros = np.zeros((3,4))
print(array_with_zeros)


# In[33]:


#crearte array_with one values
array_with_one_values = np.ones((3,4))
print(array_with_one_values)


# In[34]:


#crearte array_with one values as int
array_with_one_values = np.ones((3,4),dtype=np.int16)
print(array_with_one_values)


# In[38]:


#create empty array

create_empty_array=np.empty((2,3))
print(create_empty_array)


# In[39]:


#create idenety matrix

arrauy_eye = np.eye(3)
print(arrauy_eye)


# In[41]:


#array of even numbers
array_of_even_numbers = np.arange(2,21,2)

print(array_of_even_numbers)


# In[42]:


#array of odd numbers
array_of_even_numbers = np.arange(1,21,2)

print(array_of_even_numbers)


# In[ ]:




