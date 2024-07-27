import pulp
import math

# Define the coordinates of the cities
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 47),
    14: (6, 99)
}
n = len(cities)

# Calculate distances between all pairs using Euclidean formula
def dist(i, j):
    return math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)

# Creating the problem variable to contain the problem data
model = pulp.LpProblem("Minimize_Maximum_Distance_in_TSP", pulp.LpMinimize)

# Creating a dictionary called 'x' for decision variable indicating if i to j is part of tour
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Continuous variable for the maximum distance
max_dist = pulp.LpVariable("max_dist", lowBound=0, cat='Continuous')

# Objective function: Minimize the maximum distance
model += max_dist

# Constraint: enter and leave each city exactly once
for k in cities:
    model += pulp.lpSum(x[i, k] for i in cities if i != k) == 1
    model += pulp.lpSum(x[k, j] for j in cities if k != j) == 1

# Constraint: subtour elimination
for s in range(2, n):
    for S in combinations(cities, s):
        model += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Constraint: max_dist is at least as large as each distance in tour
for i in cities:
    for j in cities:
        if i != j:
            model += max_dist >= dist(i, j) * x[i, j]

# Solve the problem
status = model.solve(pulp.PULP_CBC_CMD(msg=0))

# Fetching the solution
tour = [0]
current_city = 0
while True:
    next_cities = [j for j in cities if j != current_city and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_value)
    current_city = next_city
    if current_city == 0:
        break

# Calculate tour cost details
total_cost = sum(dist(tour[i], tour[i+1]) for i in range(len(tour)-1))
max_distance = max(dist(tour[i], tour[i+1]) for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")