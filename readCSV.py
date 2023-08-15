import pandas as pd

csv_file_path = 'enter/file/path/here'
df = pd.read_csv(csv_file_path)

columns_with_percent = ['Enter column name with percent symbols']
columns_with_equals = ['Enter column name with equal symbols']

#removes % symbol from columns listed in columns_with_percent
for column in columns_with_percent:
    if df[column].dtype == 'O':
        df[column] = df[column].str.rstrip('%')  # Remove percent sign
        df[column] = df[column].apply(lambda x: float(x) / 100.0 if x != 'N.A.' else x)  # Convert to float if not 'N/A'


# Remove '=' from the columns listed in column_with_equals
for column in columns_with_equals:
    df[column] = df[column].str.replace('=', '')

output_csv_file_path = 'enter/file/path/here'
df.to_csv(output_csv_file_path, index=False)


#below code rounds all decimals in given columns to two decimal places
import pandas as pd

csv_file_path = 'enter/file/path/here'
output_csv_file_path = 'enter/file/path/here'

# Read the CSV file
df = pd.read_csv(csv_file_path)

# List of columns to be rounded
columns_to_round = ['YearlyChange', 'UrbanPop%', 'WorldShare']

# Round values in the specified columns to two decimal places
df[columns_to_round] = df[columns_to_round].round(2)

# Save the modified DataFrame to a new CSV file
df.to_csv(output_csv_file_path, index=False)

#code for importing csv file and returning max value of a given column

import pandas as pd

# Read the CSV file into a pandas DataFrame
df = pd.read_csv('Enter/File/Path')

# Get the maximum value in a specific column
column_name = 'Production'
max_value = df[column_name].max()

print(f"The highest value in column '{column_name}' is: {max_value}")


#---------------

#imports csv file, takes out blank spaces from all columns/rows and produces a new file that saves
#to desktop  

import csv

input_file = 'Enter/File/Path'  # Replace with your CSV file path
output_file = 'Enter/File/Path'  # Replace with the desired output file path

with open(input_file, 'r') as file_in, open(output_file, 'w', newline='') as file_out:
    reader = csv.reader(file_in)
    writer = csv.writer(file_out)

    for row in reader:
        processed_row = [cell.strip() if isinstance(cell, str) else cell for cell in row]
        writer.writerow(processed_row)

#----------------

#imports csv file, removes column of choice

import csv

input_file = 'Enter/File/Path'  # Replace with your input CSV file path
output_file = 'Enter/File/Path'  # Replace with the desired output CSV file path
column_to_remove = 'Enter column to remove'  # Replace with the column name to be removed

with open(input_file, 'r', newline='') as file_in, open(output_file, 'w', newline='') as file_out:
    reader = csv.DictReader(file_in)
    fieldnames = reader.fieldnames

    # Exclude the column to be removed from the fieldnames
    fieldnames = [field for field in fieldnames if field != column_to_remove]

    writer = csv.DictWriter(file_out, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        # Exclude the column to be removed from each row
        modified_row = {field: row[field] for field in fieldnames}
        writer.writerow(modified_row)