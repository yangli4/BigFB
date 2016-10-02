import numpy as np
import pandas as pd
import h5py

filename = 'train_numeric.csv'

f = h5py.File("Generated_train_First10000Lines.hdf5", "w")
chunksize = 1*(10**4) 
linecounter = 0
chunknum = 1;
for chunk in pd.read_csv(filename, chunksize = chunksize):
	linecounter = linecounter + chunksize 
	datasetname = "Chunk_" + str(chunknum)
	a = np.array(chunk)
	f.create_dataset(datasetname,data=a)
	print(linecounter)
	chunknum = chunknum + 1
	break
"""
print(len(a))
dset = f.create_dataset("Chunk_1", data = a)
dset.shape

bigdata = pd.read_csv(filename2)
#bigdata.fillna("-1")
with h5py.File('data.h5','w') as hf:
	hf.create_dataset('dataset_1',data = bigdata,dtype = 'a')
print(bigdata[1445:1455])
"""

