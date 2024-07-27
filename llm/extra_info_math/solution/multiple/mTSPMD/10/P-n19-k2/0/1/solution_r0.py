import pulp
import math

# Given data
coords = {
    0: (30, 40),   # Depot for Robot 0
    1: (37, 52),   # Depot for Robot 1
    2: (49, 43),
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
    13: (58, 27),
    14: (37, 69),
    15: (61, 33),
    16: (62, 63),
    17: (63, 69),
    18: (45, 35),
}

num_robots = 2
depots = {0: 0, 1: 1}
cities = list(range(2, 19))

# Distance function using Euclidean distance
def distance(city1, city2):
    return math.sqrt((coords[city1][0] - coords[city2][0]) ** 2 + (coords[city1][1] - coords[city2][1]) ** 2)

# Setup the problem instance
problem = pulp.LpProblem("Multi_Depot_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(19) for j in range(19) if i != j for k in depots], cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", [(i, k) for i in range(19) for k in depots], lowBound=0, cat=pulp.LpInteger)

# Objective function
problem += pulp.lpSum(distance(i, j) * x[(i, j, k)] for i in range(19) for j in range(19) if i != j for k in depots)

# Each robot begins and ends at its depot
for k in depots:
    problem += pulp.lpSum(x[(depots[k], j, k)] for j in range(19) if j != depots[k]) == 1, f"Start_Depot_{k}"
    problem += pulp.lpSum(x[(j, depots[k], k)] for j in range(19) if j != depots[k]) == 1, f"End_Depot_{k}"

# Each city is visited exactly once by any robot
for j in cities:
    problem += pulp.lpSum(x[(i, j, k)] for i in range(19) for k in depots if i != j) == 1, f"Enter_City_{j}"
    problem += pulp.lpSum(x[(j, i, k)] for i in range(19) for k in depots if i != j) == 1, f"Leave_City_{j}"

# Subtour elimination and route continuity
for i in range(2, 19):
    for j in range(2, 19):
        if i != j:
            for k in depots:
                problem += u[(i, k)] - u[(j, k)] + len(cities) * x[(i, j, k)] <= len(cities) - 1, f"Subtour_{i}_{j}_{k}"

# Solve the problem
status = problem.solve()

# Output results
overall_cost = 0
for k in depots:
    tour = []
    current_location = depots[k]
    while True:
        tour.append(current_location)
        next_locations =  [j for j in range(19) if j != current_location and pulp.value(x[(current_location, j, k)]) == 1]
        if not next_locations:
            break
        current_location = next_locations[0]
    tour.append(depots[k])
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    overall_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")