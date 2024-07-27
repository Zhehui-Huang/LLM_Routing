import pulp
import math

# Given data
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

depots = [0, 1, 2, 3]
robots = len(depots)

# Helper function to calculate Euclidean distance
def distance(p1, p2):
    return math.sqrt((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)

# Generate the cost matrix
n = len(cities)
costs = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Set up the problem
problem = pulp.LpProblem("Minimize_Total_Travel_Cost", pulp.LpMinimize)

# Decision variables: x[i][j][k] = 1 if robot k travels from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in depots), 
                          cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(costs[i][j] * x[i][j][k] for i in range(n) for j in range(n) for k in depots)

# Constraints

# Each city is visited exactly once by any robot
for j in range(n):
    if j not in depots:
        problem += pulp.lpSum(x[i][j][k] for i in range(n) for k in depots) == 1

# Maintain continuity from cities
for i in range(n):
    for k in depots:
        if i in depots:
            problem += pulp.lpSum(x[i][j][k] for j in range(n) if j != i) == 1
        else:
            problem += pulp.lpSum(x[i][j][k] for j in range(n)) == \
                       pulp.lpSum(x[j][i][k] for j in range(n))

# Every tour returns to its depot
for k in depots:
    problem += pulp.lpSum(x[j][k][k] for j in range(n) if j != k) == 1

# Solve the problem
problem.solve()

# Output the results
overall_cost = 0

for k in depots:
    tour = [k]
    next_city = k
    tour_cost = 0

    while True:
        next_city = [j for j in range(n) if pulp.value(x[next_city][j][k]) == 1][0]
        tour_cost += costs[tour[-1]][next_city]
        if next_city == k:
            break
        tour.append(next_city)
    
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")
    overall_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_cost}")