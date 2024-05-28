import os
import pandas as pd

def process_dat_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    headers = lines[0].strip().split()

    data = []
    for line in lines[1:]:
        parts = line.strip().split()
        job_title = ' '.join(parts[4:-2])
        record = parts[:4] + [job_title] + parts[-2:]
        data.append(record)

    df = pd.DataFrame(data, columns=headers)
    return df

directory_path = "C:/Users/HP/Downloads/New folder/input/"

file_paths = [os.path.join(directory_path, file) for file in os.listdir(directory_path) if file.endswith('.dat')]

combined_df = pd.DataFrame()

for file_path in file_paths:
    df = process_dat_file(file_path)
    combined_df = pd.concat([combined_df, df], ignore_index=True)

combined_df['basic_salary'] = pd.to_numeric(combined_df['basic_salary'])

average_salaries = combined_df['basic_salary'].mean()

unique_salaries = combined_df['basic_salary'].drop_duplicates().sort_values(ascending=False)

if len(unique_salaries) > 1:
    second_highest_salary = unique_salaries.iloc[1]
else:
    second_highest_salary = 'N/A'  

footer = pd.DataFrame([['', '', '', '', f'mean salary {average_salaries}', f'second highest salary {second_highest_salary}', '']], columns=combined_df.columns)

combined_df = pd.concat([combined_df, footer], ignore_index=True)

directory_path = "C:/Users/HP/Downloads/New folder/output"
output_file_path = os.path.join(directory_path, 'result.csv')
combined_df.to_csv(output_file_path, index=False)

print(combined_df)
