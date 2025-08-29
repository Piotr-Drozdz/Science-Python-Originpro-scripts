import originpro as op
import pandas as pd
import numpy as np

#Constant used for scaling data
stala = 0.4
#Get the first worksheet of "widma_energy" workbook
nowy = op.find_sheet(ref = "[widma_energy]1!")
#Get the values in raw "Labels" of the worksheet
labele = nowy.get_labels('L')
#Convert values in row "Comments" of the worksheet to actual values of pressure.
#This is pressure in this particular example, but it can be Temperature or whatever you wish.
cisnienia = [float(n) for n in nowy.get_labels('C') if n != '']
#Find the lowest difference between neighbouring pressure values.
#We will need this to prevent the plots from overlapping
inter = np.diff(cisnienia)
nn = min(inter)
print(nn)
dane = nowy.to_df()
cnn = []
i = 0
dane1 = {}
#Rescale data so that they are suitable for waterfall plotting
dane1['Energy'] = dane['Energy']
for ci in labele:
    cs = ci.split(' ')
    
    if len(cs)>1:
      if cnn:
          dod = (stala*inter[i]/nn) +cnn[-1]
          dane1[ci] = dane[ci] * 10**(dod)
          i = i+1
          cnn.append(dod)
          print(ci)
      else:
           dane1[ci] = dane[ci]
           cnn.append(0)
          

#Find the workbook "waterfall". If it exist, overwrite it, if it doesn't exist, create it and save the values.
nova = op.find_sheet(ref = "[waterfall]1!")
if nova:
    nova.from_dict(dane1)
else:
    nova = op.new_sheet('w', lname='waterfall')
    nova.from_dict(dane1)
