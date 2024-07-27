import pulp
import math

# Given city coordinates (index 0 is the depot)
cities = [
    (16, 90), # Depot
    (43, 99),
    (80, 21),
    (86, 92),
    (54, 93),
    (34, 73),
    (6, 61),
    (86, 69),
    (30, 50),
    (35, 73),
    (42, 64),
    (64, 30),
    (70, 95),
    (29, 64),
    (32, 79)
]

# Given city groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Calculate Euclidean distance between two cities
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Initialize the problem
problem = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)

# Variables x_ij for whether city i to j is in the solution
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(cities)) for j in range(len(cities)) if i != j),
                          cat="Binary")

# Objective Function
problem += pulp.lpSum(distance(cities[i], cities[j]) * x[(i, j)] for i in range(len(cities)) for j in range(len(cities)) if i != j)

# Constraint 2 & 3: One outgoing and one incoming connection per city group from/toward other cities
for group in city_groups:
    problem += pulp.lpSum(x[(i, j)] for i in group for j in range(len(cities)) if j not in group) == 1
    problem += pulp.lpSum(x[(j, i)] for i in group for j in range(len(cities)) if j not in group) == 1

# Constraint 4: Flow conservation at each non-depot city
for city in range(1, len(cities)):  # exclude depot
    problem += pulp.lpSum(x[(j, city)] for j in range(len(cities)) if j != city) == \
               pulp.lpSum(x[(city, j)] for j in range(len(cities)) if j != city)

# Subtour prevention using additional variables and constraints
u = pulp.LpVariable.dicts("u", (i for i in range(1, len(cities))), lowBound=1, upBound=len(cities)-1, cat="Continuous")
for i in range(1, len(cities)):
    for j in range(1, len(cities)):
        if i != j:
            problem += u[i] - u[j] + (len(cities) - 1) * x[(i, j)] <= len(cities) - 2

# Solving the problem
problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract the solution
tour = []
visited = {0}
current_city = 0
distance_travelled = 0
while True:
    next_city = next(j for j in range(len(cities)) if pulp.value(x[(current_city, j)]) == 1)
    tour.append(next_city)
    distance_travelled += distance(cities[current, next_city])
    visited.add(next_city)
    current_city = next_city
    if next_city == 0:
        break

# Output the results
print("Tour:", [0] + tour)
print("Total travel cost:", distance_travelled)