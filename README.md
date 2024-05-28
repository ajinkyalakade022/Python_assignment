Data Processing Script
This script processes multiple .dat files from a specified directory, consolidates the data into a single CSV file, and calculates overall statistics like the average salary and the second-highest salary.

Requirements
Python 3.x
pandas library
Installation
Ensure Python is installed. You can download it from python.org.

Install the pandas library if you haven't already:

bash
Copy code
pip install pandas
Usage
Place all your .dat files in a directory (e.g., C:/Users/HP/Downloads/New folder/input/).
Update the directory_path variable in the script to point to your directory containing the .dat files.
Run the script. The output will be a CSV file named combined_output.csv in the same directory.
Script Details
Function process_dat_file(file_path)
Reads a .dat file.
Extracts headers and processes each line to correctly format the job title.
Returns a DataFrame containing the data from the file.
Main Script
Sets the directory path containing .dat files.
Lists all .dat files in the specified directory.
Initializes an empty DataFrame to hold combined data.
Iterates over each file, processes it using process_dat_file, and concatenates the results.
Converts the basic_salary column to numeric.
Calculates the average salary.
Finds the second-highest unique salary.
Creates a footer row with the average and second-highest salaries.
Appends the footer row to the combined DataFrame.
Writes the combined DataFrame to a CSV file named combined_output.csv.
Prints the combined DataFrame to the console.
Example Output
The output CSV file (combined_output.csv) will have the combined data from all the .dat files, along with a footer row containing the average salary and the second-highest salary.

Notes
The script assumes the .dat files have a consistent format with headers on the first line.
The basic_salary column must contain numeric values for accurate calculations.
