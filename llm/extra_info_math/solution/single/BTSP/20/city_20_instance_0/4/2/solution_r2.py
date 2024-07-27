import pulp
from math import sqrt

# City coordinates
cities = {
    0: (8, 11),
    1: (40, 6),
    2: (95, 33),
    3: (80, 60),
    4: (25, 18),
    5: (67, 23),
    6: (97, 32),
    7: (25, 71),
    8: (61, 16),
    9: (27, 91),
    10: (91, 46),
    11: (40, 87),
    12: (20, 97),
    13: (61, 25),
    14: (5, 59),
    15: (62, 88),
    16: (13, 43),
    17: (61, 28),
    18: (60, 63),
    19: (93, 15)
}

def distance(i, j):
    return sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

n = len(cities)  # Number of cities

# Create the problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
d = pulp.LpVariable("MaxDistance", lowBound=0, cat='Continuous')

# Objective: minimize the maximum distance
prob += d

# Constraints
# Each city must have exactly one departure
for i in range(n):
    prob += sum(x[i, j] for j in range(n) if i != j) == 1, f"DepartFrom_{i}"

# Each city must have exactly one arrival
for j in range(n):
    prob += sum(x[i, j] for i in range(n) if i != j) == 1, f"ArriveAt_{j}"

# No sub-tours
for r in range(3, n+1):
    for subset in itertools.combinations(range(1, n), r - 1):
        i_subset = [0] + list(subset)
        prob += sum(x[i, j] for i in i_subset for j in i_subset if i != j) <= len(i_subset) - 1

# Distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distance(i, j) <= d, f"DistConstraint_{i}_{j}"

# Solve
solver = pulp.PULP_CBC_CMD(msg=0)
prob.solve(solver)

# Tour and distance calculation
tour = [0]
max_edge_length = 0

current_city = 0
while True:
    for next_city in range(n):
        if current_city != next_city and pulp.value(x[current_city, next_city]) == 1:
            max_edge_length = max(max_edge_length, distance(current_city, next_city))
            tour.append(next_city)
            current_city = next_city
            break
    if current_city == 0:
        break

total_travel_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Outputs
print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", max_edge_length)