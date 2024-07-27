import numpy as np
import pulp

# Define the city coordinates and groups
city_coordinates = [(3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56),
                    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53),
                    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94),
                    (51, 58), (30, 48)]
groups = [[7, 10, 11, 12], [3, 8, 13, 16], [2, 4, 15, 18], [1, 9, 14, 19], [5, 6, 17]]

def euclidean_distance(i, j):
    xi, yi = city_coordinates[i]
    xj, yj = city_coordinates[j]
    return np.sqrt((xi - xj)**2 + (yi - yj)**2)

V = [0] + [city for group in groups for city in group]
n = len(city_coordinates)
k = len(groups) 

problem = pulp.LpProblem("Minimal_Tour_Cost", pulp.LpMinimize)

x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective Function
problem += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j), "Total travel cost"

# Constraints
for group in groups:
    problem += pulp.lpSum(x[(i, j)] for i in group for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[(j, i)] for i in group for j in range(n) if j != i) == 1

for i in range(n):
    problem += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) - pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 0

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + k * x[(i, j)] <= (k - 1)

problem.solve()

# Retrieving the results
tour = [0]
current = 0
for _ in range(n - 1):
    next_city = [j for j in range(n) if j != current and pulp.value(x[(current, j)]) == 1]
    if not next_city:
        break
    next_city = next_city[0]
    tour.append(next_city)
    current = next_city

tour.append(0)  # Return to the depot
total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")