import pulp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), 
    (32, 39), (56, 37)
]

# Parameters
num_cities = len(coordinates)
num_robots = 8
depot = 0

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

# Distance matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Create the problem
prob = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities), range(num_robots)), 0, 1, pulp.LpBinary)

# Objective function
prob += pulp.lpSum([cost[i][j] * x[i][j][k] for k in range(num_robots) for i in range(num_cities) for j in range(num_cities)])

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, num_cities):
    prob += pulp.lpSum([x[i][j][k] for k in range(num_robots) for i in range(num_cities)]) == 1

# Flow conservation
for k in range(num_robots):
    for j in range(1, num_cities):
        prob += pulp.lpSum([x[i][j][k] for i in range(num_cities)]) == pulp.lpSum([x[j][i][k] for i in range(num_cities)])

# Leave and return to the depot
for k in range(num_robots):
    prob += pulp.lpSum([x[depot][j][k] for j in range(1, num_cities)]) == 1
    prob += pulp.lpSum([x[j][depot][k] for j in range(1, num_cities)]) == 1

# Subtour elimination
u = pulp.LpVariable.dicts('u', range(1, num_cities), 1, num_cities - 1, pulp.LpInteger)
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                prob += u[i] - u[j] + (num_cities - 1) * x[i][j][k] <= num_cities - 2

# Solve the problem
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Printing results
total_cost = 0
for k in range(num_robots):
    tour = [depot]
    while True:
        for j in range(num_cities):
            if pulp.value(x[tour[-1]][j][k]) == 1:
                tour.append(j)
                break
        if tour[-1] == depot:
            break
    tour_cost = sum(cost[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travel Cost: {total_cost}")