import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

df=pd.read_csv('athlete_events.csv')

print(df.describe())
print(df.describe(include='object'))
print(df.isna().sum())
print(df.duplicated())
df.drop_duplicates(inplace=True)

print(df.corr(numeric_only=True))

sns.heatmap(df.corr(numeric_only=True))
plt.show()

#Participants each year
df_grp_team=df.groupby('Year')['ID'].count()
print(df_grp_team)

df_grp_team.plot(kind='bar')
plt.title('Number of participants over the years')
plt.xlabel('Year')
plt.ylabel('Number of participants')
plt.show()

#Medals by age 
df_medal_age=df.groupby('Age')['Medal'].count()
print(df_medal_age)

df_medal_age.plot(kind='bar')
plt.title('Medals per age')
plt.xlabel('Age')
plt.ylabel('medal')
plt.show()

#Atletes average weight
df_av_weight=df.Weight.mean()
print(df_av_weight)

df_medal_weight=df.groupby('Sex')['Weight'].mean()
print(df_medal_weight)

df_medal_weight.plot(kind='bar')
plt.title('Weight by sex')
plt.xlabel('sex')
plt.ylabel('weight')
plt.show()

#athlete average height
df_av_height=df.Height.mean()
print(df_av_height)

df_medal_height=df.groupby('Sex')['Height'].mean()
print(df_medal_height)

df_medal_height.plot(kind='bar')
plt.title('Medals per age')
plt.xlabel('Medals')
plt.ylabel('medal')
plt.show()

#medals for each sport of each country
df_medal_country=df.groupby(['NOC','Sport'])['Medal'].count()
df_medal_country.plot(kind='bar')
plt.title('Medals by country')
plt.xlabel('Country')
plt.ylabel('Medals')
plt.xticks(rotation=45)
plt.show()

# Working on South African athletes
df_SA=df[df['Team']== 'South Africa']
print(df_SA.shape)

#droping columns with info that is not needed

df_SA=df_SA.drop(['Team'], axis=1)
df_SA=df_SA.drop('NOC', axis=1)
df_SA=df_SA.drop('Games', axis=1)

#filling null values in Medal's column where zero mean zero medals'
#df_SA['Medal'].fillna(0, inplace=True)

#working on column with null values
df_SA['Age']=df_SA['Age'].fillna(df_SA.Age.mean())
df_SA['Height']=df_SA['Height'].fillna(df_SA.Height.mean())
df_SA['Weight']=df_SA['Weight'].fillna(df_SA.Weight.mean())

#checking and dropping duplicated data
print(df_SA.duplicated().sum())
df_SA.drop_duplicates(inplace=True)

sns.countplot(data=df_SA, x='Sex')
plt.title('Number of Males and Females')
plt.show()

#medals by sex
df_grp_sex=df_SA.groupby('Sex')['Medal']
print(df_grp_sex.count())

sns.countplot(data=df_SA.dropna(), x='Medal')
plt.title('Medals distribution')
plt.show()

sns.histplot(data=df_SA, x='Age', bins=20)
plt.title('Age distribution')
plt.title
plt.show()

#number medals by sport
df_grp=df_SA.groupby('Sport')['Medal']

print(df_grp.count())
