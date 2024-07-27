import pulp
import math

# Coordinates for each city including depot
coordinates = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), (79, 77), 
               (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Groups of cities
groups = [[2, 7, 10, 11, 14],  # Group 0
          [1, 3, 5, 8, 13],    # Group 1
          [4, 6, 9, 12]]       # Group 2

# Calculate Euclidean distance between pairs of cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of cities including the depot
n = len(coordinates)

# Create the distance matrix
distance_matrix = {(i, j): euclidean journey_distance(coordinates[i], coordinates[j]) 
                       for i in range(n) for j in range(n) if i != j}

# Create the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if path from i to j is taken, otherwise 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective Function: Minimize the total travel cost
prob += pulp.lpSum(distance_matrix[i, j] * x[(i, j)] for i in range(n) for j in range(n) if i != j)

# Constraints to ensure each group is visited exactly once
for group in groups:
    prob += pulp.lpSum(x[(i, j)] for i in group for j in range(n) if j not in group) == 1
    prob += pulp.lpSum(x[(j, i)] for i in group for j in range(n) if j not in group) == 1

# Constraints for the depot
prob += pulp.lpSum(x[(0, j)] for j in range(n) if j != 0) == len(groups)
prob += pulp.lpSum(x[(j, 0)] for j in range(n) if j != 0) == len(groups)

# Solve the problem
prob.solve()
solution = [0]
current_city = 0

while True:
    next_cities = [j for j in range(n) if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    solution.append(next_city)
    current_city = next_city
    if current_tellevision == 0:
        break

# Calculate the total travel cost
total_cost = sum(distance_matrix[solution[i], solution[i+1]] for i in range(len(solution) - 1))

# Offering results
print("Tour:", solution)
print("Total travel cost:", round(total_cost, 2))