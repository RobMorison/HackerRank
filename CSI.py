import pandas as pd


df = pd.read_csv('CSI_Data.csv')

df.describe()

#df is your dataframe
col_count = df.shape[1]
