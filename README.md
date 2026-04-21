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
│   ├── raw/                              # original data (not tracked by Git)
│   └── processed/
│       ├── bleaching_clean.csv           # cleaned dataset
│       ├── bleaching_feature_selection.csv
│       ├── atlantic_sites_latest.csv     # one row per site (dashboard map)
│       └── atlantic_sites_history.csv    # all observations per site (dashboard history panel)
├── notebooks/
│   ├── 01_data_loading_and_cleaning.ipynb
│   ├── 02_eda.ipynb
│   ├── 03_feature_selection.ipynb
│   ├── 04_preprocessing_and_modelling.ipynb
│   └── 05_atlantic_model.ipynb
├── models/
│   ├── rf_atlantic_model.pkl
│   └── rf_atlantic_preprocessor.pkl
├── outputs/
│   └── figures/
└── requirements.txt
```

## Status
🟡 In progress — Notebooks 01–05 complete. Streamlit dashboard in progress.

Notebook 05 covers: Atlantic regional model (RF + SMOTE), substrate ablation, SHAP interpretability, error analysis, model saving, and dashboard data export.

## Key Results
- Global binary model (Random Forest + SMOTE): bleaching recall 0.64, macro F1 0.73
- Atlantic regional model (no substrate): bleaching recall 0.78, macro F1 0.69
- Error analysis: Atlantic FN rate 0.22 (vs 0.39 global), FP rate 0.31 (vs 0.34 global)
- Root cause of global model bias: Pacific major bleaching events (2016, 2020, 2022, 2024) fall outside the training window

## Future Work
- Extended dataset (post-2020) to capture Pacific bleaching events (2020, 2022, 2024)
  — required for a meaningful Pacific regional model
- Regional models (Indo-Pacific, Mediterranean) after Atlantic model is validated
- Interactive map with temporal slider for bleaching severity evolution by site
- Overlay of bleaching data with SSTA and ocean current data
- LSTM for SST time series and missing value imputation
- Coupling of the bleaching risk classifier with an SST/DHW forecasting model 
  to predict bleaching risk under future climate scenarios, enabling site-specific 
  early warning and monitoring
- Validation against the 2024 global bleaching event as a qualitative 
  geographic check of model predictions

## Author
Giulia Balducci — Data Scientist | Materials Chemistry PhD
[LinkedIn](https://www.linkedin.com/in/giuliabalducci) | [GitHub](https://github.com/giulia-balducci) | [Kaggle](https://www.kaggle.com/giuliabalducci)
