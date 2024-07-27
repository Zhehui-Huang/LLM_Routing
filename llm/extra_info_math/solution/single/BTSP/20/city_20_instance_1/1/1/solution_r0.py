import math
from pulp import LpProblem, lpSum, LpVariable, LpBinary, LpMinimize

# City coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76),
    17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Calculate Euclidean distance
def dist(city1, city2):
    (x1, y1), (x2, y2) = cities[city1], cities[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Number of cities including the depot
n = len(cities)

# Create problem
prob = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat=LpBinary)
d_max = LpVariable("d_max", lowBound=0, cat='Continuous')

# Objective
prob += d_max

# Constraints
for i in cities:
    if i == 0:
        prob += lpSum(x[i, j] for j in cities if j != i) == 2  # Start and end at depot
    else:
        prob += lpSum(x[i, j] for j in cities if j != i) == 1  # Each city is entered once
        prob += lpSum(x[j, i] for j in cities if j != i) == 1  # Each city is left once

# Subtour constraints
for S in range(3, n):
    for subtour in combinations(cities.keys() - {0}, S):
        prob += lpSum(x[i, j] for i in subtour for j in subtour if i != j) <= len(subtour) - 1

# Linking d_max with distances
for i in cities:
    for j in cities:
        if i != j:
            prob += x[i, j] * dist(i, j) <= d_max

# Solve the problem
prob.solve()

# Prepare output tour
tour = [0]
current_city = 0
while True:
    next_city = next(j for j in cities if j != current_city and x[current_city, j].varValue > 0.5)
    if next_city == 0:
        break
    tour.append(next_city)
    current_city = next_city
tour.append(0)  # Return to depot

# Total travel cost and maximum distance
total_cost = sum(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))
max_distance = max(dist(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)