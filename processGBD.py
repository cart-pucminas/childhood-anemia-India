
import pandas as pd
import os 
import glob 


# for each sheet:
#     columns:
#     Location,Year,Age,Sex,Cause of death or injury,Value,

#     NewDf:
#     Location;Year;NameAtributte;
#     NameAtributte = Cause of death + Age
#     NameAtributteValue = Value

# Concat all indicators by Location, Year



def process(df):
    df.dropna(subset=['Year'], inplace=True)
    df['Year'] = df['Year'].astype('int')
    df['Value'] = df['Value'].astype('float')

    nameColumn = str(df['Cause of death or injury'][0]) + '|' + str(df['Sex'][0]) + '|' + str(df['Age'][0])
    df.pop('Age')
    df.pop('Cause of death or injury')
    df.pop('Measure')
    df.pop('Sex')
    df.pop('Lower bound')
    df.pop('Upper bound')
    df['regionName'] = 'Asia'

    # I will use countryName for the system execution, but this column will be stateName
    df.rename(columns={"Value": nameColumn, 'Year': 'year', 'Location': 'countryName'}, inplace=True)
    df = df[['regionName', 'countryName', 'year', nameColumn]]
    return df


csv_files = glob.glob("GBD Database/*.csv")
datas = pd.read_csv("GBD DatabaseOutput/A.7.4Dietary iron deficiency.csv")
datas = process(datas)

for f in csv_files:
    df = pd.read_csv(f)
    df = process(df)
    datas = pd.merge(datas, df, how='left', on=['regionName', 'year', 'countryName'])
    
print(datas)
print(datas)
df.dropna(inplace=True)
datas.to_csv("base.csv", sep=';')

