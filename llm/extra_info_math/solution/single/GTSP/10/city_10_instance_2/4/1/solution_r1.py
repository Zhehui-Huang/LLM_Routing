import math
import pulp

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
cities = {
    0: (90, 3),  # Depot city
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

# City groups
groups = [
    [3, 6], [5, 8], [4, 9], [1, 7], [2]
]

# Problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Objective
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}
prob += pulp.lpSum(x[i, j] * distances[i, j] for i in cities for j in cities if i != j)

# Constraints
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

for i in cities:
    prob += (pulp.lpSum(x[j, i] for j in cities if (j, i) in x) ==
             pulp.lpSum(x[i, j] for j in cities if (i, j) in x))

# Solve
prob.solve()

# Output the solution
tour = [0]  # start at depot
current = 0
visited = set()
visited.add(current)

while True:
    next_city = [j for j in cities if j != current and pulp.value(x[current, j]) == 1]
    if not next_city or next_city[0] in visited:
        break
    next_city = next_city[0]
    visited.add(next_city)
    tour.append(next_city)
    current = next_city

tour.append(0)  # end at depot
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Print results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")