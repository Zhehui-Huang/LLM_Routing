import pulp as pl
import math
from itertools import permutations, combinations

# Given city coordinates
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Function to calculate Euclidean distance
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of cities
n = len(cities)

# Computing the cost matrix
costs = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create LP problem instance
model = pl.LpProblem("Minimize_Maximum_Distance_TSP", pl.LpMinimize)

# Creating LP variables
x = pl.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
max_dist = pl.LpVariable("Max_Distance", lowBound=0)

# Objective function to minimize the maximum distance
model += max_dist

# Adding constraints
for i in range(n):
    model += pl.lpSum(x[i, j] for j in range(n) if i != j) == 1
    
for j in range(n):
    model += pl.lpSum(x[i, j] for i in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * costs[i][j] <= max_dist

# Subtour elimination constraints
for size in range(2, n):
    for subset in combinations(range(1, n), size):
        model += pl.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = model.solve()

# Solution extraction and output formation
if pl.LpStatus[status] == 'Optimal':
    tour = [0]
    total_cost = 0
    max_distance_in_tour = 0
    
    # Following the tour path starting from depot
    next_node = 0
    while True:
        for j in range(n):
            if j != next_node and pl.value(x[next_node, j]) == 1:
                tour.append(j)
                dist = costs[next_node][j]
                total_cost += dist
                if dist > max_distance_in_tour:
                    max_distance_in_tour = dist
                next_node = j
                break
        if next_node == 0:
            break
    
    tour.append(0)  # Return to depot
    total_cost += costs[tour[-2]][0]  # Add the cost of returning to the depot
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance_in_tour}")
else:
    print("No optimal solution found.")