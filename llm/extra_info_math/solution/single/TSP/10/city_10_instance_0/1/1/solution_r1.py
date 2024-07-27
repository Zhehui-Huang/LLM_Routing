import pulp
import math
import itertools

# Coordinates of the cities
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Create the variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function: minimize the total cost of traveling
problem += pulp.lpSum(x[(i, j)] * distance(cities[i], cities[j]) for i in cities for j in cities if i != j)

# Constraints
# Each city must be left exactly once
for i in cities:
    problem += pulp.lpSum(x[(i, j)] for j in cities if i != j) == 1

# Each city must be entered exactly once
for j in cities:
    problem += pulp.lpSubtract(x[(i, j)] for i in cities if i != j) == 1

# Subtour elimination
for s in range(2, len(cities)):
    for subset in itertools.combinations(cities, s):
        problem += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem using PuLP's default solver
problem.solve()

# Extract the solution and print the results
tour = [0]
current = 0
total_cost = 0

# Detect tour from variables
while True:
    next_cities = [j for j in cities if j != current and pulp.value(x[(current, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    total_cost += distance(cities[current], cities[next_city])
    current = next_city
    if current == 0:
        break

# Ensuring the tour ends at the depot
if tour[-1] != 0:
    tour.append(0)
    total_cost += distance(cities[tour[-2]], cities[0])

print("Tour:", tour)
print("Total travel cost:", total_cost)