import math
from pulp import *

# Defining the coordinates including the depot
coords = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252), 5: (163, 247),
    6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236), 10: (148, 232),
    11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189), 20: (155, 185), 21: (139, 182)
}

# Function to calculate Euclidean distance between cities
def distance(i, j):
    return math.sqrt((coords[i][0] - coords[j][0])**2 + (coords[i][1] - coords[j][1])**2)

# Number of salesmen (robots)
m = 4

# The number of nodes including the depot
n = len(coords)

# Create the problem
prob = LpProblem("MTSP", LpMinimize)

# Creating variables
x = LpVariable.dicts('x', ((i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)), cat='Binary')
u = LpVariable.dicts('u', range(1, n), lowBound=0, cat='Continuous')

# Objective function: Minimize the maximum distance traveled by any robot
max_distance = LpVariable('max_distance')
prob += max_distance

# Constraints
# 1. Each city is visited exactly once by exactly one robot
for j in range(1, n):
    prob += lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

# 2. Each robot must start and end at the depot
for k in range(m):
    prob += lpSum(x[0, j, k] for j in range(1,n)) == 1
    prob += lpSum(x[i, 0, k] for i in range(1,n)) == 1

# 3. Flow conservation
for k in range(m):
    for j in range(1, n):
        prob += lpSum(x[i, j, k] for i in range(n) if i != j) - lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# 4. Subtour Elimination
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                prob += u[i] - u[j] + (n-1) * x[i, j, k] <= n-2

# Define max_distance constraint
for k in range(m):
    prob += lpSum(x[i, j, k] * distance(i, j) for i in range(n) for j in range(n) if i != j) <= max_distance

# Solve the problem
prob.solve(PULP_CBC_CMD(msg=False))

# Extract the results
tour_costs = {}
tours = {k: [] for k in range(m)}

for k in range(m):
    current_location = 0  # Start at the depot
    route = [current_location]
    cost = 0

    while True:
        next_city = [j for j in range(n) if j != current_location and pulp.value(x[current_location, j, k]) == 1]
        if not next_city:
            break
        next_city = next_city[0]
        cost += distance(current_location, next_city)
        current_location = next_city
        route.append(current_location)
        if current_location == 0:
            break

    tours[k] = route
    tour_costs[k] = cost

# Display results
print("Tours and Costs for Each Robot:")
for k in tours:
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_costs[k]}")

max_cost = pulp.value(max_distance)
print("\nMaximum Travel Cost: {:.2f}".format(max_cost))