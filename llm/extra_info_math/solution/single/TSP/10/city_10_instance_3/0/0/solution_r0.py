import pulp
from math import sqrt

# Define the cities' coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
n = len(cities)
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[(i, j)] = euclidean_distance(cities[i], cities[j])

# Setup the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if the tour goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(distance_matrix[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_{i}"
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

# Solving the problem
prob.solve()

# Extracting the solution
tour = []
current = 0
while True:
    tour.append(current)
    next_cities = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
    if not next_cities:
        break
    current = next_cities[0]

# Ensure tour returns to the start
tour.append(tour[0])

# Calculate the total cost
total_cost = sum(distance_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")