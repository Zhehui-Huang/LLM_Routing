from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary, PULP_CBC_CMD, LpStatus
from math import sqrt

# Distance function
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57),
    11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69),
    16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}
n = len(cities)  # Including the depot
num_robots = 2

# Cost matrix
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[i, j] = euclidean_distance(cities[i], cities[j])
        else:
            cost_matrix[i, j] = 0

# Problem
prob = LpProblem("RobotRoutingProblem", LpMinimize)

# Variables
x = LpVariable.dicts("x", (range(n), range(n), range(num_robots)), cat=LpBinary)
u = LpVariable.dicts("u", range(1, n), lowBound=0, upBound=n-1, cat="Continuous")

# Objective
prob += lpSum(x[i][j][k] * cost_matrix[i][j] for i in range(n) for j in range(n) for k in range(num_robots))

# Constraints
# Each city is visited exactly once by one robot, excluding the depot as a repeated back-to point
for j in range(1, n):
    prob += lpSum(x[i][j][k] for i in range(n) for k in range(num_robots)) == 1

# Each robot starts and ends its tour at the depot
for k in range(num_robots):
    prob += lpSum(x[0][j][k] for j in range(1, n)) == 1
    prob += lpSum(x[j][0][k] for j in range(1, n)) == 1

# Subtour elimination
for k in range(num_robots):
    for i in range(2, n):
        for j in range(1, n):
            if i != j:
                prob += u[i] - u[j] + (n-1) * x[i][j][k] <= n-2

# Solve
solver = PULP_CBC_CMD(msg=True)  # This enables solver messages
prob.solve(solver)

# Check the status
status = LpStatus[prob.status]
print("Status:", status)

if status == 'Optimal':
    # Output results
    for k in range(num_robots):
        print(f"Robot {k} Tour: ", end="")
        tour = []
        for i in range(n):
            for j in range(n):
                if x[i][j][k].value() == 1:
                    tour.append((i, j))
        # Reorder the tour starting from the depot
        organized_tour = [0]
        next_location = 0
        while len(organized_tour) < len(tour) + 1:
            for i, j in tour:
                if i == next_location:
                    next_location = j
                    organized_tour.append(j)
                    break
        print(organized_tour)
        
        travel_cost = sum(cost_matrix[organized_tour[i]][organized_tour[i + 1]] for i in range(len(organized_tour) - 1))
        print(f"Robot {k} Total Travel Cost: {travel_cost}")

else:
    print("Problem may not be solvable or may require more time or different solver settings.")