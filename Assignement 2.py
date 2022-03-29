#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.What are the two values of the Boolean data type? How do you write them');get_ipython().run_line_magic('pinfo', 'them')

Two value of bookean data typs are following .
1.True
2.False 


# In[ ]:


get_ipython().set_next_input('2. What are the three different types of Boolean operators');get_ipython().run_line_magic('pinfo', 'operators')
Three different type of boolean operators ar following .

1. OR
2. AND
3 NOT 


# In[ ]:


3. Make a list of each Boolean operator's truth tables
(i.e. every possible combination of Boolean values for the operator and what it evaluate ).

or Truth table          and Truth Tables               not truth tables

1 or 1 = 1              1 and 1=1                       A      OUTPUT
1 or 0 = 1              1 and 0=0                       1  =     0
0 or 1 = 1              0 and 1=0                       0  =     1
0 or 0 = 0              0 and 0=0


# In[ ]:


get_ipython().set_next_input('4. What are the values of the following expressions');get_ipython().run_line_magic('pinfo', 'expressions')
(5 > 4) and (3 == 5)
not (5 > 4)
(5 > 4) or (3 == 5)
not ((5 > 4) or (3 == 5))
(True and True) and (True == False)
(not False) or (not True)


# In[2]:


(5 > 4) and (3 == 5)


# In[3]:


not (5 > 4)


# In[4]:


(5 > 4) or (3 == 5)


# In[5]:


not ((5 > 4) or (3 == 5))


# In[6]:


(True and True) and (True == False)


# In[9]:


(not False) or (not True)


# In[ ]:


get_ipython().set_next_input('5. What are the six comparison operators');get_ipython().run_line_magic('pinfo', 'operators')

Six comparison oprators are following .

> (grater than)
>=(greater than equal to)
< 
<=
==
get_ipython().system('=')


# In[ ]:


get_ipython().set_next_input('6. How do you tell the difference between the equal to and assignment operators');get_ipython().run_line_magic('pinfo', 'operators')
Describe a condition and when you would use one.

a=10( here i am assigning 10 to variable a)

a==10(here i am comparing "a" is equal to ten)


# In[ ]:


7. Identify the three blocks in this code:
spam = 0
if spam == 10: 
print('eggs')  - indentation error
if spam > 5:
print('bacon')-indentation error
else:
print('ham')-indentation error
print('spam')-indentation error
print('spam')-indentation error


# In[15]:


#8. Write code that prints Hello if 1 is stored in spam, prints Howdy if 2 is stored in spam, 
#and prints Greetings! if anything else is stored in spam.

spam=int(input())

if spam ==1:
    print ("Hello")
elif spam ==2:
    print("Howdy")
else: 
    print ("Greetings!")


# In[ ]:


get_ipython().set_next_input('9.If your programme is stuck in an endless loop, what keys you’ll press');get_ipython().run_line_magic('pinfo', 'press')

ans- interrupt the kernel 


# In[ ]:


get_ipython().set_next_input('10. How can you tell the difference between break and continue');get_ipython().run_line_magic('pinfo', 'continue')

break statement intrupt the ittration of loop and exit.

continue statement stop the current excution and pass the control to loop for next ittration .


# In[21]:


#11. In a for loop, what is the difference between range(10), range(0, 10), and range(0, 10, 1)?
range (10) and range (0,10) is same only in range (0,10) starting rang "0" is mentioned . 

range (0,10,1) in this jump of 1 is mentioned .


# In[23]:


#12. Write a short program that prints the numbers 1 to 10 using a for loop. 
#Then write an equivalent program that prints the numbers 1 to 10 using a while loop.

for i in range(1,11):
    print (i,end=" ")


# In[26]:


count=1
while count<=10:
    print (count,end=" ")
    count=1+count


# In[ ]:


get_ipython().set_next_input('13. If you had a function named bacon() inside a module named spam, how would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')
  
    This function can be called with spam.bacon().


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




