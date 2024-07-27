import pulp
import math
from itertools import combinations

# Coordinates of the cities
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Number of cities
n = len(cities)

# Distance matrix
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Setting up the optimization problem: Minimize the maximum distance between consecutive cities
prob = pulp.LpProblem("Minimize_Max_Distance", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), 0, 1, pulp.LpBinary)
d_max = pulp.LpVariable("d_max", lowBound=0)

# Objective
prob += d_max

# Constraints
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if j != i) == 1
    prob += pulp.lpSum(x[j, i] for j in cities if j != i) == 1

for i, j in distances:
    prob += x[i, j] * distances[i, j] <= d_max

# Subtour elimination constraints
for s in range(2, n+1):
    for S in combinations(range(1, n), s):
        prob += pulp.lpSum(x[i, j] for i in S for j in S if i!=j) <= len(S)-1

# Solve the problem
prob.solve()

# Extracting the tour
tour = []
current_city = 0
tour.append(current_city)
remaining_cities = set(cities.keys()) - {current_city}

while remaining_cities:
    next_city = max((j for j in remaining_cities if pulp.value(x[current_city, j]) == 1), key=lambda j: x[current_city, j])
    tour.append(next_city)
    remaining_cities.remove(next_city)
    current_city = next_city

# Append the starting city to complete the tour
tour.append(0)

# Calculate the total distance and max segment distance
total_distance = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
max_segment_distance = max(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output result
print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_segment_distance)