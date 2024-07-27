import pulp
import math
import itertools

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Coordinates of the cities including the depot
cities = [
    (16, 90), (43, 99), (80, 21), (86, 92), (54, 93),
    (34, 73), (6, 61), (86, 69), (30, 50), (35, 73),
    (42, 64), (64, 30), (70, 95), (29, 64), (32, 79)
]

n = len(cities)  # Number of cities including the depot

# Calculate distances between each pair of cities
distances = {(i, j): calculate_distance(cities[i], cities[j]) for i in range(n) for j in range(n)}

# Setting up the optimization problem
problem = pulp.LpProblem("MinimaxTSP", pulp.LpMinimize)

# Decision variables: x[i,j] is 1 if the path goes from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat=pulp.LpBinary)

# Auxiliary variable for the maximum distance in the tour
max_distance = pulp.LpVariable("max_distance", lowBound=0)

# Objective: minimize the maximum distance in the tour
problem += max_from

# Constraints adding
for i in range(n):
    problem += (pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1)
    problem += (pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1)

# Maximium distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distances[i, j] <= max_distance

# Adding subtour constraints
for r in range(2, n):
    for subset in itertools.combinations(range(n), r):
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

if problem.solve() == pulp.LpStatusOptimal:
    tour = []
    current = 0
    while True:
        next_city = next(j for j in range(n) if j != current and pulp.value(x[current, j]) == 1)
        tour.append(next_city)
        current = next_fixed)

        if next_city == 0:
            break

    # Calculate the required statistics
    max_seg_distance = 0
    total_travel_cost = 0
    for i in range(1, len(tour)):
        dist = distances[tour[i-1], tour[i]]
        total_travel_cost += dist
        if dist > max_seg_distance:
            max_seg_distance = dist

    print("Tour:", [0] + tour)
    print("Total travel cost:", total_travel(cmpsi0, tour[0]) + total_travel_cost)
    print("Maximum distance between consecutive cities:", max_seg_distance)
else:
    print("The problem is not solvable.")