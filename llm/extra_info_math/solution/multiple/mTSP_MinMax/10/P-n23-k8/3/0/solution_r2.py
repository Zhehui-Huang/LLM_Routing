import pulp
import math

# Define the cities and their coordinates
cities = [ 
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Variables
num_cities = len(cities)
num_robots = 8

def euclidean_distance(index1, index2):
    return math.sqrt((cities[index1][0] - cities[index2][0]) ** 2 + (cities[index1][1] - cities[index2][1]) ** 2)

prob = pulp.LpProblem("VRP", pulp.LpMinimize)

x = pulp.LpVariable.dicts("x", ((k, i, j) for k in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j), cat="Binary")
u = pulp.LpVariable.dicts("u", (k, i) for k in range(num_robots) for i in range(num_cities), lowBound=0, cat='Continuous')

# Objective Function
prob += pulp.lpSum(x[k, i, j] * euclidean_distance(i, j) for k in range(num_robots) for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
for j in range(1, num_cities):  # All cities except the depot city
    prob += sum(x[k, i, j] for k in range(num_robots) for i in range(num_cities) if i != j) == 1
 
for k in range(num_robots):
    for j in range(num_cities):
        prob += sum(x[k, i, j] for i in range(num_cities) if i != j) == sum(x[k, j, i] for i in range(num_cities) if i != j)

    # Start and end at the depot
    prob += sum(x[k, 0, j] for j in range(1, num_cities)) == 1
    prob += sum(x[k, j, 0] for j in range(1, num_cities)) == 1

for k in range(num_robots):
    for i in range(1, num_cities):
        prob += u[k, 0] == 0
        prob += u[k, i] >= 1

# Solve the problem
prob.solve()

# Output solution
for k in range(num_robots):
    tour = [0]
    for i in range(num_cities):
        if i in tour:
            continue
        for j in range(num_cities):
            if j != i and pulp.value(x[k, i, j]) == 1:
                tour.append(j)
                i = j
                break
        if tour[-1] == 0:
            break
    print(f"Robot {k} Tour: {tour}")