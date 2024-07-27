import math
from pulp import *

# City locations
city_locations = [(30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
                  (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
                  (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)]

# Number of cities
n = len(city_locations)

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0])**2 + (loc1[1] - loc2[1])**2)

# Cost matrix
costs = [[euclidean_distance(city_locations[i], city_locations[j]) for j in range(n)] for i in range(n)]

# Define the problem
prob = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i,j) for i in range(n) for j in range(n)], cat='Binary')

# Objective function
prob += lpSum(costs[i][j] * x[(i,j)] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += lpSum(x[(i,j)] for j in range(n) if i != j) == 1  # leave each city only once
    prob += lpSum(x[(j,i)] for j in range(n) if i != j) == 1  # enter each city only once

# Subtour elimination constraints (implementing a naive version)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += x[(i, j)] + x[(j, i)] <= 1

# Solve the problem using the default solver
prob.solve()

# Output the solution
tour = []
for i in range(n):
    for j in range(n):
        if x[(i, j)].value() == 1:
            tour.append((i,j))

# Display the tour
organized_tour = [0]
for _ in range(n-1):
    for i in range(n):
        if tour[i][0] == organized_tour[-1]:
            organized_tour.append(tour[i][1])
            break

# Add the return to the depot
organized_tour.append(0)

# Calculate the travel cost
travel_cost = sum(costs[organized_tour[i]][organized_tour[i+1]] for i in range(len(organized_tour)-1))

# Print the results
print("Tour:", organized_tour)
print("Total travel cost:", round(travel_cost, 2))