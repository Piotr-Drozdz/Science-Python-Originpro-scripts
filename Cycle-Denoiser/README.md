# Cycle Denoiser

This script removes outliers from repetitive spectroscopic measurements collected in cycles (multiple acquisition passes at the same experimental condition) and produces averaged, cleaned spectra as Origin worksheets.

## Motivation

Raw spectroscopic data often contain outliers due to detector noise or other experimental fluctuations.  
Manually cleaning these spectra is tedious and error-prone.  

**Cycle Denoiser** automates this process by:
- Detecting points that deviate more than a user-defined multiple of the standard deviation
- Replacing these points with `NaN` to ignore them in averaging
- Averaging repeated cycles to produce a clean spectrum
- Generating energy-normalized spectra (`Energy⁻⁶`) commonly used in ruby fluorescence calibration

## Usage

1. Open your Origin project containing all raw spectra worksheets.
2. Open the the project in Origin (Connectivity -> Embedded Python). You should see the code in text editor.
3. Press F5.


## Output

This script does not load any external files.

**Input** = Origin worksheets that are already open in the current Origin project.

Each worksheet must contain:
- column 0 → Wavelength  
- columns 1…N → repeated cycles of the same spectrum (e.g. multiple accumulations)

### What the script produces

If data are valid, it will generate **3 new worksheets** in the same Origin project:

| Worksheet name  | What it contains |
|-----------------|------------------|
| `widma`         | denoised + averaged spectra from all “simple” measurements (two tokens in column label) |
| `rubiny`        | denoised + averaged spectra from ruby measurements (three tokens in column label) |
| `widma_energy`  | same as `widma`, but each averaged spectrum is additionally normalized by `Energy⁻⁶` |

Column labels in all these worksheets correspond to measurement parameters parsed from the original sheets (temperature, pressure, etc — whatever was in the column label).

All of this happens in-memory in Origin — no intermediate files are created.
