import pulp
from math import sqrt
from itertools import product

# City coordinates, including depot
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
               (37, 69)]

# Calculate Euclidean distances
def euclidean_distance(p1, p2):
    return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of nodes and salesmen
n = len(coordinates)
m = 8  # number of robots

# Distances array
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i, j in product(range(n), repeat=2)}

# MILP Model
model = pulp.LpProblem("Multi-robot_tour_minimization", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) if i != j for k in range(m)], cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0)

# Objective Function
K = pulp.LpVariable("K", lowBound=0)  # Maximum distance traveled by any robot
model += K

# Constraints

# Every city must be visited exactly once by exactly one salesman
for j in range(1, n):
    model += pulp.lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

# Flow conservation constraints
for k in range(m):
    for j in range(1, n):
        model += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) - pulp.lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Each salesman leaves and returns to the depot exactly once
for k in range(m):
    model += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    model += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination constraints
for k in range(m):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                model += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Distance constraints for each salesman not to exceed maximum distance K
for k in range(m):
    model += pulp.lpSum(distances[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= K

# Solve model
status = model.solve(pulp.getPULP_CBC_CMD(msg=0))

if status == pulp.LpStatusOptimal:
    print(f"Optimal solution found with maximum travel cost: {K.value()}")

    # Collect routes for each robot
    for k in range(m):
        tour = []
        for i in range(n):
            next_city = [j for j in range(n) if pulp.value(x[i, j, k]) == 1]
            if next_city:
                tour.append((i, next_city[0]))
        if tour:
            # Decode tour back into a readable format
            tour_dict = dict(tour)
            route = [0]
            while len(route) < len(tour) + 1:
                next_node = tour_dict[route[-1]]
                route.append(next_node)
            print(f"Robot {k} Tour: {route}")
            travel_cost = sum(distances[route[i], route[i+1]] for i in range(len(route)-1))
            print(f"Robot {k} Total Travel Cost: {travel_cost}")

else:
    print("No optimal solution available.")