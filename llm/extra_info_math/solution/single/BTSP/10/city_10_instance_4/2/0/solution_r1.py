from pulp import *
import math

# Coordinates of each city including the depot city
coordinates = [
    (79, 15),  # depot city 0
    (79, 55),  # city 1
    (4, 80),   # city 2
    (65, 26),  # city 3
    (92, 9),   # city 4
    (83, 61),  # city 5
    (22, 21),  # city 6
    (97, 70),  # city 7
    (20, 99),  # city 8
    (66, 62)   # city 9
]

n = len(coordinates)

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Model initialization
model = LpProblem('TSP', LpMinimize)

# Decision variables
x = LpVariable.dicts('x', [(i, j) for i in range(n) for j in range(n)], cat='Binary')
u = LpVariable.dicts('u', [i for i in range(n)], lowBound=0, upBound=n-1, cat='Continuous')

# Objective function
model += lpSum(x[i, j] * distances[i][j] for i in range(n) for j in range(n))

# Subject to constraints
for i in range(n):
    model += lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += lpSum(x[j, i] for j in range(n) if i != j) == 1

# Eliminate subtours
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n*x[i, j] <= n-1

# Solve the problem
model.solve(PULP_CBC_CMD(msg=False))

# Output the results
tour = []
current_city = 0
while True:
    next_cities = [j for j in range(n) if value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if next_city == 0:
        break

tour.insert(0, 0)  # Start at the depot

# Calculate max distance and total travel cost
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
total_distance = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance}")