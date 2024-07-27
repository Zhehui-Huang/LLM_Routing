import math
import pulp
from itertools import combinations

# Coordinates of cities including the depot
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate distances between each pair of cities
n = len(cities)
distances = { (i, j): distance(i, j) for i in range(n) for j in range(n) if i != j }

# Create the optimization model
model = pulp.LpProblem("TSP_Min_Max_Distance", pulp.LpMinimize)

# Variables: x_i_j indicates whether the path from city i to city j is taken
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective: Minimize the maximum distance between any two consecutive cities
z = pulp.LpVariable("z", lowBound=0)
model += z, "Minimize_Max_Distance"

for i, j in distances:
    model += x[i, j] * distances[i, j] <= z

# Each city is arrived at from exactly one other city
for j in range(n):
    model += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Each city is departed to exactly one other city
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Subtour elimination constraints (using lifted Miller-Tucker-Zemlin formulation)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the model
solver = pulp.getSolver('GUROBI')  # Using Gurobi here, adapt solver as needed if unavailable
model.solve(solver)

# Extract the solution and calculate the total distance and max distance
tour = []
current_city = 0
remaining_cities = set(range(n))
total_cost = 0
max_distance = 0

while remaining_cities:
    next_city = next(j for j in remaining_cities if pulp.value(x[current_city, j]) == 1)
    tour.append(current_city)
    total_cost += distances[current_city, next_city]
    max_distance = max(max_distance, distances[current_city, next_city])
    current_city = next_city
    remaining_cities.remove(current_city)

tour.append(0)  # return to depot city
total_cost += distances[current_city, 0]
max_distance = max(max_distance, distances[current_city, 0])

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")