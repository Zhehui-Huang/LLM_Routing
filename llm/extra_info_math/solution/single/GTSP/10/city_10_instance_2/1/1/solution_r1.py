import pulp
import math

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2],
}

# Distance calculator
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Define problem
problem = pulp.LpProblem("TSP_Grp", pulp.LpMinimize)

# Variables: x[i,j] is 1 if path i->j is taken, otherwise 0
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective
problem += pulp.lpSum(distance(i, j) * x[i, j] for i in cities for j in cities if i != j)

# Constraints
for k, v in groups.items():
    # Exactly one city from each group is visited
    problem += pulp.lpSum(x[i, j] for i in v for j in cities if i != j) == 1
    problem += pulp.lpSum(x[j, i] for i in v for j in cities if i != j) == 1

# Flow conservation
for i in cities:
    problem += (pulp.lpSum(x[i, j] for j in cities if i != j) - pulp.lpSum(x[j, i] for j in cities if i != j)) == 0

# Solve problem
problem.solve()

# Retrieving the route
route = []
current_city = 0
remaining_cities = list(cities.keys())

while remaining_cities:
    next_cities = [j for j in remaining_cities if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:  # No next city found, tour might be incomplete or broken
        break
    next_city = next_cities[0]
    route.append(next_city)
    remaining_cities.remove(current_city)
    current_city = next_city

# Complete the tour by returning to the depot
if route[0] != 0:
    route = [0] + route  # Ensure starts at the depot
if current_city != 0:
    route.append(0)  # Ensure ends at the depot

# Calculate total cost
total_cost = sum(distance(route[i], route[i+1]) for i in range(len(route) - 1))

print("Tour:", route)
print("Total travel cost:", total_cost)