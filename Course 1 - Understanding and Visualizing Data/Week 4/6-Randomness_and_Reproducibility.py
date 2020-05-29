
# coding: utf-8

# # Randomness and Reproducibility
# 
# As we learned in the beginning of this week, the concept of randomness is a cornerstone for statistical inference when drawing samples from larger populations.
# 
# In this tutorial, we are going to cover the following:
# 
# * Randomness and its uses in python.
# 
# * Utilizing python seeds to reproduce analysis.
# 
# * Generating random variables from a probability distribution.
# 
# * Random sampling from a population.
# 
# 
# ## What is Randomness?
# 
# In the beginning of this week's lectures, we touched on the significance of randomness when it comes to performing statistical inference on population samples.  If we have complete randomness, our estimates of means, proportions, and totals are ubiased.  This means our estimates are equal to the population values on average. 
# 
# In Python, we refer to randomness as the ability to generate data, strings, or, more generally, numbers at random.
# 
# However, when conducting analysis it is important to consider reproducibility.  If we are creating random data, how can we enable reproducible analysis?
# 
# We do this by utilizing pseudo-random number generators (PRNGs).  PRNGs start with a random number, known as the seed, and then use an algorithm to generate a psuedo-random sequence based on it.
# 
# This means that we can replicate the output of a random number generator in python simply by knowing which seed was used.
# 
# We can showcase this by using the functions in the python library *__random__*.
# 
# ### Setting a Seed and Generating Random Numbers

# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

import random


# In[2]:


random.seed(1234)

random.random()


# In[3]:


random.seed(1234)

random.random()


# ### Random Numbers from Real-Valued Distributions 
# #### Uniform

# In[4]:


random.uniform(25,50)


# In[18]:


unifNumbers = [random.uniform(0,1) for _ in range(1000)]


# In[19]:


unifNumbers


# In[20]:


plt.figure(figsize=(15,5))
sns.lineplot(range(0, len(unifNumbers)), unifNumbers)
plt.show()


# #### Normal

# In[21]:


mu = 0

sigma = 1

random.normalvariate(mu, sigma)


# In[22]:


mu = 5

sigma = 2

random.normalvariate(mu, sigma)


# In[24]:


mu = 0

sigma = 1

randNorm = [random.normalvariate(mu, sigma) for _ in range(10000)]

randNorm


# In[25]:


plt.figure(figsize=(15,5))
sns.lineplot(range(0, len(randNorm)), randNorm)
plt.show()


# ### Random Sampling from a Population
# 
# From lecture, we know that **Simple Random Sampling (SRS)** has the following properties:
# 
# * Start with known list of *N* population units, and randomly select *n* units from the list
# * Every unit has **equal probability of selection = _n/N_**
# * All possible samples of size *n* are equaly likely
# * Estimates of means, proportions, and totals based on SRS are **UNBIASED** (meaning they are equal to the population values on average)

# In[26]:


import random
import numpy as np


# In[27]:


mu = 0
    
sigma = 1

Population = [random.normalvariate(mu, sigma) for _ in range(10000)]


# In[28]:


SampleA = random.sample(Population, 500)
SampleB = random.sample(Population, 500)


# In[29]:


np.mean(SampleA)


# In[30]:


np.std(SampleA)


# In[31]:


np.mean(SampleB)


# In[32]:


np.std(SampleB)


# In[39]:


means = [np.mean(random.sample(Population, 500)) for _ in range(100)]

np.mean(means)


# In[40]:


plt.figure(figsize=(15,5))
sns.distplot(means)
plt.show()


# In[41]:


standarddevs = [np.std(random.sample(Population, 500)) for _ in range(100)]


# In[42]:


plt.figure(figsize=(15,5))
sns.distplot(standarddevs)
plt.show()

