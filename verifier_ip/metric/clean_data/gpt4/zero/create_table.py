import numpy as np
import pandas as pd
import re

# File paths
files = {
    'pass_one': {
        'opt_gap': 'pass_one/all_opt_gap.txt',
        'success': 'pass_one/all_success.txt'
    },
    'pass_debug': {
        'opt_gap': 'pass_debug/all_opt_gap.txt',
        'success': 'pass_debug/all_success.txt'
    },
    'pass_overall': {
        'opt_gap': 'pass_overall/all_opt_gap.txt',
        'success': 'pass_overall/all_success.txt'
    }
}


# Load data
def load_data(file_path):
    data = {}
    current_problem = None
    with open(file_path, 'r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line.startswith('gpt4/zero/'):
                parts = line.split('/')
                current_problem = f"{parts[3]}_{parts[4]}"
            elif current_problem and line and ':' in line:
                problem_type, values = line.split(':', 1)
                values = list(map(float, re.findall(r"[-+]?\d*\.\d+|\d+", values)))
                # key = f"{current_problem}_{problem_type.strip().replace(':', '')}"
                key = f"{current_problem}"
                key = key.replace(':', '')
                if key not in data:
                    data[key] = []
                data[key].extend(values)
    return data


# Process data
def calculate_stats(data):
    stats = {}
    for key, values in data.items():
        if values:  # Check if there are values
            mean = np.mean(values)
            std = np.std(values)
            if len(values) == 1:
                std = 0.0  # Set std to 0 if there's only one value
            stats[key] = (mean, std)
        else:
            stats[key] = (np.nan, np.nan)  # Handle cases with no values
    return stats


# Create summary
summary = []

for method, paths in files.items():
    opt_gap_data = load_data(paths['opt_gap'])
    success_data = load_data(paths['success'])

    opt_gap_stats = calculate_stats(opt_gap_data)
    success_stats = calculate_stats(success_data)

    for key in set(opt_gap_stats.keys()).union(success_stats.keys()):
        opt_gap_mean, opt_gap_std = opt_gap_stats.get(key, (np.nan, np.nan))
        success_mean, success_std = success_stats.get(key, (np.nan, np.nan))

        if key is not None:
            problem_type_parts = key.split('_')
            problem_type = problem_type_parts[0]
            subproblem = ' '.join(problem_type_parts[1:]).replace('_', ' ')
            strategy = method.replace('pass_', '').capitalize().replace('_', ' ')
            if strategy == 'One':
                strategy = 'A_First'
            elif strategy == 'Debug':
                strategy = 'B_Debugging'
            elif strategy == 'Overall':
                strategy = 'C_Overall'

            summary.append({
                'Problem Type': f"{problem_type} {subproblem}",
                'Strategy': strategy,
                'Opt. Gap': f"{opt_gap_mean:.2f} ± {opt_gap_std:.2f}" if not np.isnan(opt_gap_mean) else '-',
                'Success Rate': f"{success_mean * 100:.2f} ± {success_std * 100:.2f}" if not np.isnan(
                    success_mean) else '-'
            })

# Convert to DataFrame
df_summary = pd.DataFrame(summary)
# df_summary.sort_values(by=['Problem Type', 'Strategy'], inplace=True)

# Display
# print(df_summary)




# Define the custom order for the Problem Type
problem_type_order = [
    "single TSP", "single BTSP", "single GTSP", "single KTSP",
    "multiple mTSP", "multiple mTSP MinMax", "multiple mTSPMD", "multiple CVRP"
]

# Create a categorical type with the custom order
df_summary['Problem Type'] = pd.Categorical(df_summary['Problem Type'], categories=problem_type_order, ordered=True)

# Sort the DataFrame by the custom order and Strategy
df_summary.sort_values(by=['Problem Type', 'Strategy'], inplace=True)

# Display the sorted DataFrame
print(df_summary)

# Save the sorted DataFrame to CSV if needed
df_summary.to_csv('sorted_summary.csv', index=False)

# Save to CSV if needed
# df_summary.to_csv('summary.csv', index=False)
