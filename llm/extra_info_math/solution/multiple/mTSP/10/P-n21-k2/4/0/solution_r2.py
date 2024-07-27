import pulp
import math
from itertools import product

# Parameters
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]
n = len(coordinates)  # Includes depot
m = 2  # Robots

# Function to calculate Euclidean Distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Decision Variables
prob = pulp.LpProblem("mTSP", pulp.LpMinimize)
x = {(i, j, k): pulp.LpVariable(f'x_{i}_{j}_{k}', cat='Binary')
     for i, j, k in product(range(n), repeat=3) if i != j}
u = {i: pulp.LpVariable(f'u_{i}', lowBound=1, upBound=n-1)
     for i in range(1, n)}

# Objective Function
cost = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i, j in product(range(n), repeat=2)}
prob += pulp.lpSum(cost[i, j] * x[i, j, k] for i, j, k in x)

# Constraints
# Each city except the depot is visited exactly once by exactly one robot
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m) if i != j) == 1

# Each robot must leave and return to the depot
for k in range(m):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination constraints
for i in range(2, n):
    for j in range(2, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + (n-1) * x[i, j, k] <= n-2

# Solve the problem
prob.solve()

# Extracting the solution
routes = {k: [] for k in range(m)}
for k in range(m):
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i, j, k]) == 1:
                routes[k].append((i, j))

# Decode the routes and calculate distances
for k in routes:
    tour = [0]  # start at depot
    next_city = 0
    travel_cost = 0
    while len(tour) < n:
        for (i, j) in routes[k]:
            if i == next_city:
                next_city = j
                tour.append(j)
                travel_out_cost = cost[i, j]
                travel_cost += travel_out_distance
                break
    # include travel back to depot
    travel_cost += cost[next_city, 0]
    tour.append(0)  # complete tour to depot

    print(f'Robot {k} Tour: {tour}')
    print(f'Robot {k} Total Travel Cost: {travel_cost}\n')

total_cost = sum(cost[tour[i], tour[i+1]] for k in routes for tour in routes[k] for i in range(len(tour)-1))
print(f'Overall Total Travel Cost: {total_cost}')