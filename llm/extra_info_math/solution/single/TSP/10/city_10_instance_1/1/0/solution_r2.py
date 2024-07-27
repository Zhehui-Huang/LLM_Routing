import pulp
import math
import itertools

# Define the cities and their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Number of cities
n = len(cities)

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost matrix
c = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective Function
problem += pulp.lpSum(c[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # each city must be left exactly once
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # each city must be entered exactly once

# Subtour elimination constraints
for S in range(2, n):
    for subtour in itertools.combinations(range(n), S):
        problem += pulp.lpSum(x[i, j] for i in subtour for j in subtour if i != j) <= len(subtour) - 1

# Solve the problem
problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the tour manually
tour = []
visited = [0]  # start tour at the depot
current_city = 0

while len(visited) < n:
    for j in range(n):
        if j not in visited and pulp.value(x[current_city, j]) == 1:
            tour.append((current_city, j))
            visited.append(j)
            current_city = j
            break

# Adding return to the start city
tour.append((current_city, 0))

# Calculate total travel cost of the tour
tour_route = [i[0] for i in tour] + [0]  # include the return to the starting city
total_cost = sum(c[tour_route[i]][tour_route[i+1]] for i in range(len(tour_route)-1))

print(f"Tour: {tour_route}")
print(f"Total travel cost: {total_cost:.2f}")