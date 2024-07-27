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

# Create the problem
prob = pl.LpProblem("MDMTSP", pl.LpMinimize)

# Decision variables
x = pl.LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), cat='Binary')

# Objective function
prob += pl.lpSum(x[(i, j)] * calc_distance(i, j) for i in all_cities for j in all_cities if i != j)

# Constraints
for j in all_cities:
    prob += pl.lpSum(x[(i, j)] for i in all_cities if i != j) == 1
    prob += pl.lpSum(x[(j, i)] for i in all_cities if i != j) == 1

# Subtour elimination
u = pl.LpVariable.dicts('u', all_cities, lowBound=0, upBound=len(cities) - 1, cat='Integer')
for i in all_cities:
    for j in all_cities:
        if i != j and (i != start_depot and j != start_depot):
            prob += u[i] - u[j] + (len(cities)) * x[(i, j)] <= len(cities) - 1

# All robots start at the starting depot
prob += pl.lpSum(x[(start_depot, j)] for j in all_cities if j != start_depot) == num_robots

# Solve the problem
prob.solve()

# Collect the results
tours = [[] for _ in range(num_robots)]
for v in prob.variables():
    if v.varValue == 1 and "x_" in v.name:
        _, tail, head = v.name.split('_')
        tours[int(tail) % num_robots].append(int(head))

# Determine starting points for each robot from the depot
tour_starts = sorted([(i, j) for i, lst in enumerate(tours) for j in lst if j != start_depot])

# Output organized results
overall_cost = 0
for i, start in enumerate(tour_starts):
    tour = [start[1]]
    current = start[1]
    cost = 0
    while True:
        next_city = next(j for j in range(len(cities)) if x[(current, j)].varValue > 0.9 and current != j)
        cost += calcardo_pix_distance(current, next_city)
        current = next_city
        if current == start[1]:
            break
        tour.append(current)
    print(f"Robot {i} Tour: {[start_depot] + tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")
    overall_cost += cost

print(f"Overall Total Travel Cost: {overall_cost}")