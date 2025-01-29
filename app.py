import pandas as pd
# Read data from a csv
data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
print(data_frame)

# Series
data = pd.Series([23,45,7,34,6,63,36,78,54,34])
print(data)

# Date Range
date_range = pd.date_range('2021-05-01','2021-05-12')
print(date_range)

# Series Apply
def divide(x):
    return x/2
my_series = pd.Series([2,4,6,8,10])
print(my_series.apply(divide))

# DataFrames from list

data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porsche", "Cayenne", "White"]]
df = pd.DataFrame(data,columns=['Brand','Model','Color'])
print(df)

# DataFrames from dict
data_list_dict = data = [
    { 
        "brand": "Toyota", 
        "model": "Corolla",
        "color": "Blue"
    },
    {
        "brand": "Ford", 
        "model": "K",
        "color": "Yellow"
    },
    {
        "brand": "Porsche", 
        "model": "Cayenne",
        "color": "White"
    },
    {
        "brand": "Tesla", 
        "model": "Model S",
        "color": "Red"
    }
]
df = pd.DataFrame(data_list_dict)
print(df)

# DataFrame iLoc
print(data_frame.iloc[133,6])

# DataFrame Head
print(data_frame.head(3))

# DataFrame Tail
print(data_frame.tail(3))

# Print Columns
print(data_frame[['Name','Type 1']].head(10))

# Loc Function
print(data_frame.loc[data_frame['Attack']>80])

#Filter and Count
print(len(data_frame.loc[data_frame['Legendary']==True]))

# Clean Datasets
baby_names = pd.read_csv('.learn/assets/us_baby_names_right.csv')
print(baby_names.head(5))

# Remove Columns
baby_names.drop(columns=baby_names.columns[0],axis=1,inplace=True)
print(baby_names.head(5))

# Value Counts
print(baby_names.value_counts('Gender'))

# Group By
print(len(baby_names.groupby('Name').sum()))





