import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

tweet_path = './datasets/russian-troll-tweets/IRAhandle_tweets_{}.csv'
df = pd.read_csv(tweet_path.format('1'))
print("LOG: initial import complete")

for i in range(2,14):
    df_next = pd.read_csv(tweet_path.format(str(i)))
    df = df.append(df_next, ignore_index=True)
    print("LOG: import/append sheet {} complete".format(str(i)))

df.to_csv('./datasets/russian-troll-tweets/combined.csv', index=False)
print("LOG: dataframe saved")
print(df.shape)
print(df.head())
print(df.describe())
print(df.info())