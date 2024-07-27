import pulp
import itertools
import math

# Coordinates setup
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
    (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28),
    (60, 63), (93, 15)
]

# Number of cities
n = len(coordinates)

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cost matrix
costs = [[euclidean_calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
problem = pulp.LpProblem("Traveling_Salesman", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective
problem += pulp.lpSum(costs[i][j] * x[(i, j)] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Sub-tour elimination
for m in range(2, n):
    for S in itertools.combinations(range(n), m):
        problem += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
problem.solve()

# Finding the tour from the result
tour = []
next_city = 0
visited_cities = [False] * n

while True:
    for j in range(n):
        if x[(next_city, j)].varValue == 1:
            tour.append(next_city)
            visited_cpathities[next_city] = True
            next_city = j
            break
    if next_city == 0:
        tour.append(0)
        break

# Calculate the total cost
total_cost = sum(costs[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")