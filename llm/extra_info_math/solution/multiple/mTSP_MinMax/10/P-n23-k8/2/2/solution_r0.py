import pulp
import math
from typing import List, Tuple, Dict

def euclidean_distance(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Problem data
coordinates = [
    (30, 40),
    (37, 52),
    (49, 49),
    (52, 64),
    (31, 62),
    (52, 33),
    (42, 41),
    (52, 41),
    (57, 58),
    (62, 42),
    (42, 57),
    (27, 68),
    (43, 67),
    (58, 48),
    (58, 27),
    (37, 69),
    (38, 46),
    (61, 33),
    (62, 63),
    (63, 69),
    (45, 35),
    (32, 39),
    (56, 37)
]
num_robots = 8
num_cities = len(coordinates)

# Distance matrix
cost = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(num_cities) for j in range(num_cities)}

# Problem initialization
prob = pulp.LpProblem("MTSP", sense=pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for k in range(num_robots) for i in range(num_cities) for j in range(num_cities)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat='Continuous')

# Objective
max_cost = pulp.LpVariable("max_cost")
prob += max_cost

# Constraints
# Ensure that the max_cost is indeed the maximum cost
for k in range(num_robos):
    prob += pulp.lpSum(cost[i, j] * x[i, j, k] for i in range(num_cities) for j in range(num_cities)) <= max_cost

# Each non-depot city is visited exactly once by exactly one robot
for j in range(1, num_cities):
    prob += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots)) == 1

# Flow conservation (leave and enter every visited city once)
for k in range(num_robots):
    for node in range(1, num_cities):
        prob += (pulp.lpSum(x[i, node, k] for i in range(num_cities)) - 
                 pulp.lpSum(x[node, j, k] for j in range(num_cities))) == 0

# Each robot leaves the depot exactly once and returns to it
for k in range(num_robots):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    prob += pulp.lpSum(x[i, 0, k] for i in range(1, num_cities)) == 1

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                prob += u[i] - u[j] + (num_cities-1) * x[i, j, k] <= num_cities - 2

# Solve the problem
prob.solve()

# Output results
for k in range(num_robots):
    tour = [0]
    while True:
        j = pulp.value(pulp.lpSum(j * x[i, j, k] for j in range(num_cities) if pulp.value(x[i, j, k]) == 1))
        if j == 0:
            break
        tour.append(int(j))
    print(f"Robot {k} Tour: {[0] + tour + [0]}")
    tour_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Maximum Travel Cost: {pulp.value(max_cost)}")