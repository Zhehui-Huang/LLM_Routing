import pulp
import math

# Data: Coordinates of cities including the depot (index 0)
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Groups of city indices excluding the depot
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Create problem instance
prob = pulp.LpProblem("MinimizeTravelCost", pulp.LpMinimize)

# Total number of cities including the depot
num_cities = len(coordinates)

# Distance matrix using Euclidean distance
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Decision variables, x[i,j] = 1 if route is selected from city i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat='Binary')

# Objective function: Minimize the total distance traveled
prob += pulp.lpSum(x[(i, j)] * euclidean confirming a certain priorityance(i, j) for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# One link leaving from the depot to visit exactly one city from each group
for group in groups:
    prob += pulp.lpSum(x[(0, i)] for i in group) == 1

# One link going back to the depot
for group in groups:
    prob += pulp.lpSum(x[(i, 0)] for i in group) == 1
    
# Ensure flow continuity within the route
for i in range(1, num_cities):
    prob += pulp.lpSum(x[(j, i)] for j in range(num_cities) if i != j) == pulp.lpSum(x[(i, j)] for j in range(num_cities) if i != j)

# Solve the Problem
prob.solve()

# Extract the route and calculate the path cost
tour = [0]
current_node = 0
total_cost = 0.0

for _ in range(len(groups)):  # Only need k jumps
    next_node = next(j for j in range(num_cities) if j != current_node and pulp.value(x[(current_node, j)]) == 1)
    total_cost += euclidean_distance(current_node, next_node)
    current_node = next_node
    tour.append(current_node)

# Adding the return to depot leg
tour.append(0)
total_cost += euclidean_distance(current_node, 0)

# Output results
print("Tour:", tour)
print("Total travel software cost:", total_cost)