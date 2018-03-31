
# coding: utf-8

# <div class="alert alert-block alert-info" style="margin-top: 20px">
#  <a href="http://cocl.us/NotebooksPython101"><img src = "https://ibm.box.com/shared/static/yfe6h4az47ktg2mm9h05wby2n7e8kei3.png" width = 750, align = "center"></a>

# <img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 200, align = "center">
# 
# 
# 
# <h1 align=center><font size = 5>Python - Writing Your First Python Code!</font></h1> 

# # Welcome!
# 
# By the end of this notebook, you will have learned the basics of Python, including writing some basic commands, understanding object types, and some simple operations!  

# # Table of Contents
# 
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <li><a href="#ref0">First Program in Python</a></li>
# <li><a href="#ref1">Object Types  </a></li>
# <li><a href="#ref2">Expressions and Variables</a></li>
# 
# <br>
# <p></p>
# Estimated Time Needed: <strong>25 min</strong>
# </div>
# 
# <hr>

#  <a id="ref0"></a>
# <h2 align=center>Your First Program in Python </h2> 

# A statement or expression is an instruction the computer will run or execute. Perhaps the simplest program you can write is to print a statement in Python.

# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# **Tip**: To *execute* the Python code in the grey code cell below, **click on it and press Shift + Enter**.
# </div>

# In[1]:

print('Hello World!')


# After executing the cell above, you should see that Python return the string, `Hello Python 101`. Congratulations on running your first Python code!

# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# **Tip:** **`print()`** is the **function** that you **executed**, and you *passed in* an **argument** of `'Hello World!'`.
# </div>
# 

# ### Python 3

# How do we know that Python 3 is running? Take a look in the top-right hand corner of this notebook. You should see "Python 3"!

# ### Writing comments in Python

# In addition to writing code, note that it is customary to comment your code to help describe what it does. Not only does this help **other people** understand your code, it can also serve as a _reminder_ **to you** of what your code does. (This is especially true when you write some code and then come back to it weeks or months later.)
# 
# To write comments in your Python code, use the hash symbol (#) before writing your comment. When you run the code Python will ignore everything after the # in that line.

# In[2]:

print('Hello Python 101') #this my comment
#print('Hi')


# Great! After executing the cell above, you should notice that **"this is my comment** did not appeared in the output, because it was a comment (and thus ignored by Python). 
# The second line was also not executed because `print('Hi')` was preceded by a hash symbol (#) as well!

# ### Errors in Python

# Before continuing, it's important to note when things go wrong in Python, and we cause **errors**.

# There are many kinds of errors, and you **do not need to memorize the various types of errors**. Instead, what's most important is know **what the error messages mean**.
# 
# For example, if you spell **print** as **frint**, you will get an error message.

# In[3]:

frint("Hello World!")


# The error message tells you (1) where the error occurred, and (2) what kind of error it was. Here, Python attempted to run the function `frint`, but could not determine what `frint` -- since it is _undefined_.

# ### Does Python know the error in the script before you run it?
# No, Python is naive! Python will try to run the code line-by-line, and it will stop if it runs into an error.

# In[4]:

print("This will be printed")
frint("This will cause an error")
print("This will NOT be printed")


# More on errors later on in this course!

# ### Exercise: Your First Program

# #### Using the `print()` function, print out the phrase: "hello world"

# In[5]:

# Write your code below and press Shift+Enter to execute 
print ('Hello World of Python!')




# <div align="right">
# <a href="#1" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="1" class="collapse">
# ```
# print("hello world!")
# ```
# </div>

# #### Print out the phrase: "Hello World"  and comment it with the phrase "printing Hello World" _all in one line of code_

# In[6]:

# Write your code below
print ('HelloWorld!')#printing hello world!




#  <div align="right">
# <a href="#2" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="2" class="collapse">
# ```
# print("Hello World") #print Hello World
# ```
# </div>

# <a id="ref1"></a>
# <h2 align=center> Types of objects in Python </h2>

# You can have many different object types in Python, let's start with **strings**, **integers** and **floats**. Anytime you write words (text) in Python, you're using character **strings** (strings for short). Numbers, on the other hand, depend: numbers can be **integers** (like -1, 0, 100) or **floats**, which are real numbers (like 3.14, -42.0).

#  <img src = "https://ibm.box.com/shared/static/8zp0t4oh7kuzleudrszhkqukcup1708f.png" width = 600, align = "center"></a>

# The following chart summarizes three data types for the last examples,  the first column indicates the expression  the second column indicates the data type
# 

# In[ ]:

11 #integer


# In[ ]:

2.14 #float


# In[ ]:

"Hello Python 101" #character string


#  We can see the actual data type in python by using the **`type()`** command

# In[ ]:

type(12)


# In[ ]:

type(2.14)


# In[ ]:

type("Hello Python 101")


# #### Using the `type()` function, check the object type of `12.0`?

# In[7]:

# Write your code below
type(12.0)




# ### Integers

# Here are some integers, integers  can be negative or positive:
# 

# <img src = "https://ibm.box.com/shared/static/19iqm3q5pvxzuwa22d5ihxcr6eftjl48.png" width = 600, align = "center"></a>

# We can verify some of the above examples using the type command:

# In[8]:

type(-1)


# In[9]:

type(4)


# In[10]:

type(0)


# ### Floats 

#  Floats are real numbers; they include the integers but also "numbers in-between the integers". Consider the numbers between  0 and one we can select numbers in-between them, these numbers are floats. Similarly, consider the numbers between 0.5 and 0.6. We can select numbers in-between them, these are floats as well. We can continue the process, zooming in for different numbers, of course, there is a limit, but it is quite small.

#  We can verify some of the above examples using the type command:

# In[11]:

type(1.0)


# In[12]:

type(0.5)


# In[13]:

type(0.56)


# ### Converting from one object type to a different object type

# You can change the type of the object in Python; this is called typecasting. For example, you can convert an integer into a float, as in 2 to 2.0.

# In[14]:

type(2) #verify that this is an integer


# #### Converting to float:

# In[15]:

float(2)


# In[16]:

type(float(2))


# #### Converting to integer:

#  Nothing really changes. If you cast a float to an integer, you must be careful. For example, if you cast the float 1.1 to 1 you will lose some information : 

# In[17]:

int(1.1)


# #### Converting from strings to integers/floats:

# If a string contains an integer value, you can convert it to an integer:

# In[18]:

int('1')


# You can also convert strings containing float values into float objects

# In[19]:

float('1.2')


# However, if we attempt to convert a string that contains a non-numerical value, we get an error:

# In[20]:

int("A")


# #### Converting to strings:

# You can convert an int to a string:

# In[21]:

str(1)


#  You can convert a  float to a string 

# In[22]:

str(1.2)


# ### Boolean 

# Boolean is another important  type in Python; a Boolean can take on two values. The first value is true, just remember we use an uppercase T:

# In[ ]:

True


#  Boolean values can also be false, with  an uppercase F:

# In[ ]:

False


# Using the type command on a Boolean value we  obtain the term bool, this is short for Boolean 

# In[23]:

type(True)


# In[ ]:

type(False)


# If we cast a Boolean true to an integer or float we will get a 1, if we cast a Boolean false to an integer or float. If we get a zero   if you cast a 1 to a boolean, you get a true similarly, if you cast a 0 to a Boolean you get a false. 

# In[24]:

int(True)


# In[25]:

bool(1)


# In[27]:

bool(0)


# In[ ]:

float(True)


# ### Quiz on types  

# #### What is the type of the result of: `6 / 2`

# In[28]:

6/2


#  <div align="right">
# <a href="#3" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="3" class="collapse">
# ```
# the type if float 
# type(6/2)
# ```
# </div>

# #### What is the type of the result of: `6 // 2`? (Note the double slash //)

# In[29]:

# type is int
6//2


#  <div align="right">
# <a href="#4" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="4" class="collapse">
# ```
# int:
# double slashes stand for integer division 
# 
# 
# ```
# </div>

# <a id="ref2"></a>
# <h2 align=center> Expression and Variables </h2>
# 
# 

# ### Expressions 

# Expressions are operations that Python performs. For example, basic arithmetic operations like adding multiple numbers.

# In[30]:

43 + 60 + 16 + 41


#  We can perform operations such as subtraction using the subtraction sign. In this case the result is a negative number.

# In[31]:

50 - 60


# We can use multiplication using an asterisk:

# In[32]:

5 * 5


# We can also perform division with the forward slash

# In[33]:

25 / 5


# In[ ]:

25 / 6


# We can use the double slash for integer division, where the result is rounded 

# In[34]:

25//5


# In[35]:

25//6


# **What is 160 min in hours?**

# In[37]:

total_hours = 160/60
total_hours


#  <div align="right">
# <a href="#6" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="6" class="collapse">
# ```
# 160.0 / 60.0
# ```
# </div>

#  Python follows mathematical conventions when performing mathematical expressions. The following operations are in different order. In both cases Python performs multiplication, then addition to obtain the final result. 

# In[ ]:

2 * 60 + 30


#  The expressions in the parentheses are performed first. We then multiply the result by 60, the result is 1920.

# In[ ]:

(30 + 2) * 60


# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# <h4> [Tip] Summary  </h4>
# <p></p>
# You can do a variety of mathematical operations in Python including:  
# <li> addition: **2 + 2** </li>
# <li> subtraction: **5 - 2** </li>
# <li> multiplication: **3 \* 2** </li>
# <li> division: **4 / 2** </li>
# <li> exponentiation: **4 \*\* 2** </li>
# </div>

# ### Variables

# We can also **store** our output in **variables**, so we can use them later on. For example:

# In[ ]:

x = 43 + 60 + 16 + 41


# To return the value of **`x`**, we can simply run the variable as a command:

# In[40]:

x


# We can also perform operations on **`x`** and save the result to a **new variable**:

# In[ ]:

y = x / 60
y


# If we save something to an **existing variable**, it will **overwrite** the previous value:

# In[41]:

x = x / 60
x


# It's good practice to use **meaningful variable names**, so you don't have to keep track of what variable is what:

# In[42]:

total_min = (43 + 42 )
total_min


# In[43]:

total_hr = total_min / 60  
total_hr


# You can put this all into a single expression, but remember to use **round brackets** to add together the album lengths first, before dividing by 60.

# In[ ]:

total_hr = (43 + 42 + 57) / 60  # get total hours in a single expression
total_hr


# <hr></hr>
# <div class="alert alert-success alertsuccess" style="margin-top: 0px">
# <h4> [Tip] Variables in Python </h4>
# <p></p>
# As you just learned, you can use **variables** to store values for repeated use. Here are some more **characteristics of variables in Python**:
# <li>variables store the output of a block of code </li>
# <li>variables are typically assigned using **=** (as in **x = 1**) </li>
# <p></p>
# </div>
# <hr></hr>

#  <a id="#ref1a"></a>
# <h2 align=center> Quiz on Expression and Variables in Python</h2>

# ####  What is the value of x ? <p> x = 3 + 2 * 2</p>

# In[44]:

# 7
x = 3 + 2 * 2


# <div align="right">
# <a href="#SM1" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="SM1" class="collapse">
# ```
# 7
# ```
# </div>
# 

# ####  What is the value of y ? <p> y = (3 + 2) * 2</p>

# In[ ]:

# 10


# <div align="right">
# <a href="#SM2" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="SM2" class="collapse">
# ```
# 10
# ```
# </div>
# 

# #### What is the value of z ? <p> z = x + y</p>

# In[ ]:

# 17


# <div align="right">
# <a href="#SM3" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="SM3" class="collapse">
# ```
# 17
# ```
# </div>

# In[ ]:




# ### Hi Joseph here, check out my other course Data Analysis with Python, just click the image below:
# <a href="http://cocl.us/PY0101ENtoDA0101EN"><img src = "https://ibm.box.com/shared/static/1msv7g4ovv35c2eb97gsp45gdm833eqz.png" width = 300, align = "center"></a>

# ### Enjoying Python? Think ahead about what you might want to use in the future.
# If you're looking for a enterprise-ready environment to use Python on a big scale with two free Apache Spark executors, consider signing up for a free account on [Data Science Experience](http://cocl.us/NotebooksPython101bottom)

# <hr></hr>
# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# <h4> [Tip] Saving the Notebook </h4>  
# 
# Your notebook saves automatically every two minutes. You can manually save by going to **File** > **Save and Checkpoint**. You can come back to this notebook anytime by clicking this notebook under the "**Recent Notebooks**" list on the right-hand side.   
# 
# 
# </div>
# <hr></hr>
# <div class="alert alert-success alertsuccess" style="margin-top: 20px">
# <h4> [Tip] Notebook Features </h4>  
#   
# Did you know there are other **notebook options**? Click on the **>** symbol to the left of the notebook:
# 
# <img src =https://ibm.box.com/shared/static/otu40m0kkzz5hropxah1nnzd2j01itom.png width = 35%>
# 
# 
# <p></p>
# 
# </div>
# <hr></hr>

# <hr>
# Copyright &copy; 2017 IBM Cognitive Class. This notebook and its source code are released under the terms of the [MIT License](https://cognitiveclass.ai/mit-license/).

# ### About the Authors:  
# 
# 
#  [Joseph Santarcangelo](https://www.linkedin.com/in/joseph-s-50398b136/) is a Data Scientist at IBM, and holds a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 
# 
# 
