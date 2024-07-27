import pulp
import math

# Setup
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
num_cities = len(cities)
robots = 8

# Distance function
def calc_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Problem
problem = pulp.LpProblem("RobotVRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) if i != j for k in range(robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", range(1, num_cities), cat='Continuous')

# Objective
max_distance = pulp.LpVariable("max_distance")
problem += max_distance

# Distance constraints and max distance update
for k in range(robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j:
                problem += x[i, j, k] * calc_distance(i, j) <= max_distance

# Constraints
# Visit each city exactly once
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(robots) if i != j) == 1

# Connectivity constraints
for k in range(robots):
    for j in range(num_cities):
        problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) if i != j) == pulp.lpSum(x[j, i, k] for i in range(num_cities) if i != j)

# Subtour prevention
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(robots):
                problem += u[i] - u[j] + (num_cities-1) * x[i, j, k] <= num_cities - 2

# Solve
problem.solve()

# Results
tour_cost = dict()
tours = {k: [0] for k in range(robots)}

for k in range(robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if i != j and pulp.value(x[i, j, k]) == 1:
                tours[k].append(j)

    # Calculate travel cost for each robot tour
    tour_distance = sum(calc_distance(tours[k][i], tours[k][i+1]) for i in range(len(tours[k])-1))
    tour_cost[k] = tour_distance
    print(f"Robot {k} Tour: {tours[k]} -> {tour_cost[k]}")

# Find maximum travel cost across robots
max_travel_cost = max(tour_cost.values())
print(f"Maximum Travel Cost: {max_travel_cost}")