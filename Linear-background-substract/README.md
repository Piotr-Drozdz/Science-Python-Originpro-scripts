# Linear Background Subtract

This script performs linear background subtraction on spectral data in an Origin worksheet.

## How it works

- The first column of the worksheet should contain the X values (e.g., wavelength).  
- Subsequent columns should contain intensity values for each spectrum.  
- For each spectrum, the script takes the first and last points, fits a straight line through them, and subtracts this line from the entire spectrum.  

## Usage

1. Open your Origin worksheet with the data arranged as described above.  
2. Run the script in Origin with Python enabled.  
3. The processed spectra will appear in new Workbook called "widma" ("spectra" in Polish), unless you modify it.

## Notes

- Make sure the worksheet contains numeric data only.  
- This method assumes a roughly linear background between the first and last points of each spectrum.

