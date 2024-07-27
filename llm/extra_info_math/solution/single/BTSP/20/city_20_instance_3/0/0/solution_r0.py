import pulp
import math
from itertools import combinations

# City coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

N = len(cities)
distances = {}

for i in range(N):
    for j in range(N):
        if i != j:
            # Euclidean distance calculation
            distances[(i, j)] = math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Define the problem
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(N) for j in range(N) if i != j), cat='Binary')
M = pulp.LpVariable("M", lowBound=0, cat='Continuous')

# Objective function
prob += M

# Constraints
for i in range(N):
    prob += pulp.lpSum([x[(i, j)] for j in range(N) if i != j]) == 1  # depart from each city only once
    prob += pulp.lpSum([x[(j, i)] for j in range(N) if i != j]) == 1  # arrive at each city only once

for i, j in distances:
    prob += distances[(i, j)] * x[(i, j)] <= M  # the maximum distance constraint

# Subtour elimination constraints
for S in range(2, N):
    for subset in combinations(range(1, N), S):
        prob += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Output results
tour = []
current_city = 0
while True:
    next_cities = [j for j in range(N) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

tour = [0] + tour

# Calculating tour cost and maximum distance
total_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))
max_distance = max(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)