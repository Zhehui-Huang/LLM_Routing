import pulp
import math

# Updated the city list
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), (88, 59), 
    (79, 77), (63, 23), (19, 76), (21, 38), (19, 65), (11, 40), 
    (3, 21), (60, 55), (4, 39)
]

# Function to calculate Euclidean distance between two cities (adjusted for indexing from 0)
def distance(city1, city2):
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Number of cities includes the depot
n = len(cities)

# Create the distance matrix
cost = {(i, j): distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Define the problem using PuLP
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if the route includes travel from city i to city j directly
x = pulp.LpVariable.dicts('x', cost.keys(), cat=pulp.LpBinary)

# Objective Function: Minimize the sum of travel distances
model += pulp.lpSum([x[(i, j)] * cost[(i, j)] for (i, j) in cost.keys()]), "Total Travel Cost"

# Constraints
# 1. Ensure each city is left exactly once
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if (i, j) in x) == 1

# 2. Ensure each city is entered exactly once
for j in range(n):
    model += pulp.lpOpp(x[(i, j)] for i in range(n) if (i, j) in x) == 1

# Subtour prevention constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += x[(i, j)] * (n-1) <= n-2

# Solve the model
status = model.solve()

# Check if the solution is optimal
if status == pulp.LpStatusOptimal:
    print("Solution found!")
    tour = [0]  # start at the depot
    current_city = 0
    visited = set([0])
    
    while len(visited) < n:
        next_cities = [j for j in range(n) if (current_city, j) in x and pulp.value(x[(current_city, j)]) == 1]
        if next_cities:
            next_city = next_cities[0]
            tour.append(next_city)
            visited.add(next_city)
            current_city = next_city
    
    tour.append(0)  # return to the depot
    print("Tour:", tour)
    total_cost = sum(cost[(tour[i], tour[i+1])] for i in range(len(tour)-1))
    print("Total travel cost:", total_cost)
else:
subseteq condition should be covered correctly by implementing a solution with correct subtour elimination logic. This is crucial if the provided constraints did not fully eliminate them.