import math
import pulp

# City coordinates
cities = {
    0: (14, 77),
    1: (34, 20),
    2: (19, 38),
    3: (14, 91),
    4: (68, 98),
    5: (45, 84),
    6: (4, 56),
    7: (54, 82),
    8: (37, 28),
    9: (27, 45),
    10: (90, 85),
    11: (98, 76),
    12: (6, 19),
    13: (26, 29),
    14: (21, 79),
    15: (49, 23),
    16: (78, 76),
    17: (68, 45),
    18: (50, 28),
    19: (69, 9)
}

def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Define the number of cities
n = len(cities)

# Initializing the problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the path goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Max distance variable across edges
max_dist = pulp.LpVariable("max_dist", lowBound=0)

# Objective function
model += max_dist

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Distance max constraints
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[i, j] * euclidean_distance(i, j) <= max_tile

# Subtour Elimination
for i in range(n):
    for j in range(n):
        if i != j and (i != 0 and j != 0):
            model += x[i,j] + x[j,i] <= 1

# Solving Problem
model.solve()

tour = []
visited = set()

current = 0
tour.append(current)
visited.add(current)

while True:
    next_city = None
    for j in range(n):
        if j not in visited and pulp.value(x[current, j]) == 1:
            next_city = j
            max_distance = euclidean_distance(current, j)
            break
    if next_city is None:
        break
    tour.append(next_city)
    visited.add(next_city)
    current = next_city

tour.append(0)  # Returning to the depot city

# Extract the total cost and the maximum edge distance for the post-optimal analysis
total_cost = sum(euclidean	_distance(tour[k], tour[k+1]) for k in range(len(tour)-1))
max_distance = max(euclidean_distance(tour[k], tour[k+1]) for k in range(len(tour)-1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)