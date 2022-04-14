#!/usr/bin/env python
# coding: utf-8

# In[ ]:


get_ipython().set_next_input('1.Why are functions advantageous to have in your programs');get_ipython().run_line_magic('pinfo', 'programs')
Ans- It avoide the repeatability of the code and we can pass n times of arguments with
same function no need to write seperate logic for each arguemnts.


# In[ ]:


get_ipython().set_next_input("2. When does the code in a function run: when it's specified or when it's called");get_ipython().run_line_magic('pinfo', 'called')
Ans- after writing return


# In[ ]:


get_ipython().set_next_input('3. What statement creates a function');get_ipython().run_line_magic('pinfo', 'function')
Ans- def is the statement create function 

def area_of_circle(r):
  a=3.14*(r**2)
  return a

def area_of_circle(r):
  a=3.14*(r**2)
  return a

area_of_circle(23)


# In[ ]:


get_ipython().set_next_input('4. What is the difference between a function and a function call');get_ipython().run_line_magic('pinfo', 'call')
Ans- Function is define to do some particular task and function call is nothing but to call function to perform 
the predefine task.
#example to add two number we define function but for adding two number we have to call function and pass the two number to add. 


# In[ ]:


5. How many globel scope in python and how many local scope ? 
ans- There is only one globel scope per execution of program . 
      Local scope variables can only be accessed within its block.


# In[ ]:


get_ipython().set_next_input('6. What happens to variables in a local scope when the function call returns');get_ipython().run_line_magic('pinfo', 'returns')
A  variable becomes undefined after the function call completes 


# In[ ]:


get_ipython().set_next_input('7. What is the concept of a return value? Is it possible to have a return value in an expression');get_ipython().run_line_magic('pinfo', 'expression')
Ans- Return concept send the value to the user define function , yes it is possible to return the value as an expression.


# In[ ]:


get_ipython().set_next_input('8. If a function does not have a return statement, what is the return value of a call to that function');get_ipython().run_line_magic('pinfo', 'function')
Ans- if we don't use return statment , we can use print function to call the function .


# In[ ]:


get_ipython().set_next_input('9. How do you make a function variable refer to the global variable');get_ipython().run_line_magic('pinfo', 'variable')
ans- by modular codding we can make function variable to globel variable . 

example writing a function in one module  we can import same module in infinite time to perform the task. 


# In[ ]:


get_ipython().set_next_input('10.10. What is the data type of None');get_ipython().run_line_magic('pinfo', 'None')
ans- print function privide the None data type and we can't use same data for next execution . 
None is an object and it's class of variable called none data type.


# In[ ]:


get_ipython().set_next_input('11. What does the sentence import areallyourpetsnamederic do');get_ipython().run_line_magic('pinfo', 'do')

it will import a module name areallyourpetsnamederic


# In[ ]:


get_ipython().set_next_input('12.If you had a bacon() feature in a spam module, what would you call it after importing spam');get_ipython().run_line_magic('pinfo', 'spam')
ans- After importing spam module , i will call bacan as fundtion 

import spam 

x=spam.bacon()

or from spam import bacon 


# In[ ]:


get_ipython().set_next_input('13. What can you do to save a programme from crashing if it encounters an error');get_ipython().run_line_magic('pinfo', 'error')
ans - we can use error handling and logging method to save it from crashing . 


# In[ ]:


get_ipython().set_next_input('14. 14. What is the purpose of the try clause? What is the purpose of the except clause');get_ipython().run_line_magic('pinfo', 'clause')
ans- try and except is exception handling block , if there is any error in the programe except clause will read after encontered by try block . 

example : 
          
         def add(a,b):
                try:
                    div=a/b
                except Exception as e:
                    print ("you have entered b less then zero",e)
                
in above code if we assign b value <0 it will throw error which will encounter by the exception handling block try and exception .

