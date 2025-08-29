# OriginPro Python Scripts

This repository contains Python scripts I developed as part of my scientific work, using the `originpro` library.

**Origin** is a computational environment widely used, for example, by experimental physicists. While it primarily relies on a graphical interface, it also offers automation capabilities, including a native scripting language.

Recent versions of Origin include an embedded Python interpreter, allowing users to automate computational tasks and combine the strengths of both Python and Origin.

The **`originpro`** Python library provides an interface to Origin, and it is used in all scripts in this repository.

## Repository Structure

Each folder contains a single script along with its own README describing its functionality and usage examples.

Example folders:  
- `Linear-background-substract/` – subtracts linear background from spectra based on first and last points of each column
- `OPO-decoder/` – decodes legacy measurement data directly in Origin (using originpro) and outputs an Origin worksheet
- `Data-for-Waterfall-log/` – scales successive spectra from an Origin worksheet for clear visualization in a waterfall plot (using logarithmic multiplication)

## Notes

- All scripts require an Origin installation with Python support and the `originpro` library.  
- These scripts are provided as-is for educational and reference purposes; they are not actively maintained.
