import matplotlib.pyplot as plt
import numpy as np

# Data extraction
problem_types = [
    "single TSP", "single BTSP", "single GTSP", "single KTSP",
    "multiple mTSP", "multiple mTSP MinMax", "multiple mTSPMD", "multiple CVRP"
]
strategies = ["A_First", "B_Debugging", "C_Overall"]

# Optimality Gaps (mean ± std)
opt_gaps = [
    [8.69, 10.66, 8.94],
    [47.77, 46.68, 46.58],
    [15.91, 16.37, 15.77],
    [161.42, 160.72, 157.95],
    [56.44, 59.63, 47.87],
    [23.15, 32.45, 46.11],
    [0, 52.40, 71.06],
    [66.72, 62.47, 60.07]
]
std_devs = [
    [5.01, 4.88, 3.97],
    [33.52, 30.61, 29.43],
    [6.36, 4.12, 2.29],
    [7.85, 11.78, 10.14],
    [18.42, 28.54, 19.40],
    [11.53, 18.57, 18.11],
    [0.00, 15.93, 6.16],
    [56.07, 32.60, 32.21]
]

# Plotting
x = np.arange(len(problem_types))  # the label locations
width = 0.25  # the width of the bars

fig, ax = plt.subplots(figsize=(15, 8))
bars1 = ax.bar(x - width, [g[0] for g in opt_gaps], width, yerr=[s[0] for s in std_devs], label='A_First', capsize=5)
bars2 = ax.bar(x, [g[1] for g in opt_gaps], width, yerr=[s[1] for s in std_devs], label='B_Debugging', capsize=5)
bars3 = ax.bar(x + width, [g[2] for g in opt_gaps], width, yerr=[s[2] for s in std_devs], label='C_Overall', capsize=5)

# Labels and titles
ax.set_xlabel('Problem Types')
ax.set_ylabel('Optimality Gap (%)')
ax.set_title('Optimality Gap by Problem Type and Strategy')
ax.set_xticks(x)
ax.set_xticklabels(problem_types, rotation=45, ha="right")
ax.legend()

plt.tight_layout()
plt.show()
