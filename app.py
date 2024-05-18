import pandas as pd
import os

data = [
    {'name': 'John', 'age': 25, 'city': "losvegas"},
    {'name': 'Jane', 'age': 30, 'city': "newyork"},
    {'name': 'Jack', 'age': 35, 'city': "chicago"},
    {'name': 'Jill', 'age': 40, 'city': "boston"}
]

# Create DataFrame
df = pd.DataFrame(data)

# Ensure the folder exists
folder_name = 'data'
if not os.path.exists(folder_name):
    os.makedirs(folder_name)

# Save DataFrame to CSV in the specified folder
file_path = os.path.join(folder_name, 'data.csv')
df.to_csv(file_path, index=False)