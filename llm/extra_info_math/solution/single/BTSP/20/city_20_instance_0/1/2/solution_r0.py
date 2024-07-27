from scipy.spatial import distance
import pulp
import numpy as np

# Positions of the cities, with city 0 being the depot city
cities = [
    (8, 11),   # city 0 - depot
    (40, 6),   # city 1
    (95, 33),  # city 2
    (80, 60),  # city 3
    (25, 18),  # city 4
    (67, 23),  # city 5
    (97, 32),  # city 6
    (25, 71),  # city 7
    (61, 16),  # city 8
    (27, 91),  # city 9
    (91, 46),  # city 10
    (40, 87),  # city 11
    (20, 97),  # city 12
    (61, 25),  # city 13
    (5, 59),   # city 14
    (62, 88),  # city 15
    (13, 43),  # city 16
    (61, 28),  # city 17
    (60, 63),  # city 18
    (93, 15)   # city 19
]

n = len(cities)

# Compute Euclidean distances
distances = [[distance.euclidean(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Setting up the optimization problem: Min-max type TSP
problem = pulp.LpProblem('MinimizeMaxDistanceTour', pulp.LpMinimize)

# Binary variables indicating whether path i to j is taken
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Continuous variable for the maximum tour distance
max_distance = pulp.LpVariable('max_distance', lowBound=0, cat='Continuous')

# Objective function
problem += max_distance, 'Minimize the maximum distance between consecutive cities'

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Sum of paths leaving city {i} equals 1"
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Sum of paths entering city {i} equals 1"

# Max distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distances[i][j] <= max_distance, f"Max distance for path {i}-{j}"

# Subtour elimination constraints
# We use the classical subtour elimination using additional variables and constraints
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat='Integer')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + n * x[i, j] <= n - 1

# Solving the problem
problem.solve()

# Outputting the results
tour = []
current = 0
tour.append(current)
seq = n
while seq > 1:
    for j in range(n):
        if x[current, j].varValue == 1:
            tour.append(j)
            current = j
            break
    seq -= 1

tour.append(0)  # Return to the depot

tour_distances = [distances[tour[i]][tour[i+1]] for i in range(len(tour)-1)]
total_distance = sum(tour_distances)
max_tour_distance = max(tour_distances)

print("Tour:", tour)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_tour_distance)