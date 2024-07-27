import pulp
import math

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define cities and their coordinates
coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
               (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
               (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
               (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
               (155, 185), (139, 182)]

# Number of robots and depots
num_robots = 4
depots = [0] * num_robots
n = len(coordinates)

# Initialize the problem
problem = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Integer')

# Objective function: Minimize the total distance
problem += pulp.lpSum(euclidean_distance(coordinates[i], coordinates[j]) * x[i, j] 
                      for i in range(n) for j in range(n) if i != j)

# Constraints
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1  # each city must be entered exactly once

for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # each city must be left exactly once

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] <= (n - 1) * (1 - x[i, j]) - 1

# Additional constraints for depots - only m robots from each depot
for depot in depots:
    problem += pulp.lpSum(x[depot, j] for j in range(n) if j != depot) == 1

# Solve the problem
status = problem.solve()

# Display results
if status == pulp.LpStatusOptimal:
    print(f"Status: {pulp.LpStatus[status]}")
    tours = {k: [] for k in depots}

    for k in depots:
        next_city = k
        while True:
            tours[k].append(next_city)
            next_city = [j for j in range(n) if j != next_city and pulp.value(x[next_city, j]) == 1][0]
            if next_city == k:
                break
        tours[k].append(k)  # To complete the cycle

    for k in depots:
        print(f"Robot at Depot {k} Tour: {tours[k]}")
        tour_cost = sum(euclidean_distance(coordinates[tours[k][i]], coordinates[tours[k][i+1]]) for i in range(len(tours[k])-1))
        print(f"Total Travel Cost for Robot at Depot {k}: {tour_cost:.2f}")
else:
    print("An optimal solution has not been found.")