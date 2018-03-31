
# coding: utf-8

#  <div class="alert alert-block alert-info" style="margin-top: 20px">
#  <a href="http://cocl.us/NotebooksPython101"><img src = "https://ibm.box.com/shared/static/yfe6h4az47ktg2mm9h05wby2n7e8kei3.png" width = 750, align = "center"></a>
# 
# 
# 

# <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# 
# 
# <h1 align=center><font size = 5> Writing and Saving Files in PYTHON</font></h1>

# <br>

# This notebook will provide information regarding writing, and saving data into  **.txt** files. 

# ## Table of Contents
# 
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# 
# <li><a href="#refw">Writing files  Text Files</a></li>
# 
# <br>
# <p></p>
# Estimated Time Needed: <strong>15 min</strong>
# </div>
# 
# <hr>

# <a id="ref3"></a>
# <h2 align=center>Writing Files</h2>

#  We can open a file object using the method ** write()**  to save the text file to a list.  To write the mode argument must be set to  write **w**. Let’s write a file **Example2.txt** with the line: “This is line A”

# In[1]:

with open('/resources/data/Example2.txt','w') as writefile:
    writefile.write("This is line A")


#  we can read the file to see if it worked

# In[2]:

with open('/resources/data/Example2.txt','r') as testwritefile:
    print(testwritefile.read())


# We can write multiple lines:

# In[3]:

with open('/resources/data/Example2.txt','w') as writefile:
    writefile.write("This is line A\n")
    writefile.write("This is line B\n")


# The method **.write()** works similar to the method **.readline()**, except instead of reading a new line it writes a new line. The process is illustrated in the figure , the different colour coding of the grid represents a new line added to the file after each method call.

#  <a ><img src = "https://ibm.box.com/shared/static/4d86eysjv7fiy5nocgvpbddyj2uckw6z.png" width = 500, align = "center"></a>
#   <h4 align=center>  
#     An example of “.write()”, the different colour coding of the grid represents a new line added after each method call.
# 
# 
#   </h4> 

# You can check the file to see if your results are correct 

# In[4]:

with open('/resources/data/Example2.txt','r') as testwritefile:
    print(testwritefile.read())


#  by setting the mode argument to append **a**  you can append a new line as follows:

# In[6]:

with open('/resources/data/Example2.txt','a') as testwritefile:
    testwritefile.write("This is line C\n")


#  you can verify the file has changed by running the following cell:

# In[7]:

with open('/resources/data/Example2.txt','r') as testwritefile:
    print(testwritefile.read())


#  We write a list to a **.txt** file  as follows:

# In[8]:

Lines=["This is line A\n","This is line B\n","This is line C\n"]
Lines


# In[9]:

with open('Example2.txt','w') as writefile:
    for line in Lines:
        print(line)
        writefile.write(line)


#  we can verify the file is written by reading it and printing out the values:  

# In[10]:

with open('Example2.txt','r') as testwritefile:
    print(testwritefile.read())


# We can again append to the file by changing the second parameter to  **a**. This adds the code.

# In[11]:

with open('Example2.txt','a') as testwritefile:
    testwritefile.write("This is line D\n")


# We can see the results of appending the file 

# In[12]:

with open('Example2.txt','r') as testwritefile:
    print(testwritefile.read())


# #### Copy a file 

# Lets copy the file **Example2.txt** to the file **Example3.txt**.

# In[13]:

with open('Example2.txt','r') as readfile:
    with open('Example3.txt','w') as writefile:
          for line in readfile:
                writefile.write(line)


# We can read the file to see if everything works:

# In[14]:

with open('Example3.txt','r') as testwritefile:
    print(testwritefile.read())


#  After reading files, we can also write data into files and save them in different file formats like **.txt, .csv, .xls (for excel files) etc**. Let's take a look at some examples.

# Now go to the directory to ensure the .txt file exists and contains the summary data that we wrote.

# #### Enjoying Python? Think ahead about what you might want to use in the future.
# If you're looking for a enterprise-ready environment to use Python on a big scale with two free Apache Spark executors, consider signing up for a free account on [Data Science Experience](http://cocl.us/NotebooksPython101bottom)

# <hr>
# ### About the Author:  
#  [Joseph Santarcangelo]( https://www.linkedin.com/in/joseph-s-50398b136/) has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.

#  <hr>
# Copyright &copy; 2017 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).​
