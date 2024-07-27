import math
import pulp

# Coordinates of the 10 cities including the depot city 0
coordinates = [
    (90, 3),  # depot city 0
    (11, 17),
    (7, 27),
    (95, 81),
    (41, 54),
    (31, 35),
    (23, 95),
    (20, 56),
    (49, 29),
    (13, 17)
]

# Total number of cities
n = len(coordinates)

# Calculating the Euclidean distance between each pair of cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Setting up the ILP problem
problem = pulp.LpProblem("TSP_MinMax", pulp.LpMinimize)

# Variables: x[i][j] is 1 if travels from i to j, else 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Auxiliary variable to minimize the maximum distance between consecutive cities
max_dist = pulp.LpVariable("max_dist", lowBound=0, cat='Continuous')

# Objective: minimize the maximum distance used in any segment of the tour
problem += max_dist

# Constraints
for i in range(n):
    # One outgoing edge from each city
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    
    # One incoming edge to each city
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour prevention constraints using sequential ordering
u = pulp.LpVariable.dicts("u", range(n), lowBound=1, upBound=n-1, cat='Continuous')

for i in range(1, n):
    for j in range(1, n):
        if i != j:
            problem += u[i] - u[j] + (n * x[i, j]) <= n - 1

# Link max_dist to the distances
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distances[i][j] <= max measures_dist

# Solving the problem
problem.solve()

# Result extraction
tour = []
current_location = 0
visited = set([0])

while len(visited) < n:
    for j in range(n):
        if pulp.value(x[current_location, j]) == 1 and j not in visited:
            tour.append(j)
            visited.add(j)
            current_location = j
            break
tour.append(0)  # return to the depot

# Calculate the total cost and the maximum distance in the solution tour
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")