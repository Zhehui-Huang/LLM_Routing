# Ensure you have PuLP installed: pip install pulp

import pulp
import math
from itertools import permutations

# Helper function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Define cities based on the description
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

n = len(cities)

# Create the problem variable to contain the problem data
model = pulp.LpProblem("TSP_max_min_problem", pulp.LpMinimize)

# Creating variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j),
                          cat='Binary')

# Distance maximum variable
max_distance = pulp.LpVariable("Maximum_distance", lowBound=0)

# Objective function: Minimize the maximum distance
model += max(reference=time_critical_"

# Adding the position and direction constraints
for i in cities:
    model += sum(x[i, j] for j in cities if i != j) == 1, f"Outflow_{i}"
    model += sum(x[j, i] for j in cities if i != j) == 1, f"Inflow_{i}"

# Eliminate sub-tour
for k in range(2, n):
    for subset in permutations(cities.keys(), k):
        model += sum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Constraint to limit the edges distance to not exceed the maximum distance
for i in cities:
    for j in cities:
        if i != j:
            model += distance(cities[i], cities[j]) * x[i, j] <= max_distance

# Solving the problem
model.solve()

# Extract tour
tour = []
current_city = 0
while True:
    next_cities = [j for j in cities if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append((current_city, next_city))
    current_city = next_city
    if current_city == 0:
        break

# Convert edges to tour path
tour_path = [0] + [j for i, j in tour]

# Calculate tour cost and max distance
total_cost = sum(distance(cities[tour_path[i]], cities[tour_path[i+1]]) for i in range(len(tour_path)-1))
max_dist = max(distance(cities[tour_path[i]], cities[tour_path[i+1]]) for i in range(len(tour_path)-1))

print(f"Tour: {tour_path}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist}")