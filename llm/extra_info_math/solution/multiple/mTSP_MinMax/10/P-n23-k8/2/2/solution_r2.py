import pulp
import math

# Helper function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Define coordinates and initializes problem
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
num_cities = len(coordinates)
num_robots = 8

# Creating a LP problem
prob = pulp.LpProblem("Multi-TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat='Continuous')

# Objective: Minimize the maximum distance traveled by any robot
prob += pulp.lpSum(x[i, j, k] * euclidean_distance(coordinates[i], coordinates[j]) for i in range(num_Cities) for j in range(num_cities) for k in range(num_robots))

# Constraints
# 1. Each city must be visited exactly once excluding the depot
for j in range(1, num_cities):
    prob += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots) if i != j) == 1

# 2. Each robot must start and end at the depot
for k in range(num_robots):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    prob += pulp.lpSum(x[i, 0, k] for i in range(1, num_cities)) == 1

# 3. Subtour elimination
for k in range(num_robots):
    for i in range(1, num_cities):
        for j in range(1, num_cities):
            if i != j:
                prob += u[i] - u[j] + (num_cities * x[i, j, k]) <= num_cities - 1

# Solve problem
prob.solve()

# Retrieve the solution
tours = {k: [] for k in range(num_robots)}
for k in range(num_robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[i, j, k]) == 1:
                tours[k].append((i, j))

# Parse tours to readable form and calculate costs
for k in tours:
    tour = tours[k]
    path = [0]  # start at depot
    next_city = 0
    travel_distance = 0
    while len(tour) > 0:
        for i, (from_city, to_city) in enumerate(tour):
            if from_city == next_city:
                travel_distance += euclidean_distance(coordinates[from_city], coordinates[to_city])
                next_city = to_city
                path.append(to_city)
                tour.pop(i)
                break
    print("Robot", k, "Tour:", path)
    print("Robot", k, "Travel Cost:", round(travel_distance, 2))

# Extract and print the maximum travel cost
max_distance = max(round(euclidean_distance(coordinates[path[i]], coordinates[path[i + 1]]), 2) for i in range(len(path) - 1))
print("Maximum Travel Cost:", max_distance)