#---------------

#imports csv file, takes out percent signs and converts the numbers to decimal representation
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

#---------------

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



#below code imports a csv file and converts values in a given column to a format PostgreSQL can accept
import csv
from datetime import datetime

input_file = 'input.csv'  # Replace with your input CSV file name
output_file = 'output.csv'  # Replace with your output CSV file name
input_column_index = 2  # Replace with the index of the column containing timestamps (0-based)

input_format = "%d-%m-%y %H:%M"
output_format = "%Y-%m-%d %H:%M:%S"

output_data = []

with open(input_file, 'r') as csv_input:
    csv_reader = csv.reader(csv_input)
    for row in csv_reader:
        if len(row) > input_column_index:
            timestamp_string = row[input_column_index]
            try:
                parsed_datetime = datetime.strptime(timestamp_string, input_format)
                formatted_timestamp = parsed_datetime.strftime(output_format)
                row[input_column_index] = formatted_timestamp
            except ValueError:
                pass  # Handle invalid timestamps here if needed
        output_data.append(row)

with open(output_file, 'w', newline='') as csv_output:
    csv_writer = csv.writer(csv_output)
    csv_writer.writerows(output_data)

print("Conversion complete.")

#below code removes double quotation marks from values in a specified column
import csv

input_file = 'input.csv'  # Replace with your input CSV file name
output_file = 'output.csv'  # Replace with your output CSV file name
column_index = 2  # Replace with the index of the column to process (0-based)

output_data = []

with open(input_file, 'r') as csv_input:
    csv_reader = csv.reader(csv_input)
    for row in csv_reader:
        if len(row) > column_index:
            value = row[column_index]
            if value.startswith('"') and value.endswith('"'):
                row[column_index] = value[1:-1]  # Remove double quotation marks
        output_data.append(row)

with open(output_file, 'w', newline='') as csv_output:
    csv_writer = csv.writer(csv_output)
    csv_writer.writerows(output_data)

print("Double quotation marks removed from column in the CSV file.")
