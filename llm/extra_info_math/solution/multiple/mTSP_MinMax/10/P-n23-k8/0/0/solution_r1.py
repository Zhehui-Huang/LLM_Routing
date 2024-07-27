import pulp
import math

# Cities coordinates defined as previously given in the problem statement:
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}
n_cities = len(cities)
robots = 8
depot = 0

# Function to calculate Euclidean distance between two cities:
def calculate_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Distance matrix
distances = {(i, j): calculate_distance(i, j) for i in range(n_cities) for j in range(n_cities)}

# Problem setup
prob = pulp.LpProblem("VRPMultipleRobots", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", (range(n_cities), range(n_cities), range(robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n_cities), lowBound=0, cat='Continuous')

# Objective to minimize the maximum distance traveled by any robot
total_costs = pulp.LpVariable("total_costs", lowBound=0)
prob += total_costs

# Constraint: Total cost per robot cannot exceed the maximum cost
for k in range(robots):
    prob += pulp.lpSum(distances[i, j] * x[i][j][k] for i in range(n_cities) for j in range(n_cities)) <= total_costs

# Constraint: Each city is visited exactly once by any robot
for j in range(1, n_cities):
    prob += pulp.lpSum(x[i][j][k] for i in range(n_cities) for k in range(robots) if i != j) == 1

# Robot should return to the depot
for k in range(robots):
    prob += pulp.lpSum(x[depot][j][k] for j in range(1, n_cities)) == 1
    prob += pulp.lpSum(x[j][depot][k] for j in range(1, n_cities)) == 1

# Flow conservation and sub-tour elimination constraints
for k in range(robots):
    for j in range(1, n_cities):
        prob += pulp.lpSum(x[i][j][k] for i in range(n_cities) if i != j) == (
            pulp.lpSum(x[j][i][k] for i in range(n_cities) if i != j))
for i in range(1, n_cities):
    for j in range(1, n_cities):
        if i != j:
            prob += u[i] - u[j] + n_cities * pulp.lpSum(x[i][j][k] for k in range(robots)) <= n_cities - 1

# Solving problem
prob.solve()

# Assess and print the resulting tours and costs
max_cost = 0
for k in range(robots):
    tour = []
    current_city = depot
    while True:
        next_cities = [j for j in range(n_cities) if pulp.value(x[current_city][j][k]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        tour.append(next_city)
        current_city = next_city
        if current_city == depot:
            break
    tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    max_cost = max(max_cost, tour_cost)
    print(f"Robot {k} Tour: {[depot] + tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {max_cost}")