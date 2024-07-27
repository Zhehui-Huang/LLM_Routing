import numpy as np
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, pulp

# City coordinates
cities = [
    (16, 90),  # Depot city 0
    (43, 99), (80, 21), (86, 92), (54, 93), 
    (34, 73), (6, 61), (86, 69), (30, 50), 
    (35, 73), (42, 64), (64, 30), (70, 95), 
    (29, 64), (32, 79)
]

# Number of cities including depot
n = len(cities)

# Calculate Euclidean distances
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the problem
model = LpProblem("Minimax_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
max_dist = LpVariable("max_dist", lowBound=0, cat='Continuous')

# Objective
model += max_dist

# Constraints
for i in range(n):
    model += lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    model += lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i][j] * x[(i, j)] <= max_dist

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(1, n), s):  # Depo isn't included in subsets
        model += lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
solution_status = model.solve()

# Checking if the solution is optimal
if solution_status == pulp.LpStatusOptimal:
    # Extract the solution
    route=[]
    for i in range(n):
        for j in range(n):
            if i != j and x[(i, j)].varValue == 1:
                route.append((i,j))

    # Construct ordered tour from route
    current_location = 0
    tour = [current_location]
    while len(tour) < n:
        for (i, j) in route:
            if i == current_location:
                tour.append(j)
                current_location = j
                break
    tour.append(0)  # complete the tour by returning to depot

    # Calculate total cost and max distance
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) -1))
    
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No optimal solution found.")