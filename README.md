# QNLP-SMS
Author: [@SergioJF10](https://github.com/SergioJF10)

## Project Description 🧪💻

This repository contains a collection of scripts, Excel files, folders, and diagrams used for an SMS (Systematic Mapping Study) on the current state of Quantum Natural Language Processing (qNLP). This work is part of a Master's Thesis (TFM) for the Master in Quantum Computing at the International University of La Rioja (UNIR).

## Table of Contents 🗃️
1. **imgs/**: Images, diagrams and tables with the data extraction results.
   - **Execution_process/**: For explaining the execution process.
   - **Preg_inv/**: Regarding research questions and additional information.
     - Conceptos (PI1)
     - Fechas (DE3)
     - Lenguajes (PI3)
     - Paises (DE2)
   - **SMS_process/**: For explaining the overall SMS methodology designed.
2. **results/**: Automatically-built results in JSON and XLSX format after counting stage.
   - **Aplicación (PI2)/**
   - **Concepto (PI1)/**
   - **Fecha (DE3)/**
   - **Lenguaje (PI3)/**
   - **País (DE2)/**
   - **Tipo (DE1)/**
3. **versions/**: Set of versions of the memory.
4. **data_extraction.py**: Python script for generating the data processing results and counting.
5. **datos_sms.xlsx**: Excel file with the main tables, countings, categories and graphics generated along the whole project execution.
6. **README.md**
7. **.gitignore**

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

## Contact 🫡
For any further question, comment or suggestion, don't hessitate on contacting me via email:
  - Sergio Jiménez (Ciudad Real, Spain) - [sergiosjf10@gmail.com](mailto:sergiosjf10@gmail.com)
