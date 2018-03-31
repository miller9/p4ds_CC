
# coding: utf-8

#  <div class="alert alert-block alert-info" style="margin-top: 20px">
#  <a href="http://cocl.us/NotebooksPython101"><img src = "https://ibm.box.com/shared/static/yfe6h4az47ktg2mm9h05wby2n7e8kei3.png" width = 750, align = "center"></a>
# 
# 
# 

#  <a href="https://www.bigdatauniversity.com"><img src = "https://ibm.box.com/shared/static/ugcqz6ohbvff804xp84y4kqnvvk3bq1g.png" width = 300, align = "center"></a>
# 
# <h1 align=center><font size = 5>Sets and Dictionaries</font></h1>

# 
# ## Table of Contents
# 
# 
# <div class="alert alert-block alert-info" style="margin-top: 20px">
# 
# <li><a href="#ref2">Dictionaries</a></li>
# <br>
# <p></p>
# Estimated Time Needed: <strong>20 min</strong>
# </div>
# 
# <hr>

# <a id="ref2"></a>
# <h2 align=center> Dictionaries  in Python  </h2>
# 

# A dictionary consists of keys and values. It is helpful to compare a Dictionary to a List. Instead of the numerical indexes like a list, dictionaries have keys. These keys are labels that are used to access values within a dictionary.

# <a ><img src = "https://ibm.box.com/shared/static/6tyznuwydogmtuv73o8l5g7xsb8o92h2.png" width = 650, align = "center"></a>
#   <h4 align=center> Figure 8: A  Comparison of a Dictionary to a list. Instead of the numerical indexes like a list, dictionaries have keys.
#   </h4> 
# 

# # An example of a Dictionary **Dict**

#  An example of a  Dictionary **Dict**

# In[1]:

Dict={"key1":1,"key2":"2","key3":[3,3,3],"key4":(4,4,4),('key5'):5,(0,1):6}
Dict


#  The keys can be strings 

# In[2]:

Dict["key1"]


#  Keys can also be any immutable object such as a tuple: 

# In[3]:

Dict[(0,1)]


#  Each key is separated from its value by a colon **:**. Commas separate the items, and the whole dictionary is enclosed in curly braces. An empty dictionary without any items is written with just two curly braces, like this: **{}**.

# In[4]:

release_year_dict = {"Thriller":"1982", "Back in Black":"1980",                     "The Dark Side of the Moon":"1973", "The Bodyguard":"1992",                     "Bat Out of Hell":"1977", "Their Greatest Hits (1971-1975)":"1976",                     "Saturday Night Fever":"1977", "Rumours":"1977"}
release_year_dict


# In summary like a list, a dictionary holds a sequence of elements. Each element is represented by a key and its corresponding value. Dictionaries are created with two curly braces containing keys and values separated by a colon. For every key, there can only be a single value however  Multiple keys can hold the same value. Keys can only be strings, numbers, or tuples, but values can be any data type.

#  It is helpful to visualize the dictionary as a table, as in figure 9. The first column represents the keys, the second column represents the values.
# 

#  <a ><img src = "https://ibm.box.com/shared/static/i45fppou18c3t0fuf2ikks48tod7chbl.png" width = 650, align = "center"></a>
#   <h4 align=center> Figure 9: Table representing a Dictionary  
# 
#   </h4> 
# 

# You will need this dictionary for the next two questions :

# In[5]:

soundtrack_dic = { "The Bodyguard":"1992", "Saturday Night Fever":"1977"}
soundtrack_dic 


# #### In the dictionary "soundtrack_dict" what are the keys ?

# In[8]:

print (soundtrack_dic.keys())
print (soundtrack_dic.values())


#  <div align="right">
# <a href="#Dict1" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="Dict1" class="collapse">
# ```
# The Keys "The Bodyguard" and "Saturday Night Fever" 
# ```
# </div>

# ####  In the dictionary "soundtrack_dict" what are the values ?

#  <div align="right">
# <a href="#Dict2" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="Dict2" class="collapse">
# ```
# The values are "1992" and "1977"
# ```
# </div>

# Now, you can retrieve the values based on the names:

# In[9]:

release_year_dict['Thriller'] 


# This corresponds to: 
# 

#  <a ><img src = "https://ibm.box.com/shared/static/glbwz23cgjjxqi7rjxn7me5i16gan7h7.png" width = 500, align = "center"></a>
#   <h4 align=center> 
#  Table used to represent accessing the value for "Thriller"   
# 
#   </h4> 
# 

# Similarly for The Bodyguard     
# 

# In[10]:

release_year_dict['The Bodyguard'] 


#  <a ><img src = "https://ibm.box.com/shared/static/6t7bu8jusckaskukwq1k0a3im5ltcpsn.png  " width = 500, align = "center"></a>
#   <h4 align=center> 
# Accessing the value for the "The Bodyguard"
# 
#   </h4> 
# 
# 
# 

# Now let us retrieve the keys of the dictionary using the method **release_year_dict()**.

# In[11]:

release_year_dict.keys() 


#  And you can retrieve the values using the method  **`values()`**

# In[12]:

release_year_dict.values() 


# we can add an entry 

# In[13]:

release_year_dict['Graduation']='2007'
release_year_dict


# We can delete an entry   

# In[14]:

del(release_year_dict['Thriller'])
del(release_year_dict['Graduation'])
release_year_dict


#  we can verify if an element is in the dictionary  

# In[15]:

'The Bodyguard' in release_year_dict


# #### The Albums 'Back in Black', 'The Bodyguard' and 'Thriller' have the following Music recording sales in millions 50,50 and 65 respectively

# ##### a) Create a dictionary “album_sales_dict” where the keys are the album name and the sales in millions are the values  

# In[17]:

album_sales_dict= { "The Bodyguard":50, "Back in Black":50,"Thriller":65}
album_sales_dict


# <div align="right">
# <a href="#q9" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="q9" class="collapse">
# ```
# album_sales_dict= { "The Bodyguard":50, "Back in Black":50,"Thriller":65}
# ```
# </div>

# #### b) Use the dictionary to find the total sales of "Thriller"

# In[18]:

album_sales_dict["Thriller"]


# <div align="right">
# <a href="#q10b" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="q10b" class="collapse">
# ```
# album_sales_dict["Thriller"]
# ```
# </div>

# #### c) Find the names of the album from the dictionary using the method "keys" 

# In[20]:

album_sales_dict.keys()


# <div align="right">
# <a href="#q10c" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="q10c" class="collapse">
# ```
# album_sales_dict.keys()
# ```

# #### d) Find the names of the recording sales​ from the dictionary using the method "values"

# In[21]:

album_sales_dict.values()


# <div align="right">
# <a href="#q10d" class="btn btn-default" data-toggle="collapse">Click here for the solution</a>
# 
# </div>
# <div id="q10d" class="collapse">
# ```
# album_sales_dict.values()
# ```
# </div>

# #### Hi Joseph here, check out my other course Data Analysis with Python, just click the image below:
# <a href="http://cocl.us/PY0101ENtoDA0101EN"><img src = "https://ibm.box.com/shared/static/1msv7g4ovv35c2eb97gsp45gdm833eqz.png" width = 300, align = "center"></a>

# #### Enjoying Python? Think ahead about what you might want to use in the future.
# If you're looking for a enterprise-ready environment to use Python on a big scale with two free Apache Spark executors, consider signing up for a free account on [Data Science Experience](http://cocl.us/NotebooksPython101bottom)

# 
# 
# # About the Authors:  
# 
#  [Joseph Santarcangelo]( https://www.linkedin.com/in/joseph-s-50398b136/) has a PhD in Electrical Engineering, his research focused on using machine learning, signal processing, and computer vision to determine how videos impact human cognition. Joseph has been working for IBM since he completed his PhD.
# 
# 

#  <hr>
# Copyright &copy; 2017 [cognitiveclass.ai](cognitiveclass.ai?utm_source=bducopyrightlink&utm_medium=dswb&utm_campaign=bdu). This notebook and its source code are released under the terms of the [MIT License](https://bigdatauniversity.com/mit-license/).
