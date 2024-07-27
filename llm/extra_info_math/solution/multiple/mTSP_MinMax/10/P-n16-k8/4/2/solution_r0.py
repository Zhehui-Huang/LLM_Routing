import pulp
import math

# Define coordinates for each city, including depot
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

num_cities = len(cities)
robots = 8

# Euclidean distance calculator
def calc_distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("RobotVRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(num_cities) for j in range(num_cities) if i != j for k in range(robots)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, upBound=num_cities-1, cat='Continuous')

# Objective
problem += pulp.lpSum(calc_distance(i, j) * x[i, j, k] for i in range(num_cements) for j in range(num_cities) if i != j for k in range(robots))

# Constraints

# Each city visited exactly once by any robot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) if i!=j for k in range(robots)) == 1
    
# Flow conservation constraints
for k in range(robots):
    for p in range(num_cities):
        problem += pulp.lpSum(x[p, j, k] for j in range(num_cities) if j!=p) - pulp.lpSum(x[i, p, k] for i in range(num_cities) if i!=p) == 0

# Each robot leaves the depot once
for k in range(robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1

# Subtour elimination
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(robots):
                problem += u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Output results
tour_cost = {k: 0 for k in range(robots)}
tours = {k: [] for k in range(robots)}

for k in range(robots):
    tour = [0]
    next_city = next(j for j in range(1, num_cities) if x[0, j, k].varValue > 0.9)
    while next_city != 0:
        tour.append(next_city)
        next_city = next(j for j in range(num_cities) if j != tour[-1] and x[tour[-1], j, k].varValue > 0.9)
        if next_city == 0:
            break
    tour.append(0)
    tours[k] = tour
    tour_cost[k] = sum(calc_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Printing
for k in range(robots):
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {tour_cost[k]}")

max_cost = max(tour_cost.values())
print(f"Maximum Travel Cost: {max_cost}")