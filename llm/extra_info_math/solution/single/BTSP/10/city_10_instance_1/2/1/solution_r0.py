import pulp
import math
from itertools import combinations

# City coordinates
coordinates = {
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

# Total number of cities including the depot
n = len(coordinates)

# Calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distances matrix
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

# Define the problem
problem = pulp.LpProblem("Min_Max_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
max_dist = pulp.LpVariable("max_dist", lowBound=0, cat=pulp.LpContinuous)

# Objective
problem += max_dist

# Constraints
for i in range(n):
    problem += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1
    problem += pulp.lpSum([x[j, i] for j in range(n) if i != j]) == 1

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

for i in range(n):
    for j in range(n):
        if i != j:
            problem += distances[i, j] * x[i, j] <= max_dist

# Solve the problem
status = problem.solve()
print(f"Status: {pulp.LpStatus[status]}")

# Extract solution
tour = []
current_city = 0
path_taken = set()
tour.append(current_city)

while len(path_taken) < n - 1:
    for j in range(n):
        if j != current_city and x[current_city, j].varValue == 1:
            path_taken.add(current_city)
            tour.append(j)
            current_city = j
            break
            
tour.append(0)  # Going back to the depot city

# Calculate total travel cost and maximum distance between consecutive cities
total_travel_cost = 0
max_distance = 0

for i in range(len(tour) - 1):
    distance = distances[tour[i], tour[i + 1]]
    total_travel_cost += distance
    if distance > max_distance:
        max_distance = distance

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")