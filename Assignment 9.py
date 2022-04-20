#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1. To what does a relative path refer');get_ipython().run_line_magic('pinfo', 'refer')


# In[ ]:


Ans-A relative path refers to a location that is relative to a current directory


# In[ ]:


get_ipython().set_next_input('2. What does an absolute path start with your operating system');get_ipython().run_line_magic('pinfo', 'system')


# In[ ]:


Ans- An absolute path refers to the complete details needed to locate a file or folder, starting from the root element and ending with the other subdirectories. 
Absolute paths are used in websites and operating systems for locating files and folders.

example- "E:\ Prashant Destop\PRASHANT BUSINESS CARD.docx" is called absoulute path 


# In[ ]:


get_ipython().set_next_input('3. What do the functions os.getcwd() and os.chdir() do');get_ipython().run_line_magic('pinfo', 'do')


# In[ ]:


Ans- getcwd() : CWD stands for Current Working Directory.
    This function allows you to see what your current working directory is.
    
    os.chdir() method in Python used to change the current working directory to specified path. 
    It takes only a single argument as new directory path.


# In[ ]:


get_ipython().set_next_input('4. What are the . and .. folders');get_ipython().run_line_magic('pinfo', 'folders')


# In[ ]:


The . is a meta-location, meaning the folder you are currently in. 
The ..  is an indicator that you can move back from this location


# In[ ]:


get_ipython().set_next_input('5. In C:\\bacon\\eggs\\spam.txt, which part is the dir name, and which part is the base name');get_ipython().run_line_magic('pinfo', 'name')


# In[ ]:


Ans- C:\bacon\eggs is dir name and spam.txt is base name 


# In[ ]:


get_ipython().set_next_input('6. What are the three “mode” arguments that can be passed to the open() function');get_ipython().run_line_magic('pinfo', 'function')


# In[ ]:


Ans "r","w","r+" are the three mode which can pass to the open function as arguments


# In[ ]:


get_ipython().set_next_input('7. What happens if an existing file is opened in write mode');get_ipython().run_line_magic('pinfo', 'mode')


# In[ ]:


Ans- It will delete all written data. refer the below example.


# In[11]:


fs=open ("test1.txt","w")


# In[12]:


fs.write("Hello Ineuron team this is my 9th assignemnt ")


# In[13]:


fs.close ()


# In[14]:


fs=open("test1.txt","r")


# In[15]:


fs.read()


# In[16]:


df=open ("test1.txt","w")


# In[17]:


df=open("test1.txt","r")


# In[18]:


df.read()


# In[ ]:


8. How do you tell the difference between read() and readlines()?


# In[ ]:


ans- read () function read all lines together althouth readlines ()function change into list .refer the below example .


# In[20]:


df=open("prashant.txt","w")


# In[23]:


df.write("""What does iNeuron do?A product-driven organization working on state-of-the-art projects for 
         our domestic and international clients, carrying a lot of expertise in product development in the area of Computer vision, Deep learning, NLP, Auto ML and Machine learning with industry expertise in Warehousing, Security, Surveillance, Healthcare ...""")


# In[30]:


df.close ()


# In[31]:


df=open("prashant.txt","r+")


# In[32]:


df.read()


# In[35]:


df.close()


# In[36]:


df=open("prashant.txt","r+")


# In[38]:


af=df.readlines()


# In[39]:


type(af)


# In[ ]:


get_ipython().set_next_input('9. What data structure does a shelf value resemble');get_ipython().run_line_magic('pinfo', 'resemble')


# In[ ]:


Ans- A shelf value resembles a dictionary value; it has keys and values, along with keys() and values() methods that work similarly to the dictionary methods of the same names.

