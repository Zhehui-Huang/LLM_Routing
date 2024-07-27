import pulp
import math
import itertools

# Define city coordinates
coordinates = [
    (79, 15),  # City 0 (Depot)
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Function to calculate the Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

n = len(coordinates)

# Create the distance matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city exactly once
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # arrive at each city exactly once

# Subtour elimination constraints
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract results
if prob.status == 1:
    path = []
    active_arcs = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]
    
    # Start from the depot
    next_city = 0
    tour_cost = 0
    while len(active_arcs) > 0:
        for i, j in active_arcs:
            if i == next_city:
                next_city = j
                tour_cost += cost[i][j]
                path.append(i)
                active_arcs.remove((i,j))
                break
    path.append(0)  # returning to the depot
    tour_cost += cost[next_city][0]  # add cost to return to depot

    # Output results
    print(f"Tour: {path + [0]}")
    print(f"Total travel cost: {tour_cost}")
else:
    print("Failed to find a valid solution.")