#!/usr/bin/env python
# coding: utf-8

# In[9]:


from mpi4py.futures import MPIPoolExecutor
from mpi4py import MPI


# In[10]:


from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

print('Welcome to PDPU From processes %d of %d' % (rank, size))


# In[ ]:




