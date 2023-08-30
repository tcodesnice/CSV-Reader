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

#imports csv file, takes out blank spaces from all columns/rows and produces a new file that saves to desktop  

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


#----------------------------
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

#----------------

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


#----------------

#imports csv file, removes commas from column of choice
import pandas as pd

# Define the paths for input and output CSV files
input_csv_file_path = '/path/to/input/file.csv'
output_csv_file_path = '/path/to/output/file.csv'

# Load the CSV file into a DataFrame
df = pd.read_csv(input_csv_file_path)

# Specify the name of the column where you want to remove commas
target_column = 'Column_Name'  # Replace with the actual column name

# Remove commas from the specified column
df[target_column] = df[target_column].str.replace(',', '')

# Save the modified DataFrame to a new CSV file
df.to_csv(output_csv_file_path, index=False)

print(f"Commas removed from '{target_column}' column and saved to '{output_csv_file_path}'.")

#----------------
#takes csv file as input and outputs csv file with columns that contain dates conveted into days of the week
import csv
from datetime import datetime

# Function to convert a date string to the day of the week
def get_day_of_week(date_string):
    weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    date_obj = datetime.strptime(date_string, '%Y-%m-%d')
    day_of_week = weekdays[date_obj.weekday()]
    return day_of_week

# Column containing cleaned date values
cleaned_date_column = 'cleaned_date'  # Change this to the actual cleaned date column name

# Input and output file names
input_file = 'input.csv'
output_file = 'output.csv'

# Read input CSV and write to output CSV with day of the week added
with open(input_file, 'r', newline='') as csv_input, open(output_file, 'w', newline='') as csv_output:
    reader = csv.DictReader(csv_input)
    fieldnames = reader.fieldnames + ['day_of_week']
    
    writer = csv.DictWriter(csv_output, fieldnames=fieldnames)
    writer.writeheader()
    
    for row in reader:
        cleaned_date_value = row[cleaned_date_column]
        day_of_week = get_day_of_week(cleaned_date_value)
        row['day_of_week'] = day_of_week
        writer.writerow(row)

print("Conversion completed. Output CSV file:", output_file)

#---------------
#code below removes all commas and quotation marks from given csv file

import csv

def clean_csv(input_file, output_file):
    with open(input_file, 'r', newline='', encoding='utf-8') as infile:
        reader = csv.reader(infile)
        header = next(reader)  # Read the header
        
        cleaned_rows = []
        for row in reader:
            cleaned_row = [column.replace(',', '').replace('"', '') for column in row]
            cleaned_rows.append(cleaned_row)

    with open(output_file, 'w', newline='', encoding='utf-8') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(header)
        writer.writerows(cleaned_rows)

if __name__ == '__main__':
    input_csv = 'input/csv/filepath'  # Replace with your input CSV filename
    output_csv = 'output/csv/filepath'  # Replace with your desired output CSV filename
    
    clean_csv(input_csv, output_csv)
    print(f'Cleaned CSV saved as {output_csv}')

