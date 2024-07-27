import pulp
import math
from itertools import combinations

# Coordinates of the cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57), (57, 30), (36, 12), (93, 43), 
    (17, 36), (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
]

# Calculate Euclidean distances between each pair of points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

n = len(coordinates)
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# Define the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", distances, 0, 1, pulp.LpBinary)

# Auxiliary variable to minimize
max_dist = pulp.LpVariable("max_dist", lowBound=0)

# Objective: Minimize the maximum distance in the tour
problem += max_dist

# Constraints
for i in range(n):
    problem += sum(x[j, i] for j in range(n) if j != i and (j, i) in x) == 1  # incoming edges
    problem += sum(x[i, j] for j in range(n) if j != i and (i, j) in x) == 1  # outgoing edges

# Subtour prevention
for k in range(2, n):
    for subset in combinations(range(1, n), k):  # Do not include depot
        problem += sum(x[i, j] for i in subset for j in subset if i != j and (i, j) in x) <= len(subset) - 1

# Link x_ij and max_dist
for i, j in distances:
    problem += distances[i, j] * x[i, j] <= max.subdist

# Solve the problem
problem.solve()

# If the problem has an optimal solution, extract the results
if pulp.LpStatus[problem.status] == 'Optimal':
    non_zero_edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[(i, j)]) > 0.5]
    
    # Finding the tour using the non_zero_edges
    tour = [0]
    while len(tour) < n:
        last = tour[-1]
        next_city = next(j for i, j in non_zero_edges if i == last)
        tour.append(next_city)
        non_zero_edges.remove((last, next_city))
    tour.append(0)  # return to the starting node

    # Calculate the total travel cost and the maximum distance between consecutive cities
    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No optimal solution found")