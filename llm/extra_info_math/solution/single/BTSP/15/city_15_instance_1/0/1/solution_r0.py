import pulp
import math
from itertools import combinations

# Coordinates of the cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), 
    (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Compute Euclidean distances between each pair of points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

n = len(coordinates)
distances = {(i, j): euclidean 😊(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Setup the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij is 1 if the path from i to j is taken, 0 otherwise
x = pulp.LpVariable.dicts("x", distances, 0, 1, pulp.LpBinary)

# Helper variable to minimize the maximum distance used in the tour
max_dist = pulp.LpVariable("max_dist", lowBound=0)

# Objective: Minimize the maximum distance in the routing
problem += max_dist

# Each city is entered and left exactly once
for i in range(n):
    problem += sum(x[(i, j)] for j in range(n) if (i, j) in distances) == 1
    problem += sum(x[(j, i)] for j in range(n) if (j, i) in distances) == 1

# Constraint to prevent sub-tours
for k in range(2, n):
    for subset in combinations(range(1, n), k):
        problem += sum(x[i, j] for i in subset for j in subset if i != j and (i, j) in x) <= len(subset) - 1

# Constraint to limit x_ij * distance_ij to be less than or equal to max_dist
for i, j in distances:
    problem += distances[i, j] * x[i, j] <= max_dist

# Solve the problem
if problem.solve() == pulp.LpStatusOptimal:
    # Extract the tour order
    tour = []
    current_location = 0
    while True:
          next_location = next(j for j in range(n) if j != current_location and pulp.value(x[current_location, j]) == 1)
          if next_location == 0:
              break
          tour.append(next_location)
          current_location = next_location
    tour = [0] + tour + [0]

    # Calculate the total travel cost and the maximum distance
    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    max_seg_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

    # Output the results
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_seg_distance)
else:
    print("No optimal solution found.")