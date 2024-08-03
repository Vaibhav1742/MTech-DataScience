#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mpi4py import MPI


# In[2]:


rank = MPI.COMM_WORLD.Get_rank()

a=6.0
b=3.0
if rank == 0:
    print(a+b)
if rank == 1:
    print(a*b)
if rank == 2:
    print(max(a,b))
print("end of MPI")


# In[ ]:




