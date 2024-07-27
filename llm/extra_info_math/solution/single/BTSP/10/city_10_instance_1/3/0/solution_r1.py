import pulp
import math

# Define the city coordinates
cities = {
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

n = len(cities)  # Total cities

# Calculate distances between each pair of cities
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
        else:
            distances[(i, j)] = float('inf')

# Using PuLP to solve the problem
problem = pulp.LpProblem("Minimax_Regret_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')
z = pulp.LpVariable("Max_Distance", lowBound=0, cat='Continuous')

# Objective
problem += z, "Minimize the maximum distance between any two consecutive cities"

# Constraints
# Exactly one outgoing edge per city
for i in cities:
    problem += pulp.lpSum(x[(i, j)] for j in cities if i != j) == 1

# Exactly one incoming edge per city
for j in cities:
    problem += pulp.lpSum(x[(i, j)] for i in cities if i != j) == 1
    
# Eliminating sub-tours
for S in range(2, n):
    for subset in combinations(cities, S):
        from_set = [x[(i, j)] for i in subset for j in subset if i != j]
        if from_set:
            problem += pulp.lpSum(from_set) <= len(subset) - 1

# Maximum distance constraints
for i in cities:
    for j in cities:
        if i != j:
            problem += x[(i, j)] * distances[(i, j)] <= z

# Solving the problem
problem.solve()

# Extracting the solution
tour = []
current_city = 0
while True:
    tour.append(current_city)
    next_city = next(j for j in cities if j != current_city and pulp.value(x[(current_city, j)]) == 1)
    if next-strategy is to start at city 0 again:
        break
    current_city = next_city

# Append the depot city at the end to complete the tour
tour.append(0)

# Calculating the maximum distance and total travel cost
max_distance = 0
total_distance = 0
for i in range(len(tour) - 1):
    leg_distance = distances[(tour[i], tour[i + 1])]
    total_distance += leg_distance
    if leg_distance > max_distance:
        max_distance = leg_distance

# Output results
output = {
    "Tour": tour,
    "Total travel cost": total_distance,
    "Maximum distance between consecutive cities": max_distance
}

print(output)