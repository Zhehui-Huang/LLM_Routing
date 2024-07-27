import math
import pulp

# Euclidean distance calculator
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cities coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 
    4: (68, 98), 5: (45, 84), 6: (4, 56), 7: (54, 82), 
    8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76), 
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 
    16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

n = len(cities)  # Number of cities including the depot

# Precompute distances
costs = [[calculate_distance(cities[i], cities[j]) for j in cities] for i in cities]

# Setting up the problem: Minimize total distance
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j]: 1 if the tour goes from city i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective function: minimize the sum of travel costs
prob += pulp.lpSum(costs[i][j] * x[i, j] for i in cities for j in cities if i != j)

# Constraints
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if i != j) == 1  # leave each city only once
    prob += pulp.lpSum(x[j, i] for j in cities if i != j) == 1  # enter each city only once

# Subtour elimination constraints (SEC)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += x[i, j] + x[j, i] <= 1

# Solve the problem
prob.solve()

# Finding the tour from the solution
tour = [0]
current_city = 0
while True:
    next_cities = [j for j in cities if current_city != j and pulp.value(x[current_city, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Calculate the total travel cost
total_cost = sum(costs[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)