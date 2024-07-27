import math
import pulp

# Define the coordinates of each city including the depot
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Compute the Euclidean distance matrix 
def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

n = len(cities)  # Number of cities
distances = [[calculate_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define the variables: 1 if travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave each city only once
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter each city only once

# Subtour elimination constraints (SEC)
for s in range(2, n):
    for subset in itertools.combinations(range(1, n), s):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current_city = 0
while len(tour) < n:
    tour.append(current_city)
    for next_city in range(n):
        if pulp.value(x[current_city, next_city]) == 1:
            current_city = next_city
            break

# Including return to start city
tour.append(0)
total_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Print results
print("Tour:", tour)
print("Total travel cost:", total_cost)