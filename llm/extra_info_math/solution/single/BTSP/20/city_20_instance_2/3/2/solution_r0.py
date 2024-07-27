import pulp
import math

# Define the locations of cities including the depot
locations = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
    (51, 58), (30, 48)
]

def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

# Number of cities (including depot)
n = len(locations)

# Distance matrix calculation
distances = [[euclidean_distance(locations[i], locations[j]) for j in range(n)] for i in range(n)]

# Setup the PuLP problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
max_dist = pulp.LpVariable("max_distance")

# Objective
prob += max_dist

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1

for j in range(n):
    prob += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == 1

prob += x[(0, 0)] == 0  # Not use the self-loop

for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[(i, j)] * distances[i][j] <= max_dist

# Solve the problem
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Extracting the solution
tour = []
current_city = 0
next_city = None
for _ in range(n):
    for j in range(n):
        if j != current_city and pulp.value(x[(current_city, j)]) == 1:
            next_city = j
            break
    tour.append(current_city)
    current_city = next_city

# Adding the depot to complete the tour
tour.append(0)

# Calculating total distance and maximum distance
total_distance = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_distance)