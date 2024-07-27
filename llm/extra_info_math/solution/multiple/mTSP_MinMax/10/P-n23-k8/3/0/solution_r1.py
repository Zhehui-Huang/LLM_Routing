import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

# Number of robots
num_robots = 8

# Initialize the problem
prob = pulp.LpProblem("Minimax_Multiple_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in cities for j in cities if i != j for k in range(num_robots)), 
                          cat='Binary')

u = pulp.LpVariable.dicts("u", (i for i in cities if i != 0), 
                          lowBound=1, upBound=len(cities)-1, cat='Integer')

max_distance = pulp.LpVariable("max_distance")

# Objective: Minimize the maximum distance traveled by any robot
prob += max_distance

# Constraints
# Ensure every city is covered exactly once by any robot
for j in cities:
    if j != 0:
        prob += pulp.lpSum(x[i, j, k] for i in cities if i != j for k in range(num_robots)) == 1

# Each robot leaves and enters the depot
for k in range(num_robots):
    prob += pulp.lpSum(x[0, j, k] for j in cities if j != 0) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in cities if j != 0) == 1

# Each robot's tour management
for k in range(num_robots):
    for j in cities:
        prob += pulp.lpSum(x[i, j, k] for i in cities if i != j) == pulp.lpSum(x[j, i, k] for i in cities if i != j)

# Subtour elimination
for i in cities:
    if i != 0:
        for j in cities:
            if i != j and j != 0:
                for k in range(num_robots):
                    prob += u[i] - u[j] + (len(cities) - 1) * x[i, j, k] <= len(cities) - 2

# Distance constraints
for k in range(num_robots):
    prob += pulp.lpSum(x[i, j, k] * math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2) for i in cities for j in cities if i != j) <= max_distance

# Solve the problem
status = prob.solve()
print(f"Status: {pulp.LpStatus[status]}")

# Output results
for k in range(num_robots):
    tour = []
    for i in cities:
        for j in cities:
            if pulp.value(x[i,j,k]) == 1:
                tour.append((i, j))
    print(f"Robot {k} Tour: {tour}")

print(f"Optimal maximum distance: {pulp.value(max_distance)}")