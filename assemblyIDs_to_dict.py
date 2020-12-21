
import pandas as pd 
df_dict = pd.read_csv("MIPS_to_RRESv4_test.csv") 

#pd.read_csv("filename.csv") converts #N/A in row 1 of CSV (value row of dictionary) to NaN

#to remove columns starting with #N/A an empty list was made to contain every column in the  data frame with #N/A
 
na_columns = []

for c in df_dict.columns:

    if c.startswith("#N/A") :
        na_columns.append(c)
    
# Using an if loop the columns that start with #N/A were searched for and appended to na_columns     

df_dict = df_dict.drop(na_columns , axis = "columns")

# The columns contained in na_columns are removed from the data frame by using .drop(na_columns , axis = "columns")
# this solved an error which prevented a dictionary from being made when #N/A was present as the key in the data frame

assembly_dict = df_dict.to_dict(orient='list') # converts data frame to a dictionary. 
#orient ='list’ : dict like {column -> [values]}

assembly_dict = {k:v[0] for k,v in assembly_dict.items()} #removes square bracket around value



print(assembly_dict) #prints dictionary