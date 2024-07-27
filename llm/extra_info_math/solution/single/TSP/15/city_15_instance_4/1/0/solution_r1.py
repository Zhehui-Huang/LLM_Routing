import pulp
import math

# Coordinates of the cities:
cities = {
    0: (35, 40),
    1: (39, 41),
    2: (81, 30),
    3: (5, 50),
    4: (72, 90),
    5: (54, 46),
    6: (8, 70),
    7: (97, 62),
    8: (14, 41),
    9: (70, 44),
    10: (27, 47),
    11: (41, 74),
    12: (53, 80),
    13: (21, 21),
    14: (12, 39)
}

# Calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Create the distance matrix
n = len(cities)
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Define the Model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the route goes directly from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(distance_matrix[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j), "Minimize the travel cost"

# Constraints
# Each city must be left exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_city_{i}"

# Each city must be entered exactly once
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1, f"Enter_city_{j}"

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Output tour and total cost.
tour = []
current_city = 0
total_cost = 0

for _ in range(n):
    tour.append(current.

    for j in range(n):
        if i != j and pulp.value(x[current_city, j]) == 1:
            total_cost += distance_matrix[current_city, j]
            current_city = j
            break

tour.append(0)  # complete the tour by returning to the start
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")