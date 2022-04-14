#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. Is the Python Standard Library included with PyInputPlus');get_ipython().run_line_magic('pinfo', 'PyInputPlus')

ans- PyInputPlus is not a part of the Python Standard Library, so you must install it separately using Pip


# In[1]:


import pyinputplus as pyip


# In[ ]:


get_ipython().set_next_input('2. Why is PyInputPlus commonly imported with import pyinputplus as pypi');get_ipython().run_line_magic('pinfo', 'pypi')
ans- import pyinputplus as pyip so that you can enter a shorter name when calling the module's functions.


# In[ ]:


3. How do you distinguish between inputInt() and inputFloat()?
ans - inputInt return intiger value where as inputfloat return float value.


# In[ ]:


4. Using PyInputPlus, how do you ensure that the user enters a whole number between 0 and 99?
ans- Ans. In the inputint function we can set the min = 0 and max =99 to ensure user enters number between 0 and 99


# In[1]:


import pyinputplus as pyip


# In[3]:


inp = pyip.inputInt(prompt = "Enter an Integer... ", 
                    default = 0, timeout = 2)


# In[6]:


inp = pyip.inputInt(prompt = "Enter an Integer... ", 
                    default = 0, timeout = 2)


# In[ ]:


get_ipython().set_next_input('5. What is transferred to the keyword arguments allowRegexes and blockRegexes');get_ipython().run_line_magic('pinfo', 'blockRegexes')

We can also use regular expressions to specify whether an input is allowed or not. 
The allowRegexes and blockRegexes keyword arguments take a list of regular expression strings to determine 
the PyInputPlus function will accept or reject as valid input.


# In[ ]:


get_ipython().set_next_input('6. If a blank input is entered three times, what does inputStr(limit=3) do');get_ipython().run_line_magic('pinfo', 'do')

ans-It will throw RetryLimitException exception.


# In[ ]:


get_ipython().set_next_input("7. If blank input is entered three times, what does inputStr(limit=3, default='hello') do");get_ipython().run_line_magic('pinfo', 'do')
ans-When you use limit keyword arguments and also pass a default keyword argument, 
the function returns the default value instead of raising an exception


# In[8]:


response = pyip.inputStr(limit=3,default='hello')


# In[9]:


response


# In[ ]:




