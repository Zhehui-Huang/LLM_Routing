import pulp
import math
from itertools import permutations

# Function to calculate Euclidean distance
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Number of cities including the depot
n = len(coordinates)

# Calculate distances matrix
distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = pulp.LpProblem("MinimizeMaxDistance", pulp.LpMinimize)

# Decision variable: x_ij is 1 if travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective: minimize the maximum distance 'z' between consecutive cities
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')
prob += z

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1  # leave each city only once
    prob += pulp.lpSum(x[j, i] for j in range(n) if j != i) == 1  # enter each city only once

# Max distance for each travel should not exceed z
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i][j] * x[i, j] <= z

# Eliminate sub-tours by using subtour elimination constraints
for S in (set(permutations(range(1, n), r)) for r in range(2, n)):
    for s in S:
        prob += pulp.lpSum(x[i, j] for i in s for j in s if i != j) <= len(s) - 1

# Solve the problem
prob.solve()

# Find the tour from decision variables
tour = [0]
current_city = 0
remaining_cities = set(range(1, n))

while remaining_cities:
    next_city = next(j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1)
    tour.append(next_city)
    remaining_cities.remove(next_city)
    current_city = next_city

# Returning to the starting city
tour.append(0)

# Calculating the total distance and max distance between consecutive cities
total_distance = 0
max_distance = 0
for i in range(len(tour) - 1):
    travel = distances[tour[i]][tour[i + 1]]
    total_distance += travel
    max_distance = max(max_distance, travel)

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")