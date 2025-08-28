# OPO-decoder

This script decodes measurement data from a legacy format that is not supported by recent versions of Origin and returns the results as an Origin worksheet.

## Motivation

Previously, decoding the data required using a separate program on the experimental setup’s control computer.  
This was inconvenient and created unnecessary queues, as people had to occupy the setup only to decode their files.  

To solve this, I wrote **OPO-decoder**:  
- Runs directly inside Origin using the `originpro` Python library  
- Produces decoded data immediately in the form of an Origin worksheet  
- Works faster than the original decoding software  
- Allows users to decode their data on their own computers without accessing the experimental setup  

## Usage

1. Open Origin with Python support enabled.  
2. Run the script from Origin’s Python console or as a Python file.  
3. The decoded data will appear in a new Origin worksheet, ready for further analysis or plotting.  

## Notes

- Requires Origin with Python support and the `originpro` library.  
- The script was written for a specific experimental device and its legacy data format.  
- If your data format differs, some adjustments may be necessary.
