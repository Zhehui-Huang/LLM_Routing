import pulp
import math

# Coordinates for the cities (Depot + Cities)
coordinates = [(84, 67), (74, 40), (71, 13), (74, 82), (97, 28), (0, 31), (8, 62), (74, 56), (85, 71), (6, 76)]

# Number of cities (including depot)
n = len(coordinates)

# Euclidean distance calculator
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Creating a distance matrix
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = distance(coordinates[i], coordinates[j])
        else:
            distances[(i, j)] = 0

# Integer linear programming model
model = pulp.LpProblem("TSP_MinMax", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pulp.LpVariable("longest_leg", lowBound=0, cat='Continuous')

# Objective function: minimize the longest leg of the tour
model += z

# Constraints
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # leave each city once
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # enter each city once

# Longest leg constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += x[(i, j)] * distances[(i, j)] <= z

# Subtour elimination
for s in range(2, n):
    for subtour in itertools.combinations(range(1, n), s):
        model += pulp.lpSum(x[(i, j)] for i in subtour for j in subtour if i != j) <= len(subtour) - 1

# Solving the problem
model.solve()

# Collecting the results
if pulp.LpStatus[model.status] == 'Optimal':
    print("Found an optimal solution.")
    tour = []
    current_city = 0
    tour.append(current_city)
    
    while True:
        next_city = [j for j in range(n) if j != current_city and pulp.value(x[(current_city, j)]) == 1][0]
        tour.append(next_city)
        current_city = next_city
        if current_city == 0:
            break
            
    total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    max_distance = max(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))
    
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)

else:
    print("Failed to find an optimal solution.")