from math import sqrt
from pulp import *

# Define cities and their coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Compute Euclidean distance between cities
def distance(city1, city2):
    return sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Distance cost matrix
n = len(cities)
costs = {(i, j): distance(i, j) for i in range(n) for j in range(n) if i != j}

# Define problem
prob = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
prob += lpSum(x[(i, j)] * costs[(i, j)] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # leave city i exactly once
    prob += lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # enter city i exactly once

# Subtour elimination constraints are not directly implemented here. Advanced techniques are required for larger instances.

# Solve the problem
prob.solve()

# Check if a valid solution was found
if LpStatus[prob.status] == 'Optimal':
    tours = []
    for i in range(n):
        for j in range(n):
            if i != j and x[(i, j)].varValue > 0.99:
                tours.append((i, j))

    # Extract the order of the tour
    current_location = 0
    tour = [0]
    tour_cost = 0
    while len(tour) < n:
        next_moves = [j for i, j in tours if i == current_location]
        next_location = next_moves[0]
        tour_cost += costs[(current_location, next_location)]
        current_location = next_destination = next_moves[0]
        tour.append(next_destination)
    tour.append(0)  # return to starting point
    tour_cost += costs[(current_location, 0)]

    # Output the tour and its total cost
    print(f"Tour: {tour}")
    print(f"Total travel cost: {tour_cost}")
else:
  print("No optimal solution found.")