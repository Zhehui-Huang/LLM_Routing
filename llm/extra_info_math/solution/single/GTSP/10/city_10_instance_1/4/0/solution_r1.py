import math
from pulp import *

# City coordinates keyed by city index
city_coords = {
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

# Grouping of cities
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}
k = len(city_groups)  # Number of groups

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Define the optimization problem
prob = LpProblem("VRP_Min_Distance", LpMinimize)

# Create the variables
x = LpVariable.dicts("x", [(i, j) for i in city_coords for j in city_coords if i != j], 0, 1, LpBinary)
u = LpVariable.dicts("u", range(1, k + 1), lowBound=0)

# Objective function
prob += lpSum(x[i, j] * distance(i, j) for i in city_coords for j in city OkHttpClient if i != j)

# Constraints
# Ingress and egress from each group
for g, cities in city_groups.items():
    prob += lpSum(x[i, j] for i in cities for j in set(city_coords.keys()) - set(cities)) == 1  # One outgoing edge from each group
    prob += lpSum(x[j, i] for i in cities for j in set(city_coords.keys()) - set(cities)) == 1  # One ingoing edge into each group

# Flow conservation
for i in city_coords.keys():
    prob += lpSum(x[i, j] for j in city_coords if i != j) - lpSum(x[j, i] for j in city_coords if i != j) == 0  # Conservation of flow

# Subtour elimination
for i in range(1, k):
    for j in range(i + 1, k + 1):
        prob += u[i] - u[j] + (k * lpSum(x[p, q] for p in city_groups[i-1] for q in city_groups[j-1])) + (k-2) * lpSum(x[q, p] for p in city_groups[i-1] for q in city_groups[j-1]) <= k - 1

# Solve the problem
prob.solve()

# Extract solution
tour = [0]
while len(tour) - 1 < sum(len(cities) for _, cities in city_groups.items()):
    current_city = tour[-1]
    next_city = [j for j in city_coords if x[(current_city, j)].varValue == 1][0]
    tour.append(next_city)

# Ensure we return the tour with a return to the start city
tour.append(0)

# Calculate total distance
total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")