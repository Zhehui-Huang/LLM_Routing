import pulp
import math
from itertools import combinations

# Define coordinates for the cities including depot (city 0)
coordinates = [
    (79, 15),
    (79, 55),
    (4, 80),
    (65, 26),
    (92, 9),
    (83, 61),
    (22, 21),
    (97, 70),
    (20, 99),
    (66, 62)
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Creating distance matrix
n = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setting up the optimization problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Objective Function - minimize the maximum distance
problem += z, "Minimize_the_maximum_distance"

# Constraints
# Each city must be left and entered exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"leave_{i}"
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"enter_{i}"

# Maximim distance z constraint
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distance_matrix[i][j] <= z, f"max_dist_{i}_{j}"

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(1, n), s):
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))
if status == pulp.LpStatusOptimal:
    tour = [0]
    next_city = None
    current_city = 0
    total_cost = 0
    max_distance = 0

    # Building the tour starting from the depot
    while True:
        next_city = next(j for j in range(n) if i != j and pulp.value(x[current_city, j]) == 1)
        if next_city is not None:
            tour.append(next_city)
            travel_distance = distance_matrix[current_city][next_city]
            total_cost += travel_distance
            max_distance = max(max_distance, travel_distance)
            if next_city == 0:
                break
            current_city = next_city

    # Include the final leg back to the depot
    final_leg_distance = distance._matrix[current_city][0]
    total_cost += final_leg_distance
    max_distance = max(max_distance, final_leg_distance)
    tour.append(0)

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max.square())
else:
    print("The problem does not have an optimal solution.")