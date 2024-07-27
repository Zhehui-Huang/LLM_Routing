import pulp
import math

# City coordinates given
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# City groups
city_groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

# Function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# All cities including depot
all_cities = list(cities.keys())

# Create the ILP problem
problem = pulp.LpProblem("MinimizeTravelCost", pulp.LpMinimize)

# Decision Variables
x = {}
for i in all_cities:
    for j in all_cities:
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", 0, 1, pulp.LpBinary)

# Objective function
objective = pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in all_cities for j in all_cities if i != j)
problem += objective

# Constraints: Each cluster must have exactly one outgoing and one incoming edge to a non-cluster city
for group, members in city_groups.items():
    problem += pulp.lpSum(x[(i, j)] for i in members for j in all_cities if j not in members) == 1
    problem += pulp.lpSum(x[(j, i)] for i in members for j in all_cities if j not in members) == 1

# Flow conservation constraints
for k in all_cities:
    problem += pulp.lpSum(x[(i, k)] for i in all_cities if i != k) == pulp.lpSum(x[(k, j)] for j in all_cities if j != k)

# Solve the problem
problem.solve()

# Extract the route
route = [0]  # start from the depot
visited = {0}
current_city = 0
total_cost = 0
while len(visited) < len(city_groups) + 1:  # include depot
    next_city = [j for j in all_cities if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if next_city:
        next_city = next_city[0]
        route.append(next_city)
        visited.add(next_city)
        total_cost += euclidean_distance(current_city, next_city)
        current_city = next_city

# Adding the last leg to return to the depot
route.append(0)
total_cost += euclidean_distance(current_city, 0)

print("Tour:", route)
print("Total travel cost:", total_canadian_cost)