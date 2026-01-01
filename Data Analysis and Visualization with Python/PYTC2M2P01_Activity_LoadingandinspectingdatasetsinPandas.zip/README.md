# Customer Data Analysis & Ingestion

## Project Overview
This project demonstrates initial data ingestion and exploratory data analysis (EDA) using Python and the Pandas library. The primary goal is to load customer demographic data, validate its structure, and calculate key statistical metrics.

## Features
* **Data Ingestion:** Loading compressed CSV data from a zip archive.
* **Structure Validation:** Using `.shape` and `.head()` to verify dataset dimensions and integrity.
* **Statistical Analysis:** Utilizing `.describe()` for summary statistics and calculating specific column means (e.g., average age).

## Technical Stack
* **Language:** Python 3.x
* **Library:** Pandas

## Usage
To run the analysis locally, ensure you have the `customer_data_50.csv` file in your directory and execute the following in a Jupyter environment:

```python
import pandas as pd
df = pd.read_csv('customer_data_50.csv')
print(df['age'].mean())