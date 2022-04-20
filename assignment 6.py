#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are escape characters, and how do you use them');get_ipython().run_line_magic('pinfo', 'them')


# In[ ]:


Ans-To insert the character into the string we escape characters with backslash  


# In[10]:


text="we are learning data science  from \"Ineuron\" which is very good instituation"


# In[11]:


text


# In[ ]:


get_ipython().set_next_input('2. What do the escape characters n and t stand for');get_ipython().run_line_magic('pinfo', 'for')


# In[ ]:


Ans-Escape character n stand for new line and t stand for tab 


# In[ ]:


get_ipython().set_next_input('3. What is the way to include backslash characters in a string');get_ipython().run_line_magic('pinfo', 'string')


# In[ ]:


Ans - backslash include in the string with \"\"
example-text="we are learning data science  from \"Ineuron\" which is very good instituation"


# In[ ]:


4. The string "Howl's Moving Castle"  is a correct value. Why isn't the single quote character in the
word Howl's  not escaped a problem? 


# In[ ]:


Ans- The single quote in Howl's is fine because we have  used double quotes at the beginning and end of the string


# In[ ]:


get_ipython().set_next_input("5. How do you write a string of newlines if you don't want to use the n character");get_ipython().run_line_magic('pinfo', 'character')


# In[14]:


Ans- print ("Hello",end=" \welcome to India")


# In[ ]:


get_ipython().set_next_input('6. What are the values of the given expressions');get_ipython().run_line_magic('pinfo', 'expressions')
'Hello, world!'[1]
'Hello, world![0:5]
'Hello, world!'[:5]
'Hello, world!'[3:]


# In[16]:


'Hello, world!'[1]


# In[18]:


'Hello, world!'[0:5]


# In[19]:


'Hello, world!'[:5]


# In[20]:


'Hello, world!'[3:]


# In[ ]:


get_ipython().set_next_input('7. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
'Hello'.upper()
'Hello'.upper().isupper()
'Hello'.upper().lower()


# In[21]:


'Hello'.upper()


# In[22]:


'Hello'.upper().isupper()


# In[23]:


'Hello'.upper().lower()


# In[ ]:


get_ipython().set_next_input('8. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
'Remember, remember, the fifth of July.'.split()
'-'.join('There can only one.'.split())


# In[26]:


'Remember , remember, the fifth of July.'.split()


# In[27]:


'-'.join('There can only one.'.split())


# In[ ]:


get_ipython().set_next_input('9. What are the methods for right-justifying, left-justifying, and centering a string');get_ipython().run_line_magic('pinfo', 'string')


# In[ ]:


Ans- Method for right-justifying is rjust 
     method for left-justifing is ljust
     method for centering is center 
        
example are below 


# In[ ]:


get_ipython().set_next_input('10. What is the best way to remove whitespace characters from the start or end');get_ipython().run_line_magic('pinfo', 'end')


# In[ ]:


Ans- To remove whitespace characters from the beginning or from the end of a string only, 
you use the trimStart() or trimEnd() method.

