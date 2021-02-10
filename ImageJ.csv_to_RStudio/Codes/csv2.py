import os
from glob import glob
import pandas as pd


files = glob('*_*_S*.csv')
df = []
for f in files:
    df.append(pd.read_csv(f))

#files = os.listdir()
#csvs = []
#for f in files:
#    csvs.append(pd.read_csv(f))

# or [pd.read_csv(f) for f in files]

#pd.read_csv() for CSV files
#    dataframe = pd.read_csv('/home/bragatte/Downloads/pycharm-community-2019.1.3/3.ImunoinfoCSVs/test')
