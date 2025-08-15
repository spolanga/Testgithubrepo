import pandas as pd
import numpy as np
import matplotlib as plt


df_housing= pd.read_csv(r'C:/Users/sampath/Downloads/Housing.csv')
#print(df_housing.info())
#print(df_housing.head())
#print(df_housing.tail())
#print(df_housing.shape)
#print(df_housing.describe())#only shows statistics of an integer
#print(df_housing.loc[df_housing.duplicated()]) #to seew any duplicated rows
#print(df_housing.columns) #to see list of all columns
print(df_housing.isna().sum()) #will give me a  sum of all the rows with null values