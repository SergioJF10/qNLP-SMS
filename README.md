# QNLP-SMS
Author: [@SergioJF10](https://github.com/SergioJF10)

## Project Description 🧪💻

This repository contains a collection of scripts, Excel files, folders, and diagrams used for an SMS (Systematic Mapping Study) on the current state of Quantum Natural Language Processing (qNLP). This work is part of a Master's Thesis (TFM) for the Master in Quantum Computing at the International University of La Rioja (UNIR).

## Table of Contents 🗃️
1. **imgs/**
   - **Execution_process/**
     - Execution_process.vsdx
     - Execution_process.drawio
     - Execution_process.png
     - Execution_process.svg
   - **SMS_process/**
     - SMS_process.drawio
     - SMS_process.jpg
     - SMS_process.png
     - SMS_process.svg
2. **results/**
   - **Aplicación (PI2)/**
     - codigo.json
     - codigo.xlsx
     - general.json
     - general.xlsx
     - papers.json
     - papers.xlsx
   - **Concepto (PI1)/**
   - **Fecha (DE3)/**
   - **Lenguaje (PI3)/**
   - **País (DE2)/**
   - **Tipo (DE1)/**
3. **.gitignore**
4. **data_extraction.py**
5. **datos_sms.xlsx**
6. **README.md**

## Dependencies 🚩

The project relies on the [`pandas`](https://pandas.pydata.org/) library. To ensure a consistent environment, it's recommended to use a Python virtual environment.

### Create and Activate a Virtual Environment

1. **Create a virtual environment:**

    ```bash
    python3 -m venv .venv
    ```
2. **Activate the virtual environment:**

    - On Windows:
        ```bash
        .\venv\Scripts\activate
        ```
    - On Linux and macOS:
        ```bash
        source venv/bin/activate
        ```
2. **Activate the virtual environment:**

    With the virtual environment activated, install the necessary package:
    ```bash
    pip install pandas
    ```

## Execution 🚀

The main script, data_extraction.py, processes the Excel file datos_sms.xlsx and generates the results directory, which includes various subdirectories, each containing files related to different evaluated features of the processed articles.

### How to Run

Ensure that the virtual environment is active, then run the script as follows:

```bash
python data_extraction.py
```

This will generate the results directory with all the corresponding subfolders and files based on the data extracted from datos_sms.xlsx.

