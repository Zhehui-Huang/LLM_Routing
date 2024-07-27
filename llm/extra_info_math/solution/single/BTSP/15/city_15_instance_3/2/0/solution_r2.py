import pulp
import math
from itertools import permutations

# Coordinates for each city including the depot city
coordinates = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

num_cities = len(coordinates)

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Problem definition
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x",
    ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j),
    cat='Binary')

# Minimize the maximum distance in the tour
max_distance = pulp.LpVariable("max_distance")
model += max_distance

# Objective Function
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            model += max_distance >= distance(i, j) * x[i, j]

# Subject to
# Every city has to be arrived at from exactly one other city
for j in range(num_cities):
    model += pulp.lpSum(x[i, j] for i in range(num_cities) if i != j) == 1

# Every city has to be left to exactly one other city
for i in range(num_cities):
    model += pulp.lpSum(x[i, j] for j in range(num_all_cities) if i != j) == 1

# Subtour elimination
u = pulp.LpVariable.dicts('u', range(num_cities), lowBound=0, upBound=num_cities - 1, cat='Continuous')
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            model += u[i] - u[j] + num_cities * x[i, j] <= num_cities - 1

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the tour
tour = [0]
for _ in range(num_cities - 1):
    next_city = [j for j in range(num_cities) if j not in tour and pulp.value(x[tour[-1], j]) == 1]
    if next_city:
        tour.append(next_city[0])

# Close the loop
tour.append(0)

# Total distance and maximum distance traveled
total_travel_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
max_distance_traveled = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Results output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_distance}")
print(f"Maximum distance between consecutive cities: {max_distance_traveled}")