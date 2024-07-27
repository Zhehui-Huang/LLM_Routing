import math
from pulp import *

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Robots & their depots
robots = list(range(8))  # Robot ids: 0 to 7
depots = list(range(8))  # Depots are cities 0 to 7

# Function to calculate Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Setting up the optimization problem
prob = LpProblem("VRP_with_Multiple_Depots_and_Robots", LpMinimize)

# Decision variables: x[i][j][k] where robot k travels from city i to city j
x = LpVariable.dicts("x", [(i, j, k) for k in robots for i in range(n) for j in range(n)], 0, 1, LpBinary)

# Objective Function
prob += lpSum(distance_matrix[i][j] * x[(i, j, k)] for k in robots for i in range(n) for j in range(n))

# Constraints
# Each robot starts and ends at its assigned depot
for k in robots:
    prob += lpSum(x[(k, j, k)] for j in range(n) if j != k) == 1  # Leave depot
    prob += lpSum(x[(j, k, k)] for j in range(n) if j != k) == 1  # Return to depot

# Each city is visited exactly once by exactly one robot
for j in range(n):
    if j not in depots:
        prob += lpSum(x[(i, j, k)] for k in robots for i in range(n)) == 1
        prob += lpSum(x[(j, i, k)] for k in robots for i in range(n)) == 1

# Subtour elimination
for k in robots:
    u = LpVariable.dicts("u", range(n), 0, n-1, LpInteger)
    for i in range(n):
        for j in range(n):
            if i != j and (i != k or j != k):
                prob += u[i] - u[j] + (n-1) * x[(i, j, k)] <= n-2

# Solve the problem
prob.solve()

# Printing the results
if prob.status == 1:
    total_cost = 0
    for k in robots:
        print(f"Robot {k} Tour: ", end="")
        tour = []
        current_location = k
        while True:
            found = False
            for j in range(n):
                if x[(current_location, j, k)].varValue == 1:
                    tour.append(j)
                    current_location = j
                    found = True
                    break
            if not found or current_location == k:
                tour.append(k)
                break
        print(tour)
        tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
        total_cost += tour_cost
        print(f"Robot {k} Total Travel Cost: {tour_cost}")
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("Failed to find a feasible solution")