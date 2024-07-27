import pulp
import math

# Coordinates of cities including the depot
coordinates = [
    (16, 90),  # Depot
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

# City groups
city_groups = {
    0: [1, 6, 14],
    1: [5, 12, 13],
    2: [7, 10],
    3: [4, 11],
    4: [2, 8],
    5: [3, 9]
}

# Calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Total number of cities, including the depot
num_cities = len(coordinates)
cities = range(num_cities)

# Define the problem
prob = pulp.LpProblem('MinimizeTravelCost', pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective
prob += pulp.lpSum(distance(i, j) * x[i, j] for i in cities for j in cities if i != j)

# Constraints

# Each group must connect to exactly one other city and vice versa
for group in city_groups.values():
    prob += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in cities if j not in which_group(i)) == 1

# Flow conservation
for k in cities:
    prob += pulp.lpSum(x[i, k] for i in cities if i != k) == pulp.lpSum(x[k, j] for j in cities if j != k)

# Prevent subtours using the lifted Miller-Tucker-Zemlin (MTZ) constraints
u = pulp.LpVariable.dicts("u", range(1, num_cities), lowBound=0, cat='Continuous')

for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + num_cities * x[i, j] <= num_cities - 1

# Solve the problem
prob.solve()

# Extract the solution
tour = []
for i in cities:
    for j in cities:
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Find the path starting from depot (0)
path = [0]
while len(path) < len(tour) + 1:
    for arc in tour:
        if arc[0] == path[-1]:
            path.append(arc[1])
            break

# Calculate the total distance
total_distance = sum(distance(path[i], path[i+1]) for i in range(len(path) - 1))

# Output
print("Tour:", path)
print("Total travel cost:", total_distance)