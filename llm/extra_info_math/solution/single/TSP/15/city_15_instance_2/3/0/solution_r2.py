from math import sqrt
from pulp import *

# Define cities and their coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Total number of cities
n = len(cities)

# Distance cost matrix
costs = {(i, j): distance(i, j) for i in range(n) for j in range(n) if i != j}

# Create the LP problem
prob = LpProblem("TSP", LpMinimize)

# Creating a dictionary of PuLP variables with keys from cost dictionary
x = LpVariable.dicts("x", costs, 0, 1, LpBinary)

# Objective function
prob += lpSum(x[(i, j)] * costs[(i, j)] for (i, j) in costs)

# Constraints
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if (i, j) in x) == 1  # Leave each city only once
    prob += lpSum(x[(j, i)] for j in range(n) if (j, i) in x) == 1  # Arrive at each city only once

# Solve the problem
prob.solve()

# Extract the optimal tour
tour = [0]
current_city = 0
distance_travelled = 0
while True:
    next_cities = [(j, x[(current_city, j)].varValue) for j in range(n) if (current_city, j) in x and x[(current_city, j)].value() == 1]
    if not next_cities:
        break
    next_city = next_cities[0][0]
    tour.append(next_city)
    distance_travelled += costs[(current_city, next_city)]
    current_city = next_city
    if current_city == 0:
        break

tour.append(0) # Return to depot
distance_travelled += costs[(tour[-2], 0)]

# Output results
if LpStatus[prob.status] == 'Optimal':
    print('Tour:', tour)
    print('Total travel cost:', round(distance_travelled, 2))
else:
    print('Failed to find an optimal solution.')