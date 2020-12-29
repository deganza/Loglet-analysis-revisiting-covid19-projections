#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[145]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


# ### Exponential growth $$b*e^{ax}$$

# In[201]:


x = np.arange(1, 100)
a = 0.1
b = 1
y= b*np.exp(a*(x))

plt.plot(x,y)
plt.show()


# In[200]:





# ### Logistic growth $$\frac{K}{(1+e^{(x-b)-r})}$$
# 

# In[140]:


x = np.arange(0, 100)
K = 100
b = 50
r = 0.1


# In[141]:


y = K/(1+np.exp((x-b)*-r))


# In[153]:


plt.plot(x,y)
plt.show()


# In[ ]:





# In[ ]:




