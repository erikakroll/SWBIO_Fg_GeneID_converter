
import pandas as pd 
df_dict = pd.read_csv("MIPS_to_RRESv4_test.csv") 

#pd.read_csv("filename.csv") converts #N/A in the 2nd row (key row of dictionary) to NaN

#to remove columns starting with #N/A an empty list was made to contain every column in the 
# data frame with #N/A
# These columns of data now contained in na_columns was removed from the 
# data frame by using .drop(na_columns , axis = "columns")
# this solved an error which prevent a dictionary from being made
# when #N/A was present as the key in the dataframe

na_columns = []

for c in df_dict.columns:

    if c.startswith("#N/A") :
        na_columns.append(c)
    
    

df_dict = df_dict.drop(na_columns , axis = "columns")



assembly_dict = df_dict.to_dict(orient='list')

assembly_dict = {k:v[0] for k,v in assembly_dict.items()}

#Printing dict showed it had a square bracket around value
#removed by adding code assembly_dict = {k:v[0] for k,v in assembly_dict.items()}

print(assembly_dict) 