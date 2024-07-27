import math
from pulp import LpProblem, LpVariable, lpSum, LpMinimize, LpBinary

# City coordinates
cities = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

def euclidean_distance(idx1, idx2):
    x1, y1 = cities[idx1]
    x2, y2 = cities[idx2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

n = len(cities)
distance = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Creating the problem
prob = LpProblem("TSP", LpMinimize)

# Variables: x_ij is 1 if the path from city i to j is taken otherwise 0
x = [[LpVariable(f'x_{i}_{j}', cat=LpBinary) for j in range(n)] for i in range(n)]
max_distance = LpVariable("max_distance", lowBound=0)

# Objective
prob += max_distance

# Constraints
for i in range(n):
    prob += lpSum(x[i][j] for j in range(n) if i != j) == 1, f"rowsum_{i}"
    prob += lpSum(x[j][i] for j in range(n) if i != j) == 1, f"colsum_{i}"

# Max distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i][j] * distance[i][j] <= max_distance

# Subtour Elimination
from itertools import combinations
for s in range(2, n):
    for S in combinations(range(n), s):
        prob += lpSum(x[i][j] for i in S for j in S if i != j) <= len(S) - 1, f"subtour_{S}"

# Solve the problem
prob.solve()

# Retrieve the order of cities visited
tour = []
for i in range(n):
    for j in range(n):
        if x[i][j].varValue == 1:
            tour.append((i, j))

# To find the tour from the binary variables, we need to trace the path starting from any city
def find_tour(tour, current_city, cities_covered):
    next_cities = [j for i, j in tour if i == current_city]
    if not next_cities:
        return cities_covered
    next_city = next_cities[0]
    return find_tour(tour, next_city, cities_covered + [next_city])


tour_order = find_tour(tour, 0, [0])
tour_distances = [distance[tour_order[i]][tour_order[i+1]] for i in range(len(tour_order)-1)]
max_tour_distance = max(tour_distances)
total_distance = sum(tour_distances)

print(f"Tour: {tour_order}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_tour_distance}")