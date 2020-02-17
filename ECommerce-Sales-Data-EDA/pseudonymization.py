import pandas as pd
from random import choices
from string import ascii_uppercase

def pseudonymization(dataframe, list_to_be_replaced, list_to_replace):
    if len(list_to_be_replaced) == len(list_to_replace):
        replace_dict = dict(zip(list_to_be_replaced, list_to_replace))
        dataframe.replace(to_replace=replace_dict,
                          inplace= True)
        return dataframe
    else:
        print("List lengths are not equal!")
    
# Example
# load data
orders = pd.read_csv("Orders - Analysis Task.csv")

# create lists
three_letter_titles = ["".join(choices(ascii_uppercase, k=3)) for i in range(49)]
product_titles = orders["product_title"].value_counts().index.tolist()

# apply function
pseudonymization(orders, product_titles, three_letter_titles)

# save into csv
orders.to_csv("Orders - Analysis Task.csv", index=False)