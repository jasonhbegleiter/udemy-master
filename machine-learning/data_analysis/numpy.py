# Once you've installed NumPy you can import it as a library:

import numpy as np

# ## Creating NumPy Arrays
#
# ### From a Python List
#
# We can create an array by directly converting a list or list of lists:

my_list = [1,2,3]

np.array(my_list)


# In[20]:


my_matrix = [[1,2,3],[4,5,6],[7,8,9]]
my_matrix


# In[21]:


np.array(my_matrix)


# ## Built-in Methods
#
# There are lots of built-in ways to generate Arrays

# ### arange
#
# Return evenly spaced values within a given interval.

# In[22]:


np.arange(0,10)


# In[23]:


np.arange(0,11,2)


# ### zeros and ones
#
# Generate arrays of zeros or ones

# In[24]:


np.zeros(3)


# In[26]:


np.zeros((5,5))


# In[27]:


np.ones(3)


# In[28]:


np.ones((3,3))


# ### linspace
# Return evenly spaced numbers over a specified interval.

# In[29]:


np.linspace(0,10,3)


# In[31]:


np.linspace(0,10,50)


# ## eye
#
# Creates an identity matrix

# In[37]:


np.eye(4)


# ## Random
#
# Numpy also has lots of ways to create random number arrays:
#
# ### rand
# Create an array of the given shape and populate it with
# random samples from a uniform distribution
# over ``[0, 1)``.

# In[47]:


np.random.rand(2)


# In[46]:


np.random.rand(5,5)


# ### randn
#
# Return a sample (or samples) from the "standard normal" distribution. Unlike rand which is uniform:

# In[48]:


np.random.randn(2)


# In[45]:


np.random.randn(5,5)


# ### randint
# Return random integers from `low` (inclusive) to `high` (exclusive).

# In[50]:


np.random.randint(1,100)


# In[51]:


np.random.randint(1,100,10)


# ## Array Attributes and Methods
#
# Let's discuss some useful attributes and methods or an array:

# In[55]:


arr = np.arange(25)
ranarr = np.random.randint(0,50,10)


# In[56]:


arr


# In[57]:


ranarr


# ## Reshape
# Returns an array containing the same data with a new shape.

# In[54]:


arr.reshape(5,5)


# ### max,min,argmax,argmin
#
# These are useful methods for finding max or min values. Or to find their index locations using argmin or argmax

# In[64]:


ranarr


# In[61]:


ranarr.max()


# In[62]:


ranarr.argmax()


# In[63]:


ranarr.min()


# In[60]:


ranarr.argmin()


# ## Shape
#
# Shape is an attribute that arrays have (not a method):

# In[65]:


# Vector
arr.shape


# In[66]:


# Notice the two sets of brackets
arr.reshape(1,25)


# In[69]:


arr.reshape(1,25).shape


# In[70]:


arr.reshape(25,1)


# In[76]:


arr.reshape(25,1).shape


# ### dtype
#
# You can also grab the data type of the object in the array:

# In[75]:


arr.dtype

# ===========================

# Indexing and Slicing


#Creating sample array
arr = np.arange(0,11)


# In[4]:


#Show
arr


# ## Bracket Indexing and Selection
# The simplest way to pick one or some elements of an array looks very similar to python lists:

# In[5]:


#Get a value at an index
arr[8]


# In[6]:


#Get values in a range
arr[1:5]


# In[7]:


#Get values in a range
arr[0:5]


# ## Broadcasting
#
# Numpy arrays differ from a normal Python list because of their ability to broadcast:

# In[8]:


#Setting a value with index range (Broadcasting)
arr[0:5]=100

#Show
arr


# In[9]:


# Reset array, we'll see why I had to reset in  a moment
arr = np.arange(0,11)

#Show
arr


# In[10]:


#Important notes on Slices
slice_of_arr = arr[0:6]

#Show slice
slice_of_arr


# In[11]:


#Change Slice
slice_of_arr[:]=99

#Show Slice again
slice_of_arr


# Now note the changes also occur in our original array!

# In[12]:


arr


# Data is not copied, it's a view of the original array! This avoids memory problems!

# In[13]:


#To get a copy, need to be explicit
arr_copy = arr.copy()

arr_copy


# ## Indexing a 2D array (matrices)
#
# The general format is **arr_2d[row][col]** or **arr_2d[row,col]**. I recommend usually using the comma notation for clarity.

# In[14]:


arr_2d = np.array(([5,10,15],[20,25,30],[35,40,45]))

#Show
arr_2d


# In[15]:


#Indexing row
arr_2d[1]


# In[16]:


# Format is arr_2d[row][col] or arr_2d[row,col]

# Getting individual element value
arr_2d[1][0]


# In[17]:


# Getting individual element value
arr_2d[1,0]


# In[18]:


# 2D array slicing

#Shape (2,2) from top right corner
arr_2d[:2,1:]


# In[19]:


#Shape bottom row
arr_2d[2]


# In[20]:


#Shape bottom row
arr_2d[2,:]


# ### Fancy Indexing
#
# Fancy indexing allows you to select entire rows or columns out of order,to show this, let's quickly build out a numpy array:

# In[21]:


#Set up matrix
arr2d = np.zeros((10,10))


# In[22]:


#Length of array
arr_length = arr2d.shape[1]


# In[23]:


#Set up array

for i in range(arr_length):
    arr2d[i] = i

arr2d


# Fancy indexing allows the following

# In[24]:


arr2d[[2,4,6,8]]


# In[25]:


#Allows in any order
arr2d[[6,4,2,7]]


# ## More Indexing Help
# Indexing a 2d matrix can be a bit confusing at first, especially when you start to add in step size. Try google image searching NumPy indexing to fins useful images, like this one:
#
# <img src= 'http://memory.osu.edu/classes/python/_images/numpy_indexing.png' width=500/>

# ## Selection
#
# Let's briefly go over how to use brackets for selection based off of comparison operators.

# In[28]:


arr = np.arange(1,11)
arr


# In[30]:


arr > 4


# In[31]:


bool_arr = arr>4


# In[32]:


bool_arr


# =======================

# Numpy Operations



# ## Arithmetic
#
# You can easily perform array with array arithmetic, or scalar with array arithmetic. Let's see some examples:

# In[1]:


import numpy as np
arr = np.arange(0,10)


# In[2]:


arr + arr


# In[3]:


arr * arr


# In[4]:


arr - arr


# In[5]:


# Warning on division by zero, but not an error!
# Just replaced with nan
arr/arr


# In[6]:


# Also warning, but not an error instead infinity
1/arr


# In[10]:


arr**3


# ## Universal Array Functions
#
# Numpy comes with many [universal array functions](http://docs.scipy.org/doc/numpy/reference/ufuncs.html), which are essentially just mathematical operations you can use to perform the operation across the array. Let's show some common ones:

# In[12]:


#Taking Square Roots
np.sqrt(arr)


# In[13]:


#Calcualting exponential (e^)
np.exp(arr)


# In[14]:


np.max(arr) #same as arr.max()


# In[15]:


np.sin(arr)


# In[16]:


np.log(arr)
