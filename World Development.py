import numpy as np
import pandas as pd

wdi = pd.read_csv(
    "https://media.githubusercontent.com/media/nickeubank/MIDS_Data/master/World_Development_Indicators/wdi_small_tidy_2015.csv"
)

subset = wdi[
    [
        "Mortality rate, infant (per 1,000 live births)",
        "GDP per capita (constant 2010 US$)",
        "Country Name",
    ]
]


import matplotlib as plt

subset.plot.scatter(
    x="GDP per capita (constant 2010 US$)",
    y="Mortality rate, infant (per 1,000 live births)",
)
