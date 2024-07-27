import pulp as pl
import math

# Define the city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Calculate Euclidean distance between two cities
def calc_distance(cid1, cid2):
    return math.sqrt((cities[cid1][0] - cities[cid2][0]) ** 2 + (cities[cid1][1] - cities[cid2][1]) ** 2)

# Number of robots
num_robots = 8
all_cities = list(cities.keys())
start_depot = 0
robots = range(num_robots)

# Create the problem
prob = pl.LpProblem("MDMTSP", pl.LpMinimize)

# Decision variables
x = pl.LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), cat='Binary')

# Objective function
prob += pl.lpSum(x[(i, j)] * calc_distance(i, j) for i in all_cities for j in all_cities if i != j)

# Each city must be visited exactly once and leave exactly once
for j in all_cities:
    prob += pl.lpSum(x[(i, j)] for i in all_cities if i != j) == 1
    prob += pl.lpSum(x[(j, i)] for i in all_cities if i != j) == 1

# Subtour elimination
u = pl.LpVariable.dicts('u', all_cities, lowBound=0, upBound=len(cities) - 1, cat='Integer')
for i in all_cities:
    for j in all_cities:
        if i != j and (i != start_depot and j != start_depot):
            prob += u[i] - u[j] + (len(cities)) * x[(i, j)] <= len(cities) - 1

# Each robot leaves the starting depot
prob += pl.lpSum(x[(start_deposit, j)] for j in all_cities if j != start_depot) == num_robots

# Solve the problem
prob.solve()

# Retrieve the tours for each robot
tours = {r: [] for r in robots}
for v in prob.variables():
    if v.varValue == 1 and v.name.startswith('x'):
        _, (i, j) = v.name.split('_')
        i, j = int(i), int(j)
        tours[i % num_robots].append((i, j))

# Print solution
total_cost = 0
for r, tour in tours.items():
    print(f"Robot {r} Tour:", [i for i, _ in tour])
    tour_cost =  sum(calc_distance(i, j) for i, j in tour)
    total_cost += tour_cost
    print(f"Robot {r} Total Travel Cost: {tourCost}")
print(f"Overall Total Travel Cost: {total_cost}")