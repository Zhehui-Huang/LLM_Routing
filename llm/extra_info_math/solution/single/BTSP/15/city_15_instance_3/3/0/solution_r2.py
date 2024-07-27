import pulp
import math

# Coordinates of the cities
cities = {
    0: (16, 90),
    1: (43, 99),
    2: (80, 21),
    3: (86, 92),
    4: (54, 93),
    5: (34, 73),
    6: (6, 61),
    7: (86, 69),
    8: (30, 50),
    9: (35, 73),
    10: (42, 64),
    11: (64, 30),
    12: (70, 95),
    13: (29, 64),
    14: (32, 79)
}

# Calculate Euclidean distance between any two cities
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

n = len(cities)

# Creating the problem
prob = pulp.LpProblem("Minimax TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat="Binary")
max_edge = pulp.LpVariable("max_edge", lowBound=0, cat="Continuous")

# Objective Function
prob += max_edge 

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave i
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter i

# Distance constraint for max_edge minimization
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[i, j] * distance(i, j) <= max_edge

# Subtour Elimination
for i in range(2, n+1):
    for subset in itertools.combinations(range(1, n), i):
        prob += pulp.lpSum(x[i, j] + x[j, i] for i, j in itertools.permutations(subset, 2)) <= len(subset) - 1

# Solve the Problem
prob.solve()

# Collect the tour from the results
tour = []
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))

# Order the tour starting from the depot
result_tour = [0]
current = 0
while len(result_tour) < n:
    for (i, j) in tour:
        if i == current:
            result_tour.append(j)
            current = j
            break

# Close the tour with returning to the depot
result_tour.append(0)

# Calculate the total and maximum distance
max_distance = 0
total_cost = 0
for idx in range(1, len(result_tour)):
    dist = distance(result_tour[idx - 1], result_tour[idx])
    total_cost += dist
    if dist > max_distance:
        max_distance = dist

# Print the output required
tour_output = "Tour: {}".format(result_tour)
cost_output = "Total travel cost: {:.2f}".format(total_cost)
max_dist_output = "Maximum distance between consecutive cities: {:.2f}".format(max_distance)

print(tour_output)
print(cost_output)
print(max_dist_output)