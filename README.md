# Coral Bleaching Risk Analysis 🪸

## Project Overview
End-to-end data science project analysing global coral bleaching patterns 
and building a predictive risk model using 40 years of environmental data (1980–2020).

## Motivation
Coral reefs cover less than 1% of the ocean floor but support 25% of all 
marine species. Rising sea surface temperatures (SST) are the primary driver 
of coral bleaching — a phenomenon I have witnessed firsthand as a scuba 
instructor with 1,600+ dives, over 1,200 of which were in the Coral Triangle.

## Dataset
**Source:** Van Woesik & Kratochwill (2022), Global Coral-Bleaching Database  
**Access:** [BCO-DMO](https://www.bco-dmo.org/dataset/773466) / [Kaggle](https://www.kaggle.com/datasets/mehrdat/coral-reef-global-bleaching)  
**Size:** 41,361 observations across 62 variables, 1980–2020

## Project Structure
```
coral-bleaching-risk-analysis/
├── data/
│   ├── raw/          # original data (not tracked by Git)
│   └── processed/    # cleaned data
├── notebooks/
│   ├── 01_data_loading_and_cleaning.ipynb
│   ├── 02_eda.ipynb #in progress
│   ├── 03_feature_engineering.ipynb #coming soon
│   └── 04_modelling.ipynb #coming soon
├── outputs/
│   └── figures/
└── requirements.txt
```

## Status
🟡 In progress — Notebook 01 complete. Notebook 02 (EDA) in progress: missing values, target variable, temporal trends and geographical distribution complete. Correlations and class imbalance assessment pending.

## Future Work
- Interactive map with temporal slider for bleaching severity evolution by site
- Overlay of bleaching data with SSTA and ocean current data
- Regional models (Atlantic, Indo-Pacific, Mediterranean) after global baseline
- LSTM for SST time series and missing value imputation

## Author
Giulia Balducci — Materials Chemistry PhD | Data Scientist
[LinkedIn](https://www.linkedin.com/in/giuliabalducci) | [GitHub](https://github.com/giulia-balducci) | [Kaggle](https://www.kaggle.com/giuliabalducci)
