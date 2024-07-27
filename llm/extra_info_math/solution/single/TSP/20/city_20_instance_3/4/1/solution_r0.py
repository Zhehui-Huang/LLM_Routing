import pulp
import math

# Coordinates of cities including the depot city at index 0
city_coords = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), 
               (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), 
               (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

n = len(city_coords)  # Number of cities including the depot

# Calculate distance matrix
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distance_matrix = [[euclidean_distance(city_coords[i], city_coords[j]) for j in range(n)] for i in range(n)]

# Defining the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n)], cat='Binary')

# Objective function
problem += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n)), "Total Travel Cost"

# Constraints
for i in range(n):
    problem += (pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1), f"Leave_{i}"
    problem += (pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1), f"Enter_{i}"

# Eliminating subtours by adding extra constraints
for i in range(1, n):
    problem += x[i, 0] == 0  # Cannot directly go to depot except from a node

for i in range(2, n):
    problem += x[0, i] == 0  # Cannot reach any node directly from depot except for node 1

# Solve the problem
status = problem.solve()
print(f"Status: {pulp.LpStatus[status]}")

# Extract the tour
tour = [0]
next_city = 0
while True:
    next_city = [j for j in range(n) if pulp.value(x[next_city, j]) == 1][0]
    if next_desc == 0:
        break
    tour.append(next_city)
tour.append(0)  # Append the return to depot city

# Calculate total travel cost
total_cost = pulp.value(problem.objective)

# Printing the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")