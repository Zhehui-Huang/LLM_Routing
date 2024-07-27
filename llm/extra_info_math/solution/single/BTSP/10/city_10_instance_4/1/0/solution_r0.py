import pulp
import math
from itertools import combinations

# Coordinates for depot and cities
coordinates = [
    (79, 15),  # Depot city 0
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

# Distance matrix calculation
n = len(coordinates)  # Number of cities including depot
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
t = pulp.LpVariable.dicts("t", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Integer')

z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Objective Function: Minimize the maximum distance traveled between consecutive cities
problem += z, "Minimize_the_maximum_distance"

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Sum_of_x_{i}_out"
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Sum_of_x_{i}_in"

# Limit maximum distance between consecutive cities
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distance_matrix[i][j] <= z, f"Max_dist_{i}_{j}"

# Subtour Elimination
for s in range(2, n):
    for S in combinations(range(1, n), s):  # Exclude depot (0) in subtour elimination constraints
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Output results
tour = []
current_city = 0
total_cost = 0
max_distance = 0

while True:
    next_city = [j for j in range(n) if pulp.value(x[current_city, j]) == 1][0]
    tour.append(next_city)
    total_cost += distance_matrix[current_city][next_city]
    max_distance = max(max_distance, distance_matrix[current_city][next_city])
    current_city = next_city
    if current_city == 0:
        break

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)