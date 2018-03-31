
# coding: utf-8

#  <div class="alert alert-block alert-info" style="margin-top: 20px">
#  <a href="http://cocl.us/NotebooksPython101"><img src = "https://ibm.box.com/shared/static/yfe6h4az47ktg2mm9h05wby2n7e8kei3.png" width = 750, align = "center"></a>
# 
# 
# 
# 

# <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# 
# 
# <h1 align=center><font size = 5>Reading Files Python </font></h1>

# <br>

# This notebook will provide information regarding reading **.txt** files.

# ## Table of Contents
# 
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# 
# <li><a href="#ref1">Reading Text Files</a></li>
# 
# <br>
# <p></p>
# Estimated Time Needed: <strong>15 min</strong>
# </div>
# 
# <hr>

#  <a id="ref1"></a>
# <h2 align=center>Reading Text Files</h2>

# One way to read or write a file in Python is to use the built-in **open** function. The **open** function provides a **File object** that contains methods and attributes you need to read, save, and manipulate the file. In this notebook, we will only cover **.txt** files. The first parameter you need is the file path and the file name. An example is shown in __Figure 1__.
# 
# 

#  <a ><img src = "https://ibm.box.com/shared/static/6wl3vw4ghflafrou0noj70t2n4hbalqr.png" width = 500, align = "center"></a>
#   <h4 align=center>  
#     Figure 1: Labeled Syntax of a file object.  
# 
#   </h4> 

#  The mode argument is optional the default value is **r**. In this notebook we only cover two modes: 
# 
# <li>**r** Read mode for reading files </li>
# <li>**w** Write mode for writing files</li>

#  For the next example, we will use the text file **Example1.txt**. The file is shown in figure 2.
# 

#  <a ><img src = "https://ibm.box.com/shared/static/ilzy3av6x1cd3gi61bq2nq0vxb0awhju.png" width = 200, align = "center"></a>
#   <h4 align=center>  
#     Figure 2: The text file "Example1.txt".
# 
#   </h4> 

#  First we load the file into the directory 

# In[1]:

get_ipython().system(u'wget -O /resources/data/Example1.txt https://ibm.box.com/shared/static/6rv6cphk4uwrfe6ne9sye1fc8yy6w9q9.txt')


#  we read the file 

# In[2]:

example1="/resources/data/Example1.txt"
file1 = open(example1,"r")


#  We can view the attributes of the file.

# The name of the file:

# In[3]:

file1.name


#  The mode the file object is in:

# In[4]:

file1.mode


# We can read the file and assign it to a variable :

# In[5]:

FileContent=file1.read()
FileContent


# The “/n” tells python that there is a new line. 

# we can print the file 

# In[6]:

print(FileContent)


# The file is of type string:

# In[7]:

type(FileContent)


#  We must close the file object:

# In[8]:

file1.close()


# In[9]:

file1


#  <h3> A  Better Way to Open a File </h3>

# Using the **with** the statement is better practice, it automatically closes the file even if the code encounters an exception. The code will run everything in the indent block then close the file.
# 

# In[10]:

with open(example1,"r") as file1:
    FileContent=file1.read()
    print(FileContent)


# The file object is closed, you can verify it by running the following cell:  

# In[11]:

file1.closed


#  we can see the info in the file:

# In[12]:

print(FileContent)


# The syntax is a little confusing as the file object is after the **as** statement. Also, we don’t explicitly close the file. Therefore we summarise the steps in a figure:

#  <a ><img src = "https://ibm.box.com/shared/static/ywul1ji1ld82xwz60ljxvbg6fs2vrunm.png" width = 500, align = "center"></a>
#   <h4 align=center>  
#     The syntax for opening a file using a with statement.
# 
#   </h4> 

# In[13]:

with open(example1,"r") as file1:
    FileContent=file1.readlines()
    print(FileContent)


# We don’t have to read the entire file, for example, we can read the first 4 characters by entering three as a parameter to the method **.read()**
# 

# In[14]:

with open(example1,"r") as file1:
    print(file1.read(4))


# Once the method **.read(4)** is called the first 4 characters are called, if we call the method again, the next four characters are called. The output for the following cell will demonstrate the process for different inputs to the method **read() **.
# 
# 

# In[15]:

with open(example1,"r") as file1:
    print(file1.read(4))
    print(file1.read(4))
    print(file1.read(7))
    print(file1.read(15))


#  The process is illustrated in figure,  each color represents the part of the file read after the method **read()** is called.
# 

#  <a ><img src = "https://ibm.box.com/shared/static/s0xs6y4vcvabp2ll2pwspa6kd8qeoddj.png" width = 500, align = "center"></a>
#   <h4 align=center>  
#      Illustration of using the method **.read()** to call differnet characters 
# 
#   </h4> 

#  here is an example using different values 

# In[16]:

with open(example1,"r") as file1:
    print(file1.read(16))
    print(file1.read(5))
    print(file1.read(9))


# We can also read one line of the file at a time using the method **readline()**: 

# In[17]:

with open(example1,"r") as file1:
   print("first line: " + file1.readline())


#  We can use a loop to iterate through each line. 
# 

# In[18]:

with open(example1,"r") as file1:
       i=0;
       for line in file1:
           print("Iteration" ,str(i),":",line)
           i=i+1;


# We can use the method **readline()** to save the text file to a list. 

# In[19]:

with open(example1,"r") as file1:
    FileasList=file1.readlines()


#  Each element of the list corresponds to a line of text.

# In[20]:

FileasList[0]


# In[21]:

FileasList[1]


# In[22]:

FileasList[2]


# ### Hi Joseph here, check out my other course Data Analysis with Python, just click the image below:
# <a href="http://cocl.us/PY0101ENtoDA0101EN"><img src = "https://ibm.box.com/shared/static/1msv7g4ovv35c2eb97gsp45gdm833eqz.png" width = 300, align = "center"></a>

# #### Enjoying Python? Think ahead about what you might want to use in the future.
# If you're looking for a enterprise-ready environment to use Python on a big scale with two free Apache Spark executors, consider signing up for a free account on [Data Science Experience](http://cocl.us/NotebooksPython101bottom)

# <hr>
# ### About the Author:  
#  [Joseph Santarcangelo]( https://www.linkedin.com/in/joseph-s-50398b136/) has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.

#  <hr>
# Copyright &copy; 2017 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).​
