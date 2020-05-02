import pandas as pd

# read dataframe and set first row as index
# Alternative: Let python insert another index that can be used by the iterator
peopleDataFrame = pd.read_csv(r'C:\\Users\\lukas\Documents\\GitHub\\Python_Examples\\Datascience\\people.cvs', index_col=0)
print("\nDataframe:\n{}\n".format(peopleDataFrame))

# print header
header = peopleDataFrame.columns.values
print("\nHeader:\n{}\n".format(header))

# print index
index = peopleDataFrame.index
print("\nindex:\n{}\n".format(index))

# data types
dataTypes = peopleDataFrame.dtypes
print("\nDatatypes:\n{}\n".format(dataTypes))

# extract specific column
specificColumn = peopleDataFrame.loc['Carl']
print("\nspecificColumn (Carl):\n{}\n".format(specificColumn))

# snip some part of the dataframe
snipped = peopleDataFrame.loc['Alexa':'Carl', 'Sex':'Age']
print("\nsnipped:\n{}\n".format(snipped))

# extract specific cell
snipped = peopleDataFrame.loc['Alexa', 'Sex']
print("\nsnipped (Sex of Alexa):\n{}\n".format(snipped))

# extract specific row

# Filter for Sex
males = peopleDataFrame.loc[peopleDataFrame['Sex'] == "M"]
print("\nFilteres people (males only):\n{}\n".format(males))

# Sort by Age
ageSortedPeople = peopleDataFrame.sort_values(['Age'])
print("\nPeople sorted by age:\n{}\n".format(ageSortedPeople))

# add row

# add column

# Change cell (Berts birthday)
peopleDataFrame.loc['Bert', 'Age'] += 1
print("\nPeople after Berts birthday:\n{}\n".format(peopleDataFrame))

# sum
weightSum = peopleDataFrame.loc[:, ['Weight']].sum()
print("\nSum of all weights:\n{}\n".format(weightSum))

# store changes to cvs
# peopleDataFrame.to_csv('C:\\Users\\lukas\Documents\\GitHub\\Python_Examples\\Datascience\\people.cvs', index=False)

