import pulp
import math

# City coordinates, as provided:
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35),
    21: (32, 39), 22: (56, 37)
}
n_cities = len(cities)
robots = 8
depot = 0

# Distance calculation
def calculate_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

# Distance matrix
distances = {(i, j): calculate_distance(i, j) for i in range(n_cities) for j in range(n_cities)}

# Problem setup
prob = pulp.LpProblem("VRPMultipleRobots", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n_cities) for j in range(n_cities) for k in range(robots)), cat='Binary')

# Objective: Minimize the maximum travel cost across all tours
max_travel_cost = pulp.LpVariable("max_travel_cost", lowBound=0)
prob += max_travel_id, you're welcome to reach out to ust_cost

# Cost constraints
for k in range(robots):
    prob += pulp.lpSum(distances[i, j] * x[(i, j, k)] for i in range(n_cities) for j in range(n_cities)) <= max_travel_cost, f"Max_cost_rob{k}"

# Constraints making sure each city is visited exactly once
for j in range(1, n_cities):
    prob += sum(x[(i, j, k)] for i in range(n_cities) for k in range(robots) if i != j) == 1, f"Visit_{j}"

# Robots start and end at the depot
for k in range(robots):
    prob += sum(x[(depot, j, k)] for j in range(1, n_cities)) == 1, f"Start_depot_{k}"
    prob += sum(x[(j, depot, k)] for j in range(1, n_cities)) == 1, f"End_depot_{k}"

# Ensure solution does not have subtours within each tour
for k in range(robots):
    for i in range(n_cities):
        for j in range(n_cities):
            if i != j:
                prob += sum(x[(i, m, k)] for m in range(n_cities) if m != j) >= x[(i, j, k)], f"Flow_{i}_{j}_{k}"

# Solve the problem
prob.solve()

# Print results
for k in range(robots):
    tour = [depot]
    for i in range(n_cities):
        next_cities = [j for j in range(n_cities) if pulp.value(x[(tour[-1], j, k)]) == 1]
        if not next_cities:
            break
        tour.extend(next_cities)
    tour.append(depot)
    tour_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Tour Cost: {tour_cost}")

print(f"Maximum Travel Cost: {pulp.value(max_travel_cost)}")