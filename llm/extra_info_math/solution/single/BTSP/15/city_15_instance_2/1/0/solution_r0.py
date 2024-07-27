# You need to install PuLP in your environment
# pip install pulp

import math
import pulp

# Helper function to calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Define cities (index and (x, y) tuple)
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

n = len(cities)  # number of cities including the depot

# Calculate distances between all pairs of cities
dist = {(i, j): distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Create the ILP problem to minimize the maximum distance traveled between any two consecutive cities
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Variables representing whether to travel between city i to city j
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Variable representing the maximum distance between two consecutive cities in the tour
max_dist = pulp.LpVariable("max_dist", lowBound=0)

# Objective function
problem += max_dist

# Constraints to ensure each city is entered and left only once
for i in cities:
    problem += (sum(x[j, i] for j in cities if j != i) == 1, f"entry_{i}")
    problem += (sum(x[i, j] for j in cities if j != i) == 1, f"exit_{i}")

# Sub-tour elimination constraints
for s in range(2, n):
    for S in itertools.combinations([i for i in cities if i != 0], s):
        problem += (sum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1)

# Constraint that any route between two cities should not exceed the maximum distance
for i in cities:
    for j in cities:
        if i != j:
            problem += (x[i, j] * dist[i, j] <= max_dist, f"max_dist_{i}_{ not exceed {j}")

# Solve the problem
status = problem.solve()

if status == pulp.LpStatusOptimal:
    solution = []
    for i in cities:
        for j in cities:
            if i != j and pulp.value(x[i, j]) == 1:
                solution.append((i, j))

    # Reformat the solution into a tour
    tour = [0]
    while len(tour) < n:
        for (i, j) in solution:
            if i == tour[-1]:
                tour.append(j)
                break
    tour.append(0)  # Return to the depot

    # Calculate total travel cost and maximum distance
    total_cost = sum(dist[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    max_distance = max(dist[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No optimal solution found.")