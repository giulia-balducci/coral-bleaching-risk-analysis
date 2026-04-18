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
│   ├── 02_eda.ipynb
│   ├── 03_feature_selection.ipynb
│   └── 04_preprocessing_and_modelling.ipynb #in progress
├── outputs/
│   └── figures/
└── requirements.txt
```

## Status
🟡 In progress — Notebook 01 (Data loading and cleaning) complete. Notebook 02 (EDA) complete. Notebook 03 (Feature selection) complete. Notebook 04 (Preprocessing and modelling) in progress.

## Future Work
- Interactive map with temporal slider for bleaching severity evolution by site
- Overlay of bleaching data with SSTA and ocean current data
- Regional models (Atlantic, Indo-Pacific, Mediterranean) after global baseline
- LSTM for SST time series and missing value imputation
- Coupling of the bleaching risk classifier with an SST/DHW forecasting model 
  to predict bleaching risk under future climate scenarios, enabling site-specific 
  early warning and monitoring
- Validation against the 2024 global bleaching event as a qualitative 
  geographic check of model predictions

## Author
Giulia Balducci — Data Scientist | Materials Chemistry PhD
[LinkedIn](https://www.linkedin.com/in/giuliabalducci) | [GitHub](https://github.com/giulia-balducci) | [Kaggle](https://www.kaggle.com/giuliabalducci)
