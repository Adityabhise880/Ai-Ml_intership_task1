import pandas as pd
import seaborn as sns # We will use this to grab the dataset easily


df = sns.load_dataset('titanic')


print("Data loaded successfully!")

print("------ step 1: structure ----------")
print("first 5 rows of the dataset:")

print(df.head())

print("\n last few rows of the dataset:")
print(df.tail())
print("\n ----step 2 & 3: info and stat----")

print(df.info())
print("\n  statistical summery ")
print(df.describe()) 

print("-----step 4 unique values-------")

print("unique classes:", df['class'].unique)

print("Unique Decks:", df['deck'].unique())
print("Unique Embarked locations:", df['embarked'].unique())