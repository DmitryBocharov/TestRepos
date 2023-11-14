#!/usr/bin/env python
# coding: utf-8

# # Data Science Tools and Ecosystem

# In this notebook, Data Science Tools and Ecosystem are summarized.

# Some of the popular languages that Data Scientists use are:

# **Objectives:**
# 
# 
# - List popular languages for Data Science.
# - Introduce the concept of version control with Git and GitHub.
# - Explore data visualization in R using ggplot2.
# - Understand basic commands for Git and GitHub, including cloning and committing changes.
# - Demonstrate creating and formatting Markdown cells in Jupyter Notebook.
# 

# In[11]:


# Creating an ordered list of commonly used languages for data science

languages = [
    "Python",
    "R",
    "SQL",
    "Julia",
    "Scala"
]

# Printing the ordered list
for index, language_description in enumerate(languages, start=1):
    print(f"{index}. {language_description}")


# Some of the commonly used libraries used by Data Scientists include:
# 

# In[13]:


# Creating an ordered list of commonly used libraries for data science

libraries = [
    "NumPy: A fundamental package for scientific computing with Python.",
    "Pandas: A powerful data manipulation and analysis library.",
    "Scikit-Learn: A machine learning library that provides simple and efficient tools for data analysis and modeling.",
    "Matplotlib: A 2D plotting library for creating static, animated, and interactive visualizations in Python.",
    "Seaborn: A statistical data visualization library based on Matplotlib, providing an aesthetically pleasing and informative visual representation of data.",
]

# Printing the ordered list
for index, library_description in enumerate(libraries, start=1):
    print(f"{index}. {library_description}")


# Create a markdown cell with a table of Data Science tools

# | Data Science Tools        |
# |---------------------------|
# | Jupyter Notebooks         |
# | RStudio                   |
# | VSCode with Python extension |
# 

# ### Below are a few examples of evaluating arithmetic expressions in Python

# In[15]:


#This a simple arithmetic expression to mutiply then add integers
(3*4)+5


# In[17]:


# This will convert 200 minutes to hours by dividing by 60.
minutes = 200
hours = minutes / 60

# Display the result
hours


# ## Author
# Dmitry Bocharov

# In[ ]:




