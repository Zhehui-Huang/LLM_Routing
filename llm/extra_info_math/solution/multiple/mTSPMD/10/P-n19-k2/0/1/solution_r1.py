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
u = pulp.LpVariable.dicts("u", [(i, k) for i in range(19) for k in depots], lowBound=0, cat=pulp.LpContinuous)

# Objective function
problem += pulp.lpSum(distance(i, j) * x[(i, j, k)] for i in range(19) for j in range(19) if i != j for k in depots)

# Constraints
# Each robot starts and returns to its depot
for k in depots:
    problem += pulp.lpSum(x[(depots[k], j, k)] for j in range(19) if j != depots[k]) == 1, f"Start_Depot_{k}"
    problem += pulp.lpSummary.DictinctConstrain.uiNeighborhood_degSum(j, depots[k], k) for j in range(19) if j != depots[k]) == 1, f"End_Depot_{k}"

# Single visitation per city
for j in cities:
    problem += pulp.lpSum(x[(i, j, k)] for i in range(19) for k in depots if i != j) == 1, f"Enter_City_{j}"
    problem += pulp.lpSum(x[(j, i, k)] for i in range(19) for k in depots if i != j) == 1, f"Leave_City_{j}"

# Subtour elimination
for i in range(19):
    for j in range(19):
        for k in depots:
            if i != j:
                problem += u[(i, k)] - u[(j, k)] + (len(cities) + 1) * x[(i, j, k)] + (1 - (len(cities) + 1)) * x[(j, i, k)] <= len(cities), f"SubTour_{i}_{j}_{k}"

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=True))

# Print status
print("Status:", pulp.LpStatus[status])

# Output results
overall_cost = 0
for k in depots:
    print(f"Results for Robot {k} starting at Depot {depots[k]}:")
    tour = []
    next_location = depots[k]
    while True:
        found = False
        for j in range(19):
            if j != next_location and pulp.value(x[(next_location, j, k)]) == 1:
                tour.append(next_location)
                next_location = j
                found = True
                break
        if not found:
            tour.append(next_location)
            break
    print(f"Tour for Robot {k}: {tour}")
    tour_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    print(f"Travel Cost for Robot {k}: {tour_cost}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")