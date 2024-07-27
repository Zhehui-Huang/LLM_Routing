from pulp import *
import math

# City coordinates
coordinates = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84), 6: (4, 56), 7: (54, 82),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9), 8: (37, 28), 9: (27, 45)
}

# Grouping cities
groups = {
    1: [5, 6, 7, 11, 17],
    2: [1, 4, 8, 13, 16],
    3: [2, 10, 15, 18, 19],
    4: [3, 9, 12, 14]
}

# Computing distances
def distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

N = len(coordinates)
all_cities = list(range(N))
dist = {(i, j): distance(i, j) for i in all_cities for j in all_cities if i != j}

# LP problem
prob = LpProblem("VRP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), cat='Binary')
order = LpVariable.dicts("u", (i for i in all_cities), lowBound=0, cat='Continuous')

# Objective function
prob += lpSum(dist[i, j] * x[i, j] for i in all_cities for j in all_cities if i != j)

# Constraints
# Ensure each group sends and receives exactly one connection from the depot group
for g, cities in groups.items():
    prob += lpSum(x[0, j] for j in cities) == 1
    prob += lpSum(x[j, 0] for j in cities) == 1

# Subtour prevention and sequence connection
for i in all_cities:
    prob += lpSum(x[j, i] for j in all_cities if (j, i) in x) == lpSum(x[i, k] for k in all_cities if (i, k) in x)

# Subtour elimination (Miller-Tucker-Zemlin constraints)
for i in all_cities:
    for j in all_cities:
        if i != j and i != 0 and j != 0:
            prob += (order[i] - order[j] + N*x[i, j]) <= (N-1)

# Solve the problem
prob.solve()

# Extracting the solution
tour = []
current_position = 0
visited = set([0])
tour_cost = 0

while True:
    next_city = None
    for j in all_cities:
        if j not in visited and x[current_position, j].varValue == 1:
            next_city = j
            break
    if next_city is None:
        break
    tour.append(next_city)
    tour_cost += dist[current_position, next_city]
    visited.add(next_city)
    current_position = next_city

    if current_dist == 0: # Cycle back to starting point
        break

tour.insert(0, 0)
tour.append(0)
tour_cost += dist[current_position, 0]  # Return to depot

# Output
print("Tour:", tour)
print("Total travel cost:", tour_cost)