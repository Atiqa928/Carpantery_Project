#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Conditionals_NEW


# In[1]:


all_elevations= [100,200,50]
for elevation in all_elevations:
    new_elevation=elevation/2 # to create new variable in the loop
    print(new_elevation)


# In[2]:


print(elevation)


# In[3]:


print(new_elevation)


# In[8]:


all_elevations= [100,200,50]
elevation_result= []
for elevation in all_elevations:
    new_elevation=elevation/2
    print(new_elevation)
    elevation_result.append(new_elevation)

print(elevation_result)

#/ will make number a float
#// forces number to be an integer


# In[ ]:


### Conditionals


# In[9]:


elevation = 100

if elevation > 10:
    print(elevation, 'is high')


# In[10]:


elevation=0
if elevation > 10:
    print(elevation, 'is high')


# In[14]:


all_elevations= [200,100,5,1]
for elevation in all_elevations:
    print(elevation)
    if elevation > 10:
        print(elevation, 'is high')


# In[15]:


all_elevation = [200,100,5,1]
for elevation in all_elevations:
    print(elevation)
    if elevation > 10: # if if statement is not true then we use else
        print (elevation, 'is high')
    else: 
        print(elevation, 'is low')


# In[18]:


all_elevation = [200,100,5,1]
for elevation in all_elevations:
    print(elevation)
    if elevation > 10: # if if statement is not true then we use else
        print (elevation, 'is high')
    elif elevation > 100: # short of elseif
        print(elevation, 'is huge!')
    else:
        print(elevation, 'is small')

# elif did not work coz the order of statement is very important. we can fix it by chaging the ordr of statements
all_elevation = [200,100,5,1]
for elevation in all_elevations:
    print(elevation)
    if elevation > 10: # if if statement is not true then we use else
        print (elevation, 'is huge!')
    elif elevation > 100: # short of elseif
        print(elevation, 'is high!')
    else:
        print(elevation, 'is small')


# In[20]:


for elevation in all_elevations:
    print(elevation)
    if elevation > 100: # if if statement is not true then we use else
        print (elevation, 'is huge!')
        
    if elevation > 10: # short of elseif
        print(elevation, 'is high!')
    


# In[22]:


all_elevations = [ 5,100,10,20,75,85,200,400]
elevation_results = []

for elevation in all_elevations:
    print(elevation)
    if elevation > 100:
        elevation_results. append ("high")
    elif elevation < 100 and elevation >= 50:
        elevation_results.append("medium")
    else:
        elevation_results.append("low")

print(elevation_results)
                  


# In[39]:


original = [-1.5, 0.2, 0.4, 1.3, 0.5]
#0 if number is below 0, 1 if number is above 1
binary_results = []
for number in original:
    if number > 0:
        binary_results.append(1)
    else:
        binary_results.append(0)

print(binary_results)
    


# In[ ]:




