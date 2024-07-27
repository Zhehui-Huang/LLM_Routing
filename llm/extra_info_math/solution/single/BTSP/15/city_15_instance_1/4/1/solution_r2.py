import math
from pulp import *

# Coordinates of the 15 cities including the depot city 0
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# Number of cities (including the depot)
n = len(coordinates)

# Create the problem variable to contain the problem data
problem = LpProblem("MinimizeMaxDistanceTSP", LpMinimize)

# Decision variables: x[i, j] is 1 if the path goes from city i to city j
x = LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')

# Variable to minimize: maximum distance between any two consecutive cities
max_distance = LpVariable("max_distance")

# Objective function
problem += max_distance

# Constraints for entering and leaving each city
for i in range(n):
    problem += lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    problem += lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Subtour elimination
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[(i, j)] * distance(i, j) <= max_dm

# Subtour elimination constraints using Miller, Tucker, Zemlin formulation
u = LpVariable.dicts("u", list(range(n)), lowBound=0, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[(i, j)] <= n - 1

# Solve the problem
problem.solve(PULP_CBC_CMD(msg=0))

# Extract the tour solving the subtour and collecting the tour order
tour = []
current_city = 0
tour.append(current_city)

for _ in range(n-1):
    next_cities = [j for j in range(n) if j != current_city and value(x[(current_city, j)]) == 1]
    if next_cities:
        next_city = next_cities[0]
        tour.append(next_city)
        current_city = next_city

# Complete the cycle
tour.append(0)

# Calculate the output values 
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
max_segment_distance = max(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output the result
print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))
print("Maximum distance between consecutive cities:", round(max_segment_distance, 2))