#%%

import pandas as pd
import pyam
import pint

# Baseline_results=pd.read_csv('results/GLUCOSE_Baseline.csv')

# IAMC_glucose = pyam.IamDataFrame(Baseline_results)
# capacity=IAMC_glucose.convert_unit('TW', to='GW').timeseries()

# IAMC_glucose2 = pyam.IamDataFrame(capacity)
# emissions=IAMC_glucose2.convert_unit('Gt CO2e/yr', to='Mt CO2e/yr').timeseries()

# emissions.to_csv('results/GLUCOSE_Baseline_ConvertedUnits.csv')


Total_results=pd.read_csv('results/TotalCCG.csv')

IAMC_glucose = pyam.IamDataFrame(Total_results)
capacity=IAMC_glucose.convert_unit('TW', to='GW').timeseries()

IAMC_glucose2 = pyam.IamDataFrame(capacity)
emissions=IAMC_glucose2.convert_unit('Gt CO2e/yr', to='Mt CO2e/yr').timeseries()

emissions.to_csv('results/TotalCCG_ConvertedUnits.csv')

# %%
