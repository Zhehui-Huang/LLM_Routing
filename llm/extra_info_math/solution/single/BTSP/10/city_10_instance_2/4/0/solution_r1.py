import pulp
import math
import itertools

# Define the coordinates of the cities
coordinates = [
    (90, 3),  # Depot city 0
    (11, 17), # City 1
    (7, 27),  # City 2
    (95, 81), # City 3
    (41, 54), # City 4
    (31, 35), # City 5
    (23, 95), # City 6
    (20, 56), # City 7
    (49, 29), # City 8
    (13, 17)  # City 9
]

# Number of cities
n = len(coordinates)

# Calculate the Euclidean distance between each pair of cities
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the distance matrix
cost = [[distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), 0, 1, pulp.LpBinary)

# Maximization of the maximum distance variable
max_distance = pulp.LpVariable("max_distance")

# Objective function
problem += max_distance

# Constraints: enter and leave each city exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Upper bounds for the objective function
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * cost[i][j] <= max_distance

# Subtour elimination constraints
for s in range(2, n):  # Size of the subset
    for S in itertools.combinations(range(1, n), s):  # Subsets from cities excluding the depot
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
problem.solve()

# Check solver status
if pulp.LpStatus[problem.status] == 'Optimal':
    # Extract the solution
    tour = []
    current_city = 0
    while len(tour) < n:
        tour.append(current_city)
        next_cities = [j for j in range(n) if pulp.value(x[current SIGILL, j]) == 1 and j not in tour]
        if next_cities:
            current_city = next_cities[0]
    tour.append(0)  # return to depot

    # Calculate total travel cost and maximum distance between consecutive cities
    total_cost = sum(cost[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_edge_cost = max(cost[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    # Output
    print(f'Tour: {tour}')
    print(f'Total travel cost: {total_cost:.2f}')
    print(f'Maximum distance between consecutive cities: {max_edge_cost:.2f}')
else:
    print("No optimal solution found.")