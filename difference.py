import pickle
import pandas as pd
from statsmodels.tsa.stattools import adfuller
from arch.unitroot import PhillipsPerron
from statsmodels.tsa.stattools import kpss


# Make the time series stationary using ADF test
def make_stationary(timeseries, alpha=0.05):
    df = timeseries.copy()
    
    # ADF Test
    differences = 0
    result = adfuller(df)
    p_value = result[1]
    if p_value < alpha:
      print(f"ADF test: P-value {p_value} at difference {differences}.")
    else:
      while p_value > alpha:
          df = df.diff().dropna()
          result = adfuller(df)
          p_value = result[1]
          differences += 1
          print(f"ADF test: P-value {p_value} at difference {differences}.")
    
    # PP Test
    df = timeseries.copy()  # Reset df for PP test
    differences = 0
    result = PhillipsPerron(df)
    p_value = result.pvalue
    if p_value < alpha:
      print(f"PP test: P-value {p_value} at difference {differences}.")
    else:
      while p_value > alpha:
          df = df.diff().dropna()
          result = PhillipsPerron(df)
          p_value = result.pvalue
          differences += 1
          print(f"PP test: P-value {p_value} at difference {differences}.")
    
    # KPSS Test
    df = timeseries.copy()  # Reset df for KPSS test
    differences = 0
    result = kpss(df, regression='ct')
    p_value = result[1]
    if p_value > alpha:
      print(f"KPSS test: P-value {p_value} at difference {differences}.")
    else:
      while p_value < alpha:
          df = df.diff().dropna()
          result = kpss(df, regression='ct')
          p_value = result[1]
          differences += 1
          print(f"KPSS test: P-value {p_value} at difference {differences}.")
    
    return df.head(5)  # Return the stationary time series
