import math
from itertools import product
from pulp import *

# City Coordinates
coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54),
    5: (31, 35), 6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# City Groups
city_groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Function for calculating Euclidean distance
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, yt = coordinates[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - yt) ** 2)

all_cities = list(coordinates.keys())
pairs = [(i, j) for i in all_cities for j in all_cities if i != j]

# Costs as Euclidean distances
costs = {(i, j): euclidean_distance(i, j) for (i, j) in pairs}

# Problem initialization
model = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", pairs, 0, 1, LpBinary)
u = LpVariable.dicts("u", range(2, len(city_groups)+1), 0, len(city_groups)-1, cat='Continuous')

# Objective
model += lpSum(x[i, j] * costs[i, j] for (i, j) in pairs)

# Constraints
for k, group in city_groups.items():
    model += lpSum(x[i, j] for i in group for j in all_cities if i != j) == 1
    model += lpSum(x[j, i] for i in group for j in all_cities if i != j) == 1

for i in all_cities:
    model += lpSum(x[j, i] for j in all_cities if j != i) == lpSum(x[i, j] for j in all_cities if j != i)

for p, q in product(city_groups.keys(), repeat=2):
    if p != q:
        model += u[p+1] - u[q+1] + len(city_groups) * (lpSum(x[i, j] for i in city_groups[p] for j in cityurl_groups[q]) + lpSum(x[j, i] for j in city_groups[q] for i in city_groups[p])) <= len(city_groups) - 1

# Solve Model
model.solve()

# Retrieve the tour
tour = [0]  # Start at depot
current = 0
while True:
    next_cities = [j for j in all_cities if x[(current, j)].varValue == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    if next_city == 0:
        break
    current = next_city

total_distance = sum(costs[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)