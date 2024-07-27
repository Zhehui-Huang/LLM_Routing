from pulp import *
import math

# City coordinates
coordinates = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84), 6: (4, 56), 7: (54, 82),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9), 8: (37, 28), 9: (27, 45)
}

# Compute distances
def distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

all_cities = list(coordinates.keys())
dist = {(i, j): distance(i, j) for i in all_cities for j in all_cities if i != j}

# Define the problem
prob = LpProblem("VRP_Shortest_Path", LpMinimize)

# Variables: x_ij = 1 if travel from city i to city j
x = LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), cat='Binary')
u = LpVariable.dicts("u", all_cities, lowBound=0, cat='Continuous')

# Objective
prob += lpSum(dist[i, j] * x[i, j] for i in all_cities for j in all_cities if i != j)

# Constraints
# Exactly one edge out of reach each non-depot node
for k in all_cities:
    prob += lpSum(x[k, j] for j in all_cities if (k, j) in x) == 1  # Leaving each city
    prob += lpSum(x[i, k] for i in all_cities if (i, k) in x) == 1  # Entering each city

# Subtour elimination constraints
N = 20  # Number of all cities including the depot
for i in all_cities:
    for j in all_cities:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + (N * x[i, j]) <= N - 1

# Solve the problem
prob.solve()

# Retrieve results
tour = []
current = 0
visited_cities = set([0])
n = len(coordinates)
total_distance = 0

while len(visited_cities) < n:
    for j in all_cities:
        if x[current, j].value() == 1 and j not in visited_cities:
            tour.append(j)
            total_distance += dist[current, j]
            visited_cities.add(j)
            current = j
            break

tour.append(0)  # returning to the depot
total_distance += dist[current, 0]

print("Tour:", tour)
print("Total travel cost:", total_distance)