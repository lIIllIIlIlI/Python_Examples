# Python expects each array to store one datatype
# If array stores one module, e.g. memory of MotM, the dataframe has to be reversed

# import pandas as pd
import pandas as pd
  
# list of strings
lst = ['Pmd', 'For', 'Geeks', 'is', 'portal', 'for', 'Geeks']
  
# list of int
lst2 = ["motm", 22, 33, 44, 55, 66, 77]
lst3 = ["sysm", 22, 33, 44, 55, 66, 77]
lst4 = ["NvM", 22, 33, 44, 55, 66, 77]
lst5 = ["abdc", 22, 33, 44, 55, 66, 77]
lists = [lst, lst2, lst3, lst4, lst5]

# Calling DataFrame constructor after zipping
# both lists, with columns specified
moduleNames = [list[0] for list in lists]

df = pd.DataFrame(list(zip(lst, lst2, lst3, lst4, lst5)), 
               columns=moduleNames, index=["a", "b", "c", "d", "e", "f", "g"])
df = df.T
# Add Row with incremented index:
# df.loc[len(df.index)] = ["NiRM", 22, 33, 44, 55, 66, 77]

# Add Row with specific index:
df.loc["NiRM"] = ["NiRM", 22, 33, 44, 55, 66, 77]
print(df)
