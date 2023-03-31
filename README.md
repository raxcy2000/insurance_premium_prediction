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

Install packages in the environment 

NB: This is for Mac (Windows users please see [documentation](https://auto.gluon.ai/stable/install.html) or other video for more)

```
pip3 install torch==1.13.1 torchvision==0.14.1 -f https://download.pytorch.org/whl/torch_stable.html
pip install autogluon 
pip install streamlit jupyter
```

To have the same version in the dependencies, you can install them together by using `pip install autogluon streamlit jupyter`

### Test your installation as follows:

```py
On your terminal, type python. then paste `from autogluon.tabular import TabularDataset, TabularPredictor`
```

If that works, then you have good installation for autogluon.

```py
Test for Streamlit by typing `streamlit hello` on the terminal.
```

You will see the message below if it works>
```
  Welcome to Streamlit. Check out our demo in your browser.

  Local URL: http://localhost:8501
  Network URL: http://192.168.1.189:8501

  Ready to create your own Python apps super quickly?
  Head over to https://docs.streamlit.io

  May you create awesome apps!
```

This will automatically pop up on your default browser on this address - http://localhost:8501/

## Project Structure

```
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
