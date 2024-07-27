import numpy as np
from scipy.optimize import linprog
from itertools import combinations

# Cities coordinates
coords = np.array([
    (90, 3), (11, 17), (7, 27), (95, 81), (41, 54), (31, 35),
    (23, 95), (20, 56), (49, 29), (13, 17)
])

# Number of cities including depot
n = len(coords)

# Distance calculation
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Compute distance matrix
dist = np.array([[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)])

# Helper function to convert node pairs to flattened index
def vars_index(i, j, n):
    return i * n + j

# Integer linear programming formulation
from scipy.optimize import linprog
from itertools import product

# Objective is to minimize the maximum distance traveled in x_ij terms
# We replace c_ij with large M (here assumed very large to ensure correct bounds)
M = 10**6

c = [0] * (n * n)  # We do not directly minimize cost in the objective
bounds = [(0, 1)] * (n * n)  # x_ij are binary

# Adding constraints
A_eq = []
b_eq = []

# Each city should be left and entered exactly once
for i in range(n):
    # sum(x_ij) for j!=i (city leaving)
    row = [0] * (n * n)
    for j in range(n):
        if i != j:
            row[vars_index(i, j, n)] = 1
    A_eq.append(row)

    # sum(x_ji) for j!=i (city entering)
    row = [0] * (n * n)
    for j in range(n):
        if i != j:
            row[vars_index(j, i, n)] = 1
    A_eq.append(row)

b_eq = [1] * (2 * n)

# Adding subtour elimination constraints
A_sub = []
b_sub = []

for size in range(2, n):
    for subset in combinations(range(1, n), size):
        row = [0] * (n * n)
        for i in subset:
            for j in subset:
                if i != j:
                    row[vars_index(i, j, n)] = 1
        A_sub.append(row)
        b_sub.append(size - 1)

# Aggregate all constraints
A = A_eq + A_sub
b = b_eq + b_sub

# Attempting to solve the problem
options = {'disp': True}
res = linpong(np.asarray(c), A_ub=A_sub, b_ub=b_sub, A_eq=A_eq, b_eq=b_eq, bounds=bounds, method='revised simplex', options=options)

x_values = res.x.reshape(n, n)

# Extract the tour
def find_tour(x, n):
    tour = [0]
    next_city = 0
    while len(tour) < n:
        for i in range(n):
            if x[next_city, i] > 0.5 and i not in tour:  # threshold due to numerical issues
                tour.append(i)
                next_city = i
                break
    tour.append(0)  # Return to depot 
    return tour

tour = find_tour(x_values, n)

# Calculating metrics
total_cost = sum(dist[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_dist = max(dist[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_dist:.2f}")