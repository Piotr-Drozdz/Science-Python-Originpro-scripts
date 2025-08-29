# Waterfall Plot Preparation Script

This Python script is part of a larger collection of data analysis scripts for **OriginPro**. It processes spectral data from an Origin worksheet and prepares it for visualization as a **waterfall plot**, scaling each spectrum to avoid overlapping curves.

## Features

- Reads spectral data from an Origin worksheet named `widma_energy`.
- Retrieves column labels and associated pressure values.
- Computes scaling factors based on pressure differences and a user-defined constant.
- Applies logarithmic scaling (multiplication by `10^factor`) to successive spectra.
- Saves the resulting dataset to a new or existing Origin worksheet named `waterfall`.
- Prepares data for clear, visually separated waterfall plots.

## Dependencies

- [OriginPro Python Library](https://www.originlab.com/python) (`originpro`)
- `pandas`
- `numpy`

> Note: Although other libraries like `scipy` are imported in the script, they are not used.

## Usage

1. Ensure your Origin project contains a worksheet named `widma_energy`.
2. Place this script in your Python environment that has access to OriginPro.
3. Run the script:
   ```bash
   python waterfall_prep.py
