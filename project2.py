import pandas as pd
import seaborn as sns


df=pd.read_csv('Weather.csv')
#df=df.drop('country_name', axis=1)
print(df.info())
#print(df.fillna(df.mean()))
df['date']=df['Date/Time'].str.split(pat=' ').str[0]

df['month']=df['date'].str.split(pat='/').str[0]
df['day']=df['date'].str.split(pat='/').str[1]
df['time']=df['Date/Time'].str.split(pat=' ').str[1]

df=df.drop('Date/Time', axis=1)
df=df.drop('date', axis=1)

 #converting to int

df=df.astype({'month':'int', 'day':'int'})

#print(df.describe())
#average wind temp, by month

print(df.groupby('month')['Temp_C'].mean())


#percentage of a clear weather
df_clear_perc=(df[df.Weather=='Clear'].value_counts().sum()/df.Weather.value_counts().sum())*100

print(df_clear_perc)

#averager temperature on a clear weather
df_clear=df[df.Weather=='Clear']
print(df_clear.Temp_C.mean())

#clear weather is mostly found on which month? How many times?
print(df_clear.groupby('month')['Weather'].value_counts())
print(df_clear.groupby('month')['Weather'].value_counts().max())

print(df_clear.groupby('time')['Temp_C'].mean())


sns.histplot(df.Weather)

#print(df.head(5))