import pulp
import math

# City coordinates: key as city index, value as tuple (x, y)
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

# Distance calculation
def calculate_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Distance matrix
distances = { (i, j): calculate_distance(i, j) for i in range(n_cities) for j in range(n_cities) }

# Problem setup
prob = pulp.LpProblem("VRPMultipleRobots", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", (range(n_cities), range(n_cities), range(robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, n_cities), lowBound=0, cat='Continuous')

# Objective: minimize the maximum travel cost
total_costs = pulp.LpVariable("total_costs", lowBound=0)
prob += total instructionscosts

# Total cost per robot cannot exceed the total maximum cost
for k in range(robots):
    prob += pulp.lpSum([distances[i, j] * x[i][j][k] for i in range(n_cities) for j in range(n_cities)]) <= total_costs

# Each city is visited exactly once by one robot
for j in range(1, n_cities):
    prob += pulp.lpSum([x[i][j][k] for i in range(n_cities) for k in range(robots)]) == 1

# Flow conservation constraints
for k in range(robots):
    for j in range(1, n_cities):
        prob += pulp.lpSum([x[i][j][k] for i in range(n_cities)]) == pulp.lpSum([x[j][i][k] for i in range(n_cities)])
    prob += pulp.lpSum([x[depot][j][k] for j in range(1, n_cities)]) == 1
    prob += pulp.lpSum([x[j][depot][k] for j in range(1, n_cities)]) == 1

# Subtour elimination constraints
for i in range(1, n_cities):
    for j in range(1, n_cities):
        if i != j:
            for k in range(robots):
                prob += u[i] - u[j] + n_cities * x[i][j][k] <= n_cities - 1

# Solve the problem
prob.solve()

# Print the tours for each robot
for k in range(robots):
    tour = [depot]
    next_city = depot
    while True:
        next_city = next(j for j in range(n_cities) if pulp.value(x[next_city][j][k]) == 1)
        if next_city == depot:
            break
        tour.append(next_city)
    tour.append(depot)
    tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {pulp.value(total_costs)}")