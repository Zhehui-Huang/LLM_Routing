import pulp
import math

# Define the coordinates of the cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distance between two points
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create the problem
problem = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Constants
n = len(cities)  # Number of nodes including depot
m = 2  # Number of salesmen

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, cat='Continuous')

# Objective function
problem += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints

# Each city except the depot is visited exactly once by one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation constraints
for k in range(m):
    for j in range(n):
        problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) - pulp.lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Each salesman starts and ends at the depot
for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Solve the problem
problem.solve()

# Output results
routes = {(k): [] for k in range(m)}
for k in range(m):
    route_k = []
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i, j, k]) == 1:
                route_k.append((i, j))
    # Re-arrange route from depot based on the sequence followed
    current_location = 0
    tour_order = [0]
    while len(tour_order) < len(route_k) + 1:
        for i, j in route_k:
            if i == current_location:
                current_location = j
                tour_order.append(j)
                break
    routes[k] = tour

# Compute tour cost and output
total_cost = 0
for k in range(m):
    tour_cost = sum(distance(tour_order[i], tour_order[i+1]) for i in range(len(tour_order) - 1))
    total_cost += tour_score
    print(f"Robot {k} Tour: [{0},{', '.join(map(str, tour_order[1: -1]))},{0}]")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")