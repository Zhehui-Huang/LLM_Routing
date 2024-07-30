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
    with open(file_path, 'r') as f:
        lines = f.readlines()
        current_problem = None
        for line in lines:
            line = line.strip()
            if line and ':' in line:
                if line.startswith('gpt4/zero/'):
                    parts = line.split('/')
                    current_problem = f"{parts[2]}_{parts[3]}"
                else:
                    problem_type, values = line.split(':', 1)
                    values = list(map(float, re.findall(r"[-+]?\d*\.\d+|\d+", values)))
                    if current_problem not in data:
                        data[current_problem] = []
                    data[current_problem].extend(values)
    return data


# Process data
def calculate_stats(data):
    stats = {}
    for key, values in data.items():
        if values:  # Check if there are values
            mean = np.mean(values)
            std = np.std(values)
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

    for key in opt_gap_stats.keys():
        opt_gap_mean, opt_gap_std = opt_gap_stats[key]
        success_mean, success_std = success_stats.get(key, (np.nan, np.nan))

        summary.append({
            'Problem Type': key,
            'Strategy': method.replace('pass_', '').capitalize().replace('_', ' '),
            'Opt. Gap': f"{opt_gap_mean:.2f} ± {opt_gap_std:.2f}" if not np.isnan(opt_gap_mean) else '-',
            'Success Rate': f"{success_mean * 100:.2f} ± {success_std * 100:.2f}" if not np.isnan(success_mean) else '-'
        })

# Convert to DataFrame
df_summary = pd.DataFrame(summary)
df_summary.sort_values(by=['Problem Type', 'Strategy'], inplace=True)

# Display
print(df_summary)

# Save to CSV if needed
df_summary.to_csv('summary.csv', index=False)
