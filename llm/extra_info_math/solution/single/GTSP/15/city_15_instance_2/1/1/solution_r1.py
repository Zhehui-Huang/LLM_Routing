import math
from pulp import LpProblem, LpVariable, LpMinimize, LpBinary, lpSum, LpStatus

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Cities and groups
cities_coordinates = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]
city_groups = [[8, 12, 14], [7, 10, 11], [4, 6, 9], [1, 3, 13], [2, 5]]
city_ids = list(range(len(cities_coordinates)))

# Problem
problem = LpProblem("RobotRouting", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j) for i in city_ids for j in city_id if i != j], cat=LpBinary)
u = LpVariable.dicts("u", city_ids[1:], lowBound=0, cat='Continuous')  # for subtour elimination, no u_0

# Objective
problem += lpSum(x[(i, j)] * euclidean_distance(cities_coordinates[i], cities_coordinates[j]) for i in city_ids for j in city_ids if i != j)

# Each group must be entered and exited exactly once
for group in city_groups:
    problem += lpSum(x[(i, j)] for i in group for j in city_ids if j not in group) == 1
    problem += lpSum(x[(j, i)] for i in group for j in city_ids if j not in group) == 1

# Flow conservation for each city (except depot)
for j in city_ids[1:]:
    problem += lpSum(x[(i, j)] for i in city_ids if i != j) - lpSum(x[(j, k)] for k in city_ids if j != k) == 0

# Subtour elimination
num_groups = len(city_groups)
for i in city_ids[1:]:
    for j in city_ids[1:]:
        if i != j:
            problem += u[i] - u[j] + len(city_ids) * x[(i, j)] <= len(city_ids) - 1

# Solve the problem
problem.solve()

# Output the results
tour = []
total_cost = 0
if LpStatus[problem.status] == 'Optimal':
    for i in city_ids:
        for j in city_ids:
            if i != j and x[(i, j)].varValue == 1:
                tour.append((i, j))
                total_cost += euclidean_distance(cities_coordinates[i], cities_coordinates[j])

# Reconstruct the tour from the decision variables
city_visited = 0
ordered_tour = [0]  # Start at depot
for _ in range(len(city_ids)-1):
    for k in city_ids:
        if k != city_visited and (city_visited, k) in x and x[(city_visited, k)].varValue == 1:
            ordered_tour.append(k)
            city_visited = k
            break

# Since it's a cycle, return to the start
ordered_tour.append(0)

# Output
print("Tour:", ordered_tour)
print("Total travel cost:", total_cost)