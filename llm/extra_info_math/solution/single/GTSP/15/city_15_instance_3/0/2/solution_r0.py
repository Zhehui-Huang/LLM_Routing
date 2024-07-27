import pulp
import math

# Coordinates of the cities, including the depot
city_coordinates = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

# City groups
city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

# Total number of city groups
num_groups = len(city_groups)

# Function to compute the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# List of all cities including depot
all_cities = [0] + [city for group in city_groups for city in group]
n = len(all_cities)  # Total number of cities including depot

# Create a dictionary to map city numbers to matrix indices
city_index = {city: idx for idx, city in enumerate(all_cities)}

# Calculate costs matrix
cost = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            city_i = all_cities[i]
            city_j = all_cities[j]
            cost[i][j] = euclidean_distance(city_coordinates[city_i], city_coordinates[city_j])

# Setup the PUPLP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraint (4): Conservation of flow in and out of each city
for i in range(n):
    prob += (pulp.lpSum(x[j, i] for j in range(n) if j != i) == pulp.lpSum(x[i, j] for j in range(n) if j != i), f"flow_conservation_{i}")

# Constraint to ensure exactly one city per group plus the depot is connected
# Connected to one city from each group and to the depot
for group in city_groups:
    prob += pulp.lpSum(x[0, city_index[city]] for city in group) == 1, f"from_depot_to_group_{group}"
    prob += pulp.lpSum(x[city_index[city], 0] for city in group) == 1, f"to_depot_from_group_{group}"

prob.solve()

# Output solution
tour = [0]
current = 0
visited = set()
visited.add(0)

# Construct the tour from the decision variables
while True:
    next_city = next(j for j in range(n) if j != current and pulp.value(x[current, j]) == 1)
    if next_city == 0:
        tour.append(0)
        break
    tour.append(all_cities[next_city])
    current = next_city
    if current in visited:
        break
    visited.add(current)

# Compute the total cost of the tour
total_cost = sum(cost[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output the results as required
print("Tour:", tour)
print("Total travel cost:", total_cost)