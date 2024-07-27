import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpInteger, value

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# Calculate distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Distances matrix
distances = { (i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j }

# Problem
prob = LpProblem("Minimax_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", distances, 0, 1, LpInteger)
M = LpVariable("M", 0)

# Objective
prob += M, "Maximize_Minimum_Distance"

# Constraints
for i in cities:
    prob += lpSum(x[(i, j)] for j in cities if i != j) == 1, f"From_city_{i}"
    prob += lpSum(x[(j, i)] for j in cities if i != j) == 1, f"To_city_{i}"

# Subtour prevention (MTZ constraints)
n = len(cities)
u = LpVariable.dicts("u", cities, 0, n-1, LpInteger)
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + n*x[(i, j)] <= n-1
            
# Longest edge constraint
for i, j in distances:
    prob += x[(i, j)] * distances[(i, j)] <= M
    
# Solve problem
prob.solve()

# Output variables
tour = []
visited = set()

current = 0
while True:
    for j in cities:
        if j != current and value(x[(current, j)]) == 1:
            tour.append(current)
            current = j
            break
    if current == 0:
        tour.append(0)
        break

# Calculate total travel cost and max distance
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))
max_dist = max(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {value(M)}")