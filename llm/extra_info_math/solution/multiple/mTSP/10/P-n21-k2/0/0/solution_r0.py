import pulp
import math
from itertools import product

# Define cities and their coordinates
cities = {
    0: (30, 40),
    1: (37, 52),
    2: (49, 49),
    3: (52, 64),
    4: (31, 62),
    5: (52, 33),
    6: (42, 41),
    7: (52, 41),
    8: (57, 58),
    9: (62, 42),
    10: (42, 57),
    11: (27, 68),
    12: (43, 67),
    13: (58, 48),
    14: (58, 27),
    15: (37, 69),
    16: (38, 46),
    17: (61, 33),
    18: (62, 63),
    19: (63, 69),
    20: (45, 35)
}

# Compute pairwise distances (Euclidean)
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

n = len(cities) # Total nodes, including depot
m = 2  # Number of robots

# Setting up the problem
problem = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)], 
                          cat='Binary', lowBound=0, upBound=1)
u = pulp.LpVariable.dicts("u", [i for i in range(n)], lowBound=0, upBound=n-1, cat='Continuous')

# Objective function
problem += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(n) for j in range(n) if i != j for k in range(m))

# Constraints
for j in range(1, n):  # Exclude depot when considering visiting each city once
    problem += pulp.lpSum(x[i, j, k] for i in range(n) if i != j for k in range(m)) == 1

for k in range(m):
    for i in range(n):
        problem += pulp.lpSum(x[i, j, k] for j in range(n) if i != j) == pulp.lpSum(x[j, i, k] for j in range(n) if i != j)

for k in range(m):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n) * x[i, j, k] <= n - 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

if status == pulp.LpStatusOptimal:
    print("Solution Found")
    solution = {}
    for k in range(m):
        tour = [0]
        next_city = 0
        while True:
            next_city = [j for j in range(n) if pulp.value(x[next_city, j, k]) == 1][0]
            if next_city == 0:
                break
            tour.append(next_city)
        tour.append(0)  # returning to the depot
        solution[k] = tour

        travel_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {travel_cost}")

    overall_cost = sum(distance(tour[i], tour[i+1]) for k in range(m) for i in range(len(solution[k])-1))
    print(f"Overall Total Travel Cost: {overall_cost}")
else:
    print("Solution Not Found")