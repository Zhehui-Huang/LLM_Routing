import pulp
import math

# Define cities and their coordinates
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Define groups
groups = {0: [7, 9], 1: [1, 3], 2: [4, 6], 3: [8], 4: [5], 5: [2]}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create the problem instance
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if the robot travels from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function: minimize the total traveling distance
model += pulp.lpSum(euclidean_distance(i, j) * x[(i, j)] for i in cities for j in cities if i != j), "Total_Distance"

# Constraint: exactly one outbound connection from depot
model += pulp.lpSum(x[(0, j)] for j in cities if j != 0) == 1

# Constraint: exactly one inbound connection to depot
model += pulp.lpSum(x[(j, 0)] for j in cities if j != 0) == 1

# Constraints for each group
for group in groups.values():
    # Choose only one node from each group to leave
    model += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1
    # Choose only one node from each group to enter
    model += pulp.lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1

# Flow conservation for other cities
for k in cities:
    if k != 0:
        model += pulp.lpSum(x[(i, k)] for i in cities if i != k) == pulp.lpSum(x[(k, j)] for j in cities if j != k)

# Solve the problem
status = model.solve()
print("Status:", pulp.LpStatus[status])

# Extract the tour and calculate the total distance
tour = [0]
total_cost = 0
current_city = 0

while True:
    next_city = [j for j in cities if j != current_city and pulp.value(x[(current_city, j)]) == 1][0]
    total_cost += euclidean_agenda