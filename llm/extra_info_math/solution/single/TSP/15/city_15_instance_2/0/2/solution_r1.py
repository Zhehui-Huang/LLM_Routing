import pulp
import math
import itertools

# Define city coordinates
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
    13: (72, 43),
    14: (6, 99)
}

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Create LP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Objective function
model += pulp.lpSum([distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j and i != j]), "Total_Cost"

# Each city must be left exactly once and entered exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"leave_{i}"
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"enter_{i}"

# Subtour elimination via additional constraints
from itertools import combinations
for s in range(2, n):
    for subset in combinations(range(1, n), s):  # Don't consider subsets including the depot (city 0)
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve()

# Check if the problem is solved and extract the solution
if model.status == 1:
    # Extract the solution to create a tour
    tour = []
    current_city = 0
    tour.append(current_city)
    
    # Construct path
    while len(tour) < n:
        for j in range(n):
            if j != current_city and pulp.value(x[current_city, j]) == 1:
                tour.append(j)
                current_city = j
                break
                
    tour.append(0)  # Return to depot
    
    # Calculate total travel cost
    total_cost = sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
    
    # Output results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("An optimal solution was not found.")