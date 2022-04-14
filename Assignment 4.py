#!/usr/bin/env python
# coding: utf-8

# In[ ]:


1. What exactly is []?

ans- empty value list


# In[ ]:


2. In a list of values stored in a variable called spam, how would you assign the value 'hello' as the third value? 
(Assume [2, 4, 6, 8, 10] are in spam.)


# In[1]:


spam=[2, 4, 6, 8, 10]


# In[3]:


spam.insert(3,"hello")


# In[4]:


spam


# In[ ]:


Let's pretend the spam includes the list ['a', 'b', 'c', 'd'] for the next three queries.


# In[5]:


spam=['a', 'b', 'c', 'd']


# In[ ]:


3. What is the value of spam[int(int('3' * 2) / 11)]?


# In[6]:


spam[int(int('3' * 2) / 11)]


# In[ ]:


4. What is the value of spam[-1]?


# In[10]:


spam[-1]


# In[ ]:


5. What is the value of spam[:2]?


# In[11]:


spam[:2]


# In[ ]:


Let's pretend bacon has the list [3.14, 'cat,' 11, 'cat,' True] for the next three questions.

#note: given list is not in the formate to excute example 'cat,'11,- it is wrong way to write.hecne i have corrected it .


# In[15]:


bacon=[3.14, 'cat', 11, 'cat', True]


# In[ ]:


6. What is the value of bacon.index('cat')?


# In[16]:


bacon.index('cat')


# In[ ]:


get_ipython().set_next_input('7. How does bacon.append(99) change the look of the list value in bacon');get_ipython().run_line_magic('pinfo', 'bacon')


# In[17]:


bacon.append(99)


# In[18]:


bacon


# In[ ]:


get_ipython().set_next_input("8. How does bacon.remove('cat') change the look of the list in bacon");get_ipython().run_line_magic('pinfo', 'bacon')


# In[19]:


bacon.remove('cat')


# In[20]:


bacon


# In[ ]:


get_ipython().set_next_input('9. What are the list concatenation and list replication operators');get_ipython().run_line_magic('pinfo', 'operators')
ans- list concatenation add two list together , list replicator operators repeate the list as many time as we want example l*3 
where list l reperat 3 times 


# In[21]:


l=[1,2,3,4,5,6,7]
l2=[34,"prashant",6+78j,"sudh","ineuron"]


# In[22]:


l1=l+l2


# In[23]:


l1


# In[25]:


l*3 # example of list replication


# In[ ]:


10. What is difference between the list methods append() and insert()?
ans- append oprator add the data at the end of the list index whereas insert operator add the data in list as specified index .

example l=[10,23]
          l.append(24) it mean 24 will add to list after 23 
          l.insert(0,24)it mean 24 will add at zero index.


# In[ ]:


get_ipython().set_next_input('11. What are the two methods for removing items from a list');get_ipython().run_line_magic('pinfo', 'list')
ans- pop and remove 


# In[35]:


l=[3,4,5,6,7,8,"prash","inuron"]


# In[36]:


l.pop(3)


# In[37]:


l


# In[39]:


l.remove("prash")


# In[40]:


l


# In[ ]:


12. Describe how list values and string values are identical.
Ans- The similarity between Lists and Strings in Python is that both are sequences. 
The differences between them are that firstly, Lists are mutable but Strings are immutable. 
Secondly, elements of a list can be of different types whereas a String only contains characters that are all of String type.


# In[ ]:


get_ipython().set_next_input("13. What's the difference between tuples and lists");get_ipython().run_line_magic('pinfo', 'lists')
ans-The key difference between tuples and list is tuples are immutable and lits are mutable .


# In[ ]:


14. How do you type a tuple value that only contains the integer 42?


# In[45]:


t=(42,)


# In[46]:


type(t)


# In[ ]:


get_ipython().set_next_input("15. How do you get a list value's tuple form? How do you get a tuple value's list form");get_ipython().run_line_magic('pinfo', 'form')


# In[47]:


alif=[3,4,5,6,7,8,"prash","inuron"]


# In[48]:


type(alif)


# In[50]:


altaf=tuple(alif)


# In[51]:


type(altaf)


# In[52]:


altaf


# In[53]:


alif=list(altaf)


# In[54]:


type(alif)


# In[55]:


alif


# In[ ]:


get_ipython().set_next_input('16. Variables that "contain" list values are not necessarily lists themselves. Instead, what do they contain');get_ipython().run_line_magic('pinfo', 'contain')
"contain" in square brackets with tail comma chnage the variable into list, we assigne "contain" dirctly to variable , the type of variable will be str.


# In[60]:


p=["contain",] 


# In[61]:


type(p)


# In[ ]:


17. How do you distinguish between copy.copy() and copy.deepcopy()?
A copy. copy means constructing a new collection object and then populating 
it with references to the child objects found in the original.
Deep copy is a process in which the copying process occurs recursively. 
It means first constructing a new collection object and then recursively populating 
it with copies of the child objects found in the original.

