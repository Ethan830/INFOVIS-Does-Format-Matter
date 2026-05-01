# Does Format Matter? Supplementary Materials

This repository contains the data, experimental scripts, and analysis code for our study evaluating Large Language Model (LLM) confidence calibration across diverse visualization modalities.

## Research Overview

This study investigates whether the cognitive benefits of visual representation established in human cognition research transfer to multimodal LLMs. We evaluate three input modalities—rendered images, structured data tables, and descriptive paragraphs—across four continuous visualization types (line graphs, color maps, isolines, and arrow glyphs). Our findings indicate a modality inversion: rendered image inputs consistently degrade confidence calibration and increase susceptibility to false claims compared to text-based alternatives. This effect is most pronounced in tasks requiring precise spatial decoding and outlier detection.

---

## Repository Structure

### Data and Stimuli
* **Ground-Truth/**: Contains the definitive ground truth values and correct answers for all experimental datasets.
* **Question.py**: A centralized script storing the specific analytic questions (Q1: Value Retrieval, Q2: Trend Detection, Q3: Outlier Detection) applied to each dataset.

### Processing Scripts
* **DAT-_PAR.py**: The translation script used to convert raw CSV data tables into structured TXT descriptive paragraphs.
* **DAT-_VIS.py**: The rendering script used to convert CSV data tables into PNG rendered images for the visualization modality.
* **Main.py**: The core experimental harness that administers the specific input modality and corresponding questions to the various LLM APIs.

### Results and Analysis
* **results/**: The primary storage directory for raw model outputs and experiment results.
* **[Results Google Sheets](https://docs.google.com/spreadsheets/d/1V_zxzw-bqGHpESPz517VrZj6eQBSuoGxXUbFOoQlwSM/edit?usp=sharing)**: The primary storage directory for processed data and data analysis.
* **Result-Excel.py**: A post-processing script that extracts confidence scoring from the results into Excel spreadsheets.
* **Linear Mixed Effect Model-1 (LMEM-1)/**: This folder stores LMEM results and **LMEM-1.py**, the Python script used for LMEM statistical analysis. (LMEM on input modality, visualization type, and LLM model)
* **Linear Fixed Effect Model (LFEM)/**: This folder stores LFEM results and **LFEM.py**, the Python script used for LMEM statistical analysis.
* **Linear Mixed Effect Model-2 (LMEM-2)/**: This folder stores LMEM results and **LMEM-2.py**, the Python script used for LMEM statistical analysis.

---

## Usage

These materials are provided to support the replication of our findings and the extension of our Brier-ECR evaluation framework. Researchers can use the provided translation scripts to generate stimuli in multiple formats and apply the Main.py harness to evaluate new models or visualization types.
