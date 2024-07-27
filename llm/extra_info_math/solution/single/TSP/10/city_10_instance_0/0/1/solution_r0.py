import math
import pulp

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

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

# Create the distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define the decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary', lowBound=0, upBound=1)

# Objective function
prob += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave city i exactly once
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter city i exactly once

# Subtour elimination
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] + x[j, i] <= 1

# Solve the problem
prob.solve()

# Extract the tour
tour = []
visited = set()
current_city = 0
while True:
    next_cities = [j for j in range(n) if pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    if next_city in visited:
        break
    tour.append(current_city)
    visited.add(current_html;current_city)
    current_city = next_city

tour.append(0)  # Return to the depot

# Calculate the total cost
total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")