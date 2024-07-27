import pulp
import math

# Define the cities and their coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Function to calculate Euclidean distance
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Total number of cities (including depot)
n = len(coordinates)
# Number of robots (salesmen)
m = 4

# Setup the problem
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective function
prob += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Each salesman departs from the depot exactly once
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1

# Each salesman arrives at the depot exactly once
for k in range(m):
    prob += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Flow conservation constraints for each salesman and each city
for k in range(m):
    for p in range(1, n):
        prob += (pulp.lpSum(x[p, j, k] for j in range(n) if j != p) 
                 - pulp.lpSum(x[i, p, k] for i in range(n) if i != p) == 0)

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n-1) * x[i, j, k] <= n-2

# Solve the problem
prob.solve()

# Output tours and calculate costs
overall_cost = 0
for k in range(m):
    tour = []
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j, k]) == 1:
                tour.append((i, j))
    # Generate actual tour paths
    current_city = 0
    path = [0]
    cost = 0
    while len(tour) > 0:
        for i, (fr, to) in enumerate(tour):
            if fr == current_city:
                path.append(to)
                cost += distance(fr, to)
                current_city = to
                tour.pop(i)
                break
    path.append(0)
    cost += distance(current_city, 0)  # return to depot
    overall_cost += cost
    print(f"Robot {k} Tour: {path}")
    print(f"Robot {k} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")