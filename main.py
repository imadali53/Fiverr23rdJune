# All tables extracted in branch 1
# issue with some data converted to dates
# to remove the first heading column i.e 0, 1, 2, 3
import os
import pandas as pd
import camelot

# Set input and output folders
input_folder = 'PDFs/'
output_folder = 'folder4444'

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)

# Get list of PDF files in the input folder
pdf_files = [file for file in os.listdir(input_folder) if file.endswith('.pdf')]

for pdf_file in pdf_files:
    # Construct the paths for input and output files
    input_path = os.path.join(input_folder, pdf_file)
    output_path_prefix = os.path.join(output_folder, os.path.splitext(pdf_file)[0])

    # Read the PDF and extract all tables from the first page
    tables = camelot.read_pdf(input_path, pages='1', multiple_tables='all')

    for i, table in enumerate(tables):
        # Convert the data types to strings
        table.df = table.df.astype(str)

        # Save each table as a separate CSV file
        output_path = f"{output_path_prefix}_table{i+1}.csv"
        table.df.to_csv(output_path, index=False)
