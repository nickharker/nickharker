import pandas as pd

df = pd.read_csv('C:/Program Files/screen-scraper Enterprise Edition/oakley.csv', sep=',')
df = df.drop_duplicates(keep='first')
df.to_csv('C:/Users/nhark/Desktop/oakley_01-16-19.csv', sep=',')