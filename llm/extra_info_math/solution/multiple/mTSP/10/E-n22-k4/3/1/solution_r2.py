import math
import pulp as lp

# Define the city coordinates
coordinates = [
    (145, 215), # Depot city 0
    (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]
n = len(coordinates)  # total cities including depot
m = 4  # number of robots

# Function to calculate euclidean distances
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Create the LP problem
problem = lp.LpProblem("Robotic_Routing", lp.LpMinimize)

# Decision variables
x = lp.LpVariable.dicts("x", [(i, j, k) for k in range(m) for i in range(n) for j in range(n) if i != j],
                        cat='Binary')

# Objective function to minimize the total distance
problem += lp.lpSum(x[(i, j, k)] * distances[i][j] for k in range(m) for i in range(n) for j in range(n) if i != j)

# Constraints

# 1. Each non-depot city must be visited exactly once by any salesman
for j in range(1, n):
    problem += lp.lpSum(x[(i, j, k)] for k in range(m) for i in range(n) if i != j) == 1

# 2. Each salesman must leave from and return to the depot
for k in range(m):
    problem += lp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1  # leaving depot
    problem += lp.lpSum(x[(j, 0, k)] for j in range(1, n)) == 1  # returning to depot

# 3. Flow conservation constraint for each salesman at each city
for k in range(m):
    for j in range(1, n):
        problem += lp.lpSum(x[(i, j, k)] for i in range(n) if i != j) - lp.lpSum(x[(j, i, k)] for i in range(n) if i != j) == 0

# Solve the problem
problem.solve()

# Output results
total_cost = 0
for k in range(m):
    tour = [0]
    next_city = [i for i in range(n) if i != 0 and lp.value(x[(0, i, k)]) == 1][0]
    while next_city != 0:
        tour.append(next_city)
        current_city = next_city
        next_city = [j for j in range(n) if lp.value(x[(current_city, j, k)]) == 1][0]
    tour.append(0)  # returning to depot
    tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    total_cost += tour_mean
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")