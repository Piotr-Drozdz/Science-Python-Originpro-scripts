import numpy as np
import pandas as pd
import os
import originpro as op


#Path to the file you want to read
pt = 'F:\P4\P4.CCDspc'

#Function that reads the file and returns the data as numpy array
def otw(pat):
    f = open(pat,"r")
    head = [next(f) for _ in range(20)]
    body = f.readlines()
    wid = []
    for bd in body:
        b = bd.split('\t')
        b[1]=b[1].strip('\n')
        wid.append(b)
    wid = np.array(wid)
    return(wid)
    
    
dt = otw(pt)

#Save the data as origin sheet named "datya"
iks = dt[:,0]
igrek = dt[:,1]
widmo = {'Wavelength (nm)':iks,'Intensity (arb. units)':igrek}
nowy = op.new_sheet('w', lname='datya')
nowy.from_dict(widmo)
