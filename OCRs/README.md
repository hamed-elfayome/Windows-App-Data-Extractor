
# Optical Character Recognition (OCR) Data Extraction

> All OCRs tested on one element: **price**

This folder contains scripts for extracting data from screenshots of a Windows application using Optical Character Recognition (OCR) techniques. The `screen.py` script captures screenshots of the window containing the targeted data and then crops the screenshots into parts, each representing specific data fields.

## OCR Methods

different OCR methods were employed to extract text from the cropped screenshots. The performance of each method was evaluated based on the average time per iteration and the efficiency of the extracted data.

| Method                                  | Average Time per Iteration (seconds) | 
|-----------------------------------------|--------------------------------------|
| pytesseract                  | 0.1902                               | 
| trocr-small-printed          | 0.3855                               | 
| trocr-small-printed *enhanced* | 0.428                                | 
| trocr-base-printed           | 1.4098                               | 

## Efficiency Analysis

The efficiency of each OCR method was assessed by comparing the extracted data with the true values. The following results were obtained:

| Method                                  | Total | Matches | Efficiency (%) |
|-----------------------------------------|------------|---------|----------------|
| pytesseract                  | 999        | 876     | 87.69          |
| trocr-small-printed          | 999        | 898     | 89.89          |
| trocr-small-printed *enhanced* | 999        | 981     | 98.20          |
| trocr-base-printed           | 999        | 998     | 99.90          |

## Conclusion

Overall, the efficiency of the OCR methods varied, with **trocr-base-printed** demonstrating the highest accuracy at 99.90%. However, it also had the longest average time per iteration. Depending on the specific requirements of the project, the choice of OCR method should consider a balance between accuracy and processing speed.
