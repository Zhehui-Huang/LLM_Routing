import math
import pulp

# Coordinates of cities including the depot
coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42), (36, 30), 
    (52, 82), (93, 44), (21, 78), (68, 14), (51, 28), (44, 79),
    (56, 58), (72, 43), (6, 99)
]

# Number of cities including the depot
n = len(coordinates)

# Euclidean distance calculation
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
dist = [[euclidean distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# TSP using Linear Programming
tsp_problem = pulp.LpProblem("TSP_Min_Cost", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat="Binary")

# Objective
tsp_problem += pulp.lpSum(x[i, j] * dist[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    tsp_problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    tsp_problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Solve the TSP
tsp_problem.solve()
tour = []
current_city = 0
tour.append(current_city)

# Find the tour from the decision variables
while True:
    next_city = [j for j in range(n) if j != current_city and pulp.value(x[current_city, j]) == 1][0]
    if next_city == 0:  # If next city is depot, break the loop
        tour.append(next_city)
        break
    tour.append(next_city)
    current_city = next_city

# Calculate total distance
total_cost = pulp.value(tsp_problem.objective)

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)