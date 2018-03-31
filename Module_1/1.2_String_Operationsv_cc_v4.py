
# coding: utf-8

#  <div class="alert alert-block alert-info" style="margin-top: 20px">
#  <a href="http://cocl.us/NotebooksPython101"><img src = "https://ibm.box.com/shared/static/yfe6h4az47ktg2mm9h05wby2n7e8kei3.png" width = 750, align = "center"></a>
# 
# 
# 
# 
# 

# <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# <h1 align=center><font size = 5>String Operations </font></h1>

# <br>

# ## Table of Contents
# 
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# <li><a href="#ref0">Strings</a></li>
# <li><a href="#ref1">Indexing</a></li>
# <li><a href="#ref2">Escape Sequences </a></li>
# <li><a href="#ref3">String Operations</a></li>
# <li><a href="#ref4">Quizz </a></li>
# <br>
# <p></p>
# Estimated Time Needed: <strong>15 min</strong>
# </div>
# 
# <hr>

# <a id="ref0"></a>
# <h2 align=center>Strings </h2>

#  A string is contained within two quotes:

# In[1]:

"Michael Jackson"


# You can also use single  quotes:

# In[2]:

'Michael Jackson'


# A string can be spaces, digits:

# In[3]:

'1 2 3 4 5 6 '


# A String can also be special characters : 

# In[4]:

'@#2_#]&*^%$'


# we can print out string using the print statement:

# In[5]:

print("hello!")


# We can bind or assign a string to another variable 
# 

# In[6]:

Name= "Michael Jackson"
Name


#  <a id="ref1"></a>
# <h2 align=center>Indexing </h2>

# its is helpful to think of a string as an ordered sequence. each element in the sequence can be accessed using an index represented by the array of numbers  

#  <img src = "https://ibm.box.com/shared/static/esdu9w118rm1aldff7ff8c9b3kpjdazc.png" width = 600, align = "center"></a>

#  the first index can be accessed as follows:

# In[7]:

print(Name[13])


#  we can access index 6

# In[8]:

print(Name[6])


# moreover, we can access the 13 th index

# In[9]:

print(Name[13])


#  We can also use negative indexing with strings:

# <img src = "https://ibm.box.com/shared/static/rmq8akevtt6uufox3xai7q2kqs4j9kan.png" width = 600, align = "center"></a>

#  the last element is given by the  index -1  

# In[10]:

print(Name[-1])


#  the first element can be obtained by  index -15 

# In[11]:

print(Name[-15])


#  we can find the number of characters is a string using len short for length

# In[12]:

len("Michael Jackson")


# We can obtain multiple characters from a string using slicing, we can obtain the 0-th to 4-th and 8-th to the 12-th element  

#  <img src="https://ibm.box.com/shared/static/bva43bmp00cxeunqh4w7blkgniycbign.png" width=600,align="center"></a>
# 
# 

# In[13]:

Name[0:4]


# In[15]:

Name[8:12]
print (Name[8:12])


#  We can also  input a stride value as follows  the 2 indicates  we select every second variable

#  <img src="https://ibm.box.com/shared/static/f49xvym409rxclhtbr30xrs9kc4l5419.png" width=600,align="center"></a>
# 
# 

# In[16]:

Name[::2]
print (Name[::2])


# We can also incorporate slicing  with the stride in this case, we select the first five elements then use the stride 

# In[17]:

Name[0:5:2]
print (Name[0:5:2])


# In[ ]:




# We can concatenate or combine strings we use the addition symbols, the result is a new string that is a combination of both 
# 

# In[18]:

Statement = Name + "is the best"
Statement


#  We can replicate values of a string  we simply multiply the string by the number of times we would like to replicate it, In this case, three. The result is a new string,the new string consists of three copies of the original string.
# 

# In[19]:

3*"Michael Jackson "


# You can create a new string by setting it to the original variable and concatenated  with a new string the result is a new string  that changes from  Michael Jackson to “Michael Jackson is the best.
# 

# In[20]:

Name= "Michael Jackson"
Name= Name+" is the best"
Name


#  <a id="ref2"></a>
# <h2 align=center>Escape Sequences  </h2>

# Back slashes represent the beginning  of escape sequences escape sequences represent strings that may be difficult to input. For example, back slashes "n" represent a new line. The output is given by a nee line after the back slashes "n” is encountered.
# 

# In[21]:

print(" Michael Jackson \n is the best" )


# Similarly, back slash  "t" represents a tab 

# In[22]:

print(" Michael Jackson \t is the best" )


#  If you want to place a back slash in your string use a double back slash:

# In[23]:

print(" Michael Jackson \\ is the best" )


#  We can also place an r before the string to read the to read the backslash 

# In[25]:

print(r" Michael Jackson \ is the best" )


# <a id="ref3"></a>
# <h2 align=center>String Operations</h2>

# There are many string operation methods in Python that can be used to manipulate the data. We are going to use some basic string operations on the dats 
# 
# 

# Let's try with the method upper; this method converts upper case characters to lower case characters

# In[ ]:

A="Thriller is the sixth studio album"
print("befor upper:",A)
B=A.upper()
print("After upper:",B)


# <br>

# The method replaces a segment of the string i,e a substring  with a new string. We input the part of the string we would like to change  the second argument is what we would like to exchange the segment with the result is a new string with the segment changed. 
# 

# In[ ]:

A="Michael Jackson is the best"
B=A.replace('Michael', 'Janet')
B


# The method "find" finds sub-strings, the argument is the substring you would like to find, the output is the first index of the sequence. We can find the sub-string "jack" or "el".  
# 

#  <img src="https://ibm.box.com/shared/static/mc414goh1l8jfo9gb19yibuylk8zk7dh.png" width=600,align="center"></a>

# In[ ]:

Name="Michael Jackson"
Name.find('el')


# In[ ]:

Name.find('Jack')


# If the  sub-string is not in the string the output is negative one. For example, the string 'Jasdfasdasdf' is not a substring. 

# In[ ]:

Name.find('Jasdfasdasdf')


#  <a id="ref4"></a>
# <h2 align=center> Quiz on Strings </h2>

# ##### What is the value of the variable A after the following code is executed? 
# A="1"

# In[ ]:

#1


#  <div align="right">
# <a href="#String1" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String1" class="collapse">
# ```
# "1"
# ```
# </div>
# 

# #### What is the value of the variable B after the following code is executed?
# `B="2"`

# In[ ]:

#2


# <div align="right">
# <a href="#String2" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String2" class="collapse">
# ```
# "2"
# ```
# </div>

# #### What is the value of the variable C after the following code is executed?
# `C=A+B`

# In[ ]:

#12


#  <div align="right">
# <a href="#String3" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String3" class="collapse">
# ```
# "12"
# ```
# </div>

# #### Consider the variable D, use slicing to print out the first three elements ?
# 

# In[ ]:

D="ABCDEFG"


# In[ ]:

print (D[:3])


#  <div align="right">
# <a href="#String4" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String4" class="collapse">
# ```
# "print(D[:3]) or print(D[0:3])"
# ```
# </div>

# #### Use a stride value of 2 to print out every second character  of the string E ?

# In[ ]:

E='clocrkr1e1c1t'


# In[ ]:

print (E[::2])


# <div align="right">
# <a href="#String6" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String6" class="collapse">
# ```
# "print(E[::2])"
# ```
# </div>

# #### Print out a backslash ?

# In[ ]:

print ('Hi \\everyone')


# <div align="right">
# <a href="#String7" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String7" class="collapse">
# ```
# print(" \\" )
# or
# print(r" \ " )
# ```
# </div>

# #### Convert the variable F to uppercase  ?

# In[ ]:

F="You are wrong"


# In[ ]:

x = F.upper()
print (x)


#  <div align="right">
# <a href="#String8" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String8" class="collapse">
# ```
# F.upper()
# ```
# </div>

# #### Consider the variable G, find the first index of the sub-string snow ?

# In[ ]:

G="Mary had a little lamb Little lamb, little lamb Mary had a little lamb Its fleece was white as snow And everywhere that Mary went Mary went, Mary went Everywhere that Mary went The lamb was sure to go"


# In[ ]:

g.find('snow')
print (g.find('snow'))


#  <div align="right">
# <a href="#String9" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String9" class="collapse">
# ```
# G.find('snow')
# ```
# </div>

# #### In the variable G replace the sub-string Mary with "Bob"? 

# In[ ]:

G.replace('Mary', 'Bob')


#  <div align="right">
# <a href="#String10" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="String10" class="collapse">
# ```
# G.replace("Mary","Bob")
# ```
# </div>

# #### Hi Joseph here, check out my other course Data Analysis with Python, just click the image below:
# <a href="http://cocl.us/PY0101ENtoDA0101EN"><img src = "https://ibm.box.com/shared/static/1msv7g4ovv35c2eb97gsp45gdm833eqz.png" width = 300, align = "center"></a>

# #### Enjoying Python? Think ahead about what you might want to use in the future.
# If you're looking for a enterprise-ready environment to use Python on a big scale with two free Apache Spark executors, consider signing up for a free account on [Data Science Experience](http://cocl.us/NotebooksPython101bottom)

# # About the Authors:  
# 
#  [Joseph Santarcangelo]( https://www.linkedin.com/in/joseph-s-50398b136/) has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 

# In[ ]:



