import originpro as op
import pandas as pd
import numpy as np


#Search for "Sheet1" in workbook "Data2" and load its content to pandas dataframe
rr = op.find_sheet(ref="[Data2]Sheet1!")
dane = rr.to_df()
#Prepare empty dict for output
widma = {}
#Take the first and last points of the spectrum
#These two points are the basis for linear backgroudn fitting, so you should adapt these for your own needs
x = [dane.A[0], dane.A.iloc[-1]]
#Correct every column of DF but A. A is assumed to be X.
for i in dane.columns:
    if i != 'A':
        y = [dane[i][0], dane[i].iloc[-1]]
        a, b = np.polyfit(x, y, 1)
        widma[i] =dane[i]- a*dane.A-b
    else:
        widma['Wavelenngth'] = dane[i]
        

#Find Sheet1 in Workbook "Widma"
nova = op.find_sheet(ref = "[widma]1!")

#If Sheet1 in Workbook "Widma" exists, rewrite it. 
#If it doesn't exist, create it and save output data.
if nova:
    nova.from_dict(widma)
else:
    nova = op.new_sheet('w', lname='widma')
    nova.from_dict(widma)
