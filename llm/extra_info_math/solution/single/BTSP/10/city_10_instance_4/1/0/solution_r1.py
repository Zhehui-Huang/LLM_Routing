import pulp
import math
from itertools import combinations

# Defining the city coordinates
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

# Function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create the distance matrix
n = len(coordinates)
distance_matrix = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Set up the optimization problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Objective: Minimize the maximum distance between any two consecutive cities
problem += z, "Minimize_the_maximum_distance"

# Constraints on entering and leaving each city
for i in range(n):
    problem += sum(x[i, j] for j in range(n) if i != j) == 1, f"leave_{i}"
    problem += sum(x[j, i] for j in range(n) if i != j) == 1, f"enter_{i}"

# Constraint for sub-tour elimination and max distance
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distance_matrix[i][j] <= z, f"distance_{i}_{j}"

# Eliminating sub-tours
for size in range(2, n):
    for S in combinations(range(1, n), size):
        problem += sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract tour from decision variables
tour = [0]
current_city = 0
max_distance_in_tour = 0
while True:
    next_city = [j for j in range(n) if i != j and pulp.value(x[current_city, j]) == 1][0]
    distance_traveled = distance_matrix[current_city][next_city]
    max_distance_in_tour = max(max_distance_in_tour, distance_traveled)
    current_city = next_city
    tour.append(next_city)
    if next_city == 0:
        break

# Calculate total travel cost
total_distance_traveled = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_distance_traveled)
print("Maximum distance between consecutive cities:", max_distance_in_tour)