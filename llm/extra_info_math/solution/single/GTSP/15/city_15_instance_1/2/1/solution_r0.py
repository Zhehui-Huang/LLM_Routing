import pulp
import math

# City coordinates
city_coords = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Groups
groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0]) ** 2 + (city_coords[city1][1] - city_coords[city2][1]) ** 2)

# Number of cities and groups
n_cities = len(city_coords)
n_groups = len(groups)

# Problem setup
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x",
                          ((i, j) for i in range(n_cities) for j in range(n_cities) if i != j),
                          cat='Binary')

# Objective
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(n_cities) for j in range(n_cities) if i != j)

# Constraints
# In and Out exactly one from each group
for g in groups:
    prob += pulp.lpSum(x[(i, j)] for i in g for j in range(n_cities) if j not in g) == 1
    prob += pulp.lpSum(x[(j, i)] for i in g for j in range(n_cities) if j not in g) == 1

# Flow conservation
for i in range(n_cities):
    prob += (pulp.lpSum(x[(j, i)] for j in range(n_cities) if j != i) -
            pulp.lpSum(x[(i, j)] for j in range(n_cities) if j != i) == 0)

# Solve the problem
prob.solve()

# Extract solution
tour = []
visited = set()
current_city = 0
while True:
    tour.append(current_city)
    visited.add(current_city)
    next_cities = [j for j in range(n_cities) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    current_city = next_cities[0]

# Return to the starting city
tour.append(0)

# Calculate the total travel cost
travel_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output
output = {
    "Tour": tour,
    "Total travel cost": travel_cost
}

print("Tour:", output["Tour"])
print("Total travel cost:", output["Total travel cost"])