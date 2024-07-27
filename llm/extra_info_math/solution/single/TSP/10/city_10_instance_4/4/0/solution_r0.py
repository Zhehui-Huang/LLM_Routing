import pulp
import math

# Define the city coordinates
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

# Calculate distances between each pair of nodes
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

n = len(coordinates)
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the route goes between city i and j, 0 otherwise
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function: minimize the total travel cost
prob += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city only once
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter each city only once

# Subtour Elimination Constraints
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Check if a valid solution has been found
if prob.status == 1:
    tour = []
    active_arcs = [arc for arc in x if x[arc].varValue == 1]
    
    # Find the tour sequence
    next_city = 0
    for _ in range(n):
        tour.append(next_city)
        next_city = next(j for i, j in active_arcs if i == next_key)
        active_arcs = [arc for arc in active_arcs if arc[0] != next_key]

    # Append the starting city to complete the tour
    tour.append(0)

    # Calculate the total travel cost
    total_cost = sum(cost[tour[i]][tour[i+1]] for i in range(n))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("Failed to find a valid tour")