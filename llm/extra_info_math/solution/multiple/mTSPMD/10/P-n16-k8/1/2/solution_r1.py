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

# LP problem
prob = LpProblem("VRP_with_Multiple_Depots_and_Robots", LpMinimize)

# Variables
x = LpVariable.dicts("x",
                    ((i, j, k) for k in robots for i in range(n) for j in range(n)),
                    cat='Binary')

# Objective
prob += lpSum(x[(i, j, k)] * distance_matrix[i][j] for k in robots for i in range(n) for j in range(n))

# Constraints
# Departing and returning once per robot
for k in robots:
    prob += lpSum(x[(k, j, k)] for j in range(n) if j != k) == 1
    prob += lpSum(x[(j, k, k)] for j in range(n) if j != k) == 1

# Every city visited exactly once
for j in range(n):
    if j not in depots:
        prob += lpSum(x[(i, j, k)] for k in robots for i in range(n)) == 1
    
# Subtour prevention using Miller-Tucker-Zemlin formulation
u = LpVariable.dicts("u", (i for i in range(n)), lowBound=0, cat='Continuous')
for k in robots:
    for i in range(n):
        for j in range(n):
            if i != j and i != k and j != k:
                prob += u[i] - u[j] + (n) * x[(i, j, k)] <= n - 1

# Solving the problem
prob.solve()

# Checking and printing the solutions
print("Status:", LpStatus[prob.status])
total_cost = 0
for k in robots:
    print(f"Robot {k} Tour: ", end="")
    tour = [k]
    for i in range(n):
        next_city = [j for j in range(n) if value(x[(tour[-1], j, k)]) == 1]
        if next_city:
            tour.extend(next_city)
            if next_city[0] == k:
                break

    print(tour)
    # Calculate the cost of the tour
    tour_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    total_cost += tour_cost
    print(f"Robot {k} Total Travel Cost: {tour *)&ast;k}")  # ➔ print cost for each robot tour

print("Overall Total Travel Cost:", total_cost)  # ➔ print total cost