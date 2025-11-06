import originpro as op
import pandas as pd
from scipy.signal import find_peaks, peak_widths,find_peaks_cwt
from scipy.datasets import electrocardiogram
from scipy.signal import argrelmax
from scipy import constants as cts
import numpy as np
import re

# prepare containers for processed spectra
widma = {}
rubiny = {}
mnoznik = 1
srt = []

# Write dictionary to Origin worksheet (for some reason writing dataframe doesn't work well)
def write_dict_to_sheet(sheet_name, data_dict, labels=None):
    sheet = op.find_sheet(ref = f"[{sheet_name}]1!")
    if sheet:
        sheet.from_dict(data_dict)
    else:
        sheet = op.new_sheet('w', lname=sheet_name)
        sheet.from_dict(data_dict)

    if labels is not None:
        sheet.set_labels(labels,'C')

# noise filtering:
# for every row compute mean and std,
# if a point is further than mnoznik * std from mean -> replace with NaN
def denoise(slc):
    for i in slc.iterrows():
        sred = i[1].mean()
        stdev = i[1].std()
        for j in range(len(i[1])-1):
            if abs(i[1][j]-sred) > mnoznik*stdev:
                slc.iloc[i[0], j] = np.nan

    # new averaged spectrum after removing outliers
    return slc.mean(axis=1, skipna=True)

def energia(wd1, wd):
    energie = {}
    energie['Energy'] = cts.h*cts.c/(cts.e*wd1['Wavelength']*10**-9)
    for i in srt:
        print(type(i))
        nz = str(i)+' '+ cm[-1]
        energie[nz] = wd[str(i)]/(energie['Energy']**6)
    return energie

# loop through all worksheets in current Origin project
# and process only those which represent valid spectra
wks = op.project.pages('w')
for w in wks:
    if len(w) > 1:
        # extract cell label and parse metadata
        com = w[1].get_label(0, type='C')
        cm = com.split(' ')
        if com and ('-' not in com):
            # convert worksheet to pandas dataframe
            df = w[1].to_df()
            sel = df.iloc[:, 1:]

            srd = denoise(sel)

            # based on how many parts cm metadata has -> classify as widma or rubiny
            if len(cm) == 2:
                srt.append(float(cm[0]))
                if 'Wavelength' in widma:
                    widma[cm[0]] = srd
                else:
                    widma['Wavelength'] = df['Wavelength']
                    widma1 = {'Wavelength': df['Wavelength']}
                    widma[cm[0]] = srd

            if len(cm) == 3:
                nz = cm[1] + ' ' + cm[2]
                if 'Wavelength' in rubiny:
                    rubiny[cm[1]] = srd
                else:
                    rubiny['Wavelength'] = df['Wavelength']
                    rubiny1 = {'Wavelength': df['Wavelength']}
                    rubiny[cm[1]] = srd

# convert into DataFrames for further processing and export
widma = pd.DataFrame(widma)
rubiny = pd.DataFrame(rubiny)
print(rubiny)

# sort temperatures (or general parameters) list
srt.sort()

# reassemble column naming convention and fill widma1 and rubiny1 dicts
for i in srt:
    print(type(i))
    nz = str(i)+' '+ cm[-1]
    widma1[nz] = widma[str(i)]
    if i != 0:
        rubiny1[nz] = rubiny[str(i)]

# build label list and set column labels for both sheets
lab = ['']
for i in srt:
    lab.append(str(i))
# write rubiny1 to Origin sheet, create new if needed
write_dict_to_sheet('rubiny', rubiny1, labels=lab)

# write widma1 to Origin sheet, create new if needed
write_dict_to_sheet('widma', widma1, labels=lab)

# compute photon energies from wavelength
# and scale each spectrum by Energy^-6  (typical for ruby calibration)
energie = energia(widma1, widma)
# write energy scaled spectra to Origin sheet
write_dict_to_sheet('widma_energy', energie, labels=lab)
