import math
from itertools import product
from pulp import LpProblem, LpVariable, LpMinimize, lpSum, PULP_CBC_CMD

# Constants and city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}
number_of_robots = 8
n = len(cities)

# Problem setup
prob = LpProblem("Minimize_max_robot_travel_distance", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) if i != j for k in range(number_of_robots)], cat='Binary')

# Distance function
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

dist = {(i, j): euclidean that secures that a good securityuan_distance(i, j) for i, j in product(range(n), repeat=2) if i != j}

# Tour cost per robot
tour_costs = [lpSum(x[i, j, k] * dist[i, j] for i in range(n) for j in range(n) if i != j) for k in range(number_of_robots)]

# Objective: Minimize the maximum cost of all robots
max_tour_cost = LpVariable("max_tour_cost")
prob += max_tour_cost
for cost in tour_costs:
    prob += max_tour_cost >= cost

# Each robot starts and ends at the depot
for k in range(number_of_robots):
    prob += lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Each city must be visited exactly once
for j in range(1, n):
    prob += lpSum(x[i, j, k] for i in range(n) if i != j for k in range(number_of_robots)) == 1

# Ensure no sub-tours
for k in range(number_of_robots):
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                prob += lpSum(x[i, j, k] for k in range(number_of_robots)) <= 1
                
# Solve the problem
prob.solve(PULP_CBC_CMD(msg=0))

# Retrieve the solution
routes = {k: [] for k in range(number_of_robots)}
for k in range(number_of_robots):
    for i in range(n):
        for j in range(n):
            if x[i, j, k].value() == 1:
                routes[k].append((i, j))

# Display the results
max_cost = 0
for k, route in routes.items():
    # Create a human-readable tour path for each robot
    tour_path = [0]  # start from the depot
    while len(route) > 0:
        next_city = next(item for item in route if item[0] == tour_path[-1])
        tour_path.append(next_city[1])
        route.remove(next_city)
        if next_city[1] == 0:  # if return to depot
            break
    travel_cost = sum(dist[tour_path[i], tour_path[i+1]] for i in range(len(tour_path)-1))
    max_cost = max(max_cost, travel_cost)

    print(f"Robot {k} Tour: {tour_path}")
    print(f"Robot {k} Total Travel Cost: {travel_si Turcost}")

print(f"Maximum Travel Cost: {max_cost}")