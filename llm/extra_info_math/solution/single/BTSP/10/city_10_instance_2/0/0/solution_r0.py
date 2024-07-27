import pulp
import math

# City coordinates
coordinates = [
    (90, 3),  # Depot city 0
    (11, 17),  # City 1
    (7, 27),   # City 2
    (95, 81),  # City 3
    (41, 54),  # City 4
    (31, 35),  # City 5
    (23, 95),  # City 6
    (20, 56),  # City 7
    (49, 29),  # City 8
    (13, 17)   # City 9
]

# Number of cities
n = len(coordinates)

# Euclidean distance calculation
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the distance matrix
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = distance(coordinates[i], coordinates[j])
        else:
            distance_matrix[i, j] = 0

# Problem definition
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts('x', distance_matrix.keys(), cat=pulp.LpBinary)
max_distance = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective function: minimize the maximum distance
prob += max_distance

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave from each city
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1  # arrive to each city

# Subtour elimination
for i in range(1, n):
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) <= 1

for S in range(2, n):
    for subset in itertools.combinations(range(1, n), S):
        prob += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Maximum distance constraint
for i, j in distance_matrix:
    prob += x[i, j] * distance_matrix[i, j] <= max_distance

# Solve
solver = pulp.PULP_CBC_CMD(msg=False)
prob.solve(solver)

# Solution extraction
tour = []
total_distance = 0
for i in range(n):
    for j in range(n):
        if pulp.value(x[i, j]) == 1:
            tour.append((i, j))
            total_distance += distance_matrix[i, j]

# Reconstructing the tour from the decision variables
current_location = 0
tour_sequence = [current_location]
for _ in range(n - 1):
    next_location = next(j for i, j in tour if i == current_location)
    current_location = next_location
    tour_sequence.append(current_location)
tour_sequence.append(0)  # Append the return to the depot

# Compute maximum distance in the final tour
max_tour_distance = max(distance_matrix[tour_sequence[i], tour_sequence[i+1]] for i in range(len(tour_sequence)-1))

# Output the solution
print("Tour:", tour_sequence)
print("Total travel cost:", total_distance)
print("Maximum distance between consecutive cities:", max_tour_distance)