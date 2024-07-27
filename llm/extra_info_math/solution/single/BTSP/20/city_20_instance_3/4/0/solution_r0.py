import pulp
import math

# Define the cities' coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Calculate distances between all cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = euclidean_distance(cities[i], cities[j])

# Create problem
problem = pulp.LpProblem("TSP_minimax", pulp.LpMinimize)

# Decision variables: x_ij = 1 if travel from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Auxiliary variable for the objective
max_dist = pulp.L Cole.LpVariable("max_dist", lowBound=0, cat='Continuous')

# Objective
problem += max_dist

# Constraints
for i in cities:
    problem += pulp.lpSum(x[i, j] for j in cities if j != i) == 1  # leave each city once
    problem += pulp.lpSum(x[j, i] for j in cities if j != i) == 1  # enter each city once

# Added subtour elimination constraints using uf constraints
u = pulp.L mau.variablesdicts("u", (i for i in cities if i != 0), lowBound=1, upBound=len(cities) - 1, cat='Continuous')
for i in cities:
    for j in cities:
        if i != j and j != 0 and i != 0:
            problem += u[i] - u[j] + len(cities) * x[i, j] <= len(cities) - 1

# Maximizing distance constraints
for i in cities:
    for j in cities:
        if i != j:
            problem += x[i, j] * distances[i, j] <= max_dist

# Solve problem
status = problem.solve()

# Extract results
tour = []
current_city = 0
visited = set()
while True:
    visited.add(current_city)
    tour.append(current_city)
    next_cities = [j for j in cities if j != current_city and x[current_city, j].varValue == 1]
    if not next_cities:
        break
    current_city = next_cities[0]
tour.append(0)  # to complete the tour by returning to the depot

# Total cost and maximum distance
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
max_dist_value = max(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_dist_value}")