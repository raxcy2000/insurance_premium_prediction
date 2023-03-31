# Insurance_Premium_Prediction

AutoML Insurance Premium Prediction using AutoGluon Framework

## Introduction

This will be using `AutoGluon` Framework.

## Business Objective


## Environment Setup
Create an environment

```python
conda create --name insuranceenv python=3.9 -y
```

Activate the environment

```python
conda activate insuranceenv
```

Install packages in the environment NB: This is for Windows (Mac users please see documentation or other video for more)

```python pip install torch==1.12.1+cpu torchvision==0.13.1+cpu torchtext==0.13.1 -f https://download.pytorch.org/whl/cpu/torch_stable.html
pip install autogluon streamlit jupyter
```

### Tell your installation as follows:
```py
(insuranceenv) C:\Users\djoguns\Documents\workspace_datahackerman\insurance_premium_prediction>python
Python 3.9.16 (main, Jan 11 2023, 16:16:36) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license" for more information.
>>> from autogluon.tabular import TabularDataset, TabularPredictor
```

If that works, then you have good installation for autogluon.

And then for Streamlit,

```python
(insuranceenv) C:\Users\djoguns\Documents\workspace_datahackerman\insurance_premium_prediction>streamlit hello

  Welcome to Streamlit. Check out our demo in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.189:8501

  Ready to create your own Python apps super quickly?
  Head over to https://docs.streamlit.io

  May you create awesome apps!
```

This will automatically pop up on your default browser on this address - http://localhost:8501/

## Project Structure

```python
Insurance Premium

|--README.md
|--images
|--data
|--main.py
|--main.ipynb
|--experimentation.ipynb
|--app.py
```

## Data Ingestion

## Exploratory Data Analysis (EDA)

## Features Engineering or Processing

## Model Building

## Model Evaluation

## Model Deployment

Deployment will be done on Streamlit.
