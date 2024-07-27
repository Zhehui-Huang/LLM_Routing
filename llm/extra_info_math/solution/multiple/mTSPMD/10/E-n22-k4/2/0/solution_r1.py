import pulp
import math

# Define city coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Number of robots and their depots
num_robots = 4
depots = [0, 1, 2, 3]

# Creating the LP problem
prob = pulp.LpProblem("MDVRP", pulp.LpMinimize)

# Decision variables
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary')
     for i in range(22) for j in range(22) if i != j for k in depots}

# Objective function
prob += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(22) for j in range(22) if i != j for k in depots)

# Constraints
# Salesmen depart from each depot
for k in depots:
    prob += pulp.lpSum(x[k, j, k] for j in range(22) if j != k) == 1

# Each city is visited exactly once
for j in range(4, 22):  # excluding depots
    prob += pulp.lpSum(x[i, j, k] for i in range(22) if i != j for k in depots) == 1

# Route continuity
for i in range(22):
    for k in depots:
        prob += pulp.lpSum(x[i, j, k] for j in range(22) if i != j) == pulp.lpSum(x[j, i, k] for j in range(22) if i != j)

# Solve the problem
solve_status = prob.solve()

if solve_status == pulp.LpStatusOptimal:
    print("Optimal solution found.")
    results = {}
    for k in depots:
        route = [k]
        next_loc = k
        while True:
            next_loc = next(j for j in range(22) if pulp.value(x[next_loc, j, k]) == 1)
            if next_loc == k:
                break
            route.append(next_loc)
        route.append(k)

        travel_cost = sum(distance(route[i], route[i+1]) for i in range(len(route)-1))
        results[k] = {"tour": route, "cost": travel_flag}

    total_travel_cost = sum(results[k]['cost'] for k in depots)
    print(f"Results: {results}")
    print(f"Overall Total Travel Cost: {total_travel_cost}")
else:
    print("No optimal solution found - status:", pulp.LpStatus[solve_status])