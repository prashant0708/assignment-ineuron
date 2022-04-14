#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input("1. What does an empty dictionary's code look like");get_ipython().run_line_magic('pinfo', 'like')


# In[1]:


d={}


# In[2]:


type(d)


# In[ ]:


2. What is the value of a dictionary value with the key 'foo' and the value 42?


# In[3]:


d={'foo':42}


# In[4]:


d


# In[5]:


d.keys()


# In[6]:


d.values()


# In[ ]:


get_ipython().set_next_input('3. What is the most significant distinction between a dictionary and a list');get_ipython().run_line_magic('pinfo', 'list')
ans- A list is an ordered sequence of objects, whereas dictionaries are unordered object. 
the significant difference is that items in dictionaries are accessed via keys and in list access by  their position.


# In[ ]:


4. What happens if you try to access spam['foo'] if spam is {'bar': 100}?
ans - it will show key error as shown below.


# In[7]:


spam={'bar':100}


# In[8]:


spam['foo']


# In[ ]:


5. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.keys()?

'cat' in spam checks whether there is a 'cat' value in the dictionary, while 'cat' in spam.keys() checks 
whether there is a value 'cat' for one of the value in spam.


# In[ ]:


6. If a dictionary is stored in spam, what is the difference between the expressions 'cat' in spam and 'cat' in spam.values()?


# In[ ]:


'cat' in spam checks whether there is a 'cat' key in the dictionary, while 'cat' in spam.values() checks 
whether there is a value 'cat' for one of the keys in spam.


# In[ ]:


get_ipython().set_next_input('7. What is a shortcut for the following code');get_ipython().run_line_magic('pinfo', 'code')
if 'color' not in spam:
spam['color'] = 'black'


# In[9]:


spam=["red","yellow","white","green"]


# In[11]:


"color" in spam


# In[15]:


spam[3]="balck"


# In[16]:


spam


# In[ ]:


get_ipython().set_next_input('8. How do you "pretty print" dictionary values using which module and function');get_ipython().run_line_magic('pinfo', 'function')

ans - I feel given question is not clear , so there is two possibility 
first - if "pretty print "  is value of dictinoary how to acess it , we can access by variable.values()
second- how to assigne "pretty print" to dictinoary as value - we can pass assign the "pretty print " by d={"k1":"pretty print "}

