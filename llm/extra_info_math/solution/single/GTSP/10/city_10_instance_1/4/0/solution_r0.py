import math
from pulp import *

# City coordinates keyed by city index
city_coords = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Grouping of cities
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Count clusters
k = len(city_groups)

# Function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create the problem
prob = LpProblem("Minimum_Cost_TSP_Groups", LpMinimize)

# Define variables
x = LpVariable.dicts("x", [(i, j) for i in city_coords.keys() for j in city_coords.keys() if i != j], cat='Binary')
u = LpVariable.dicts("u", range(1, k+1), lowBound=0, cat='Continuous')

# Objective function
prob += lpSum(x[i,j] * distance(city_coords[i], city_coords[j]) for i in city_coords for j in city_coords if i != j), "Total_Travel_Cost"

# Constraints for each cluster
for idx, group in city_groups.items():
    prob += lpSum(x[j,i] for j in group for i in set(city_coords.keys()) - set(group)) == 1, f"One_outgoing_edge_cluster_{idx}"
    prob += lpSum(x[i,j] for i in group for j in set(city_coords.keys()) - set(group)) == 1, f"One_incoming_edge_cluster_{idx}"

# Flow conservation constraints
for i in city_coords.keys():
    prob += (lpSum(x[j, i] for j in city_coords.keys() if j != i) - lpSum(x[i, j] for j in cityads.keys() if j != i) == 0, f"Flow_conservation_{i}")

# Subtour elimination constraints
for i in range(1, k):
    for j in range(i + 1, k + 1):
        if i != j:
            prob += (u[i] - u[j] + k * lpSum(x[p, q] for p in city_groups[i-1] for q in city_groups[j-1]) + (k - 2) * lpSum(x[q, p] for p in city_groups[i-1] for q in city_groups[j-1])) <= k - 1, f"Subtour_elimination_{i}_{j}"

# Solving the problem
status = prob.solve()

# Output the results
tour = []
total_cost = 0

if LpStatus[status] == 'Optimal':
    for i in city_coords:
        for j in city_coords:
            if i != j and x[(i, j)].varValue == 1:
                tour.append((i, j))
                total_cost += distance(city_coords[i], city_coords[j])
                
    # Reconstruct the tour starting from the depot
    organized_tour = [0]
    current_city = 0
    while len(organized_tour) < len(tour) + 1:
        for i, j in tour:
            if i == current_city:
                organized_tour.append(j)
                current_city = j
                break

    # Output result
    print(f"Tour: {organized_tour}")
    print(f"Total travel cost: {round(total_cost, 2)}")
else:
    print("Failed to find an optimal solution. Please review the problem constraints and data.")