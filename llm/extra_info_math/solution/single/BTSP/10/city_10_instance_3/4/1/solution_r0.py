import pulp
import math

# Cities coordinates
coords = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Number of cities
num_cities = len(coords)

# Function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Distance matrix
distance = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            distance[i, j] = euclidean_distance(coords[i], coords[j])

# Integer Program Model
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables, x_{i,j} = 1 if city i is followed by j
x = pulp.LpVariable.dicts('x', distance.keys(), cat=pulp.LpBinary)

# Auxiliary variable for the objective (maximum edge length in the tour)
max_edge_length = pulp.LpVariable("max_edge_length", lowBound=0, cat=pulp.LpContinuous)

# Objective function: minimize the maximum distance between consecutive cities
model += max_edge_length

# Constraints
for i in range(num_cities):
    model += pulp.lpSum(x[i, j] for j in range(num_cities) if (i, j) in x) == 1  # Leave from each city once
    model += pulp.lpSum(x[j, i] for j in range(num_cities) if (j, i) in x) == 1  # Arrive at each city once

# Max edge limit constraint
for i, j in distance:
    model += distance[i, j] * x[i, j] <= max_edge_length

# Subtour elimination constraints
subsets = range(2, num_cities + 1)
for size in subsets:
    for subset in itertools.combinations(range(1, num_cities), size):
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the model
model.solve()

# Extract the solution and calculate the tour details
tour = []
current_position = 0
total_distance = 0
max_distance_between_cities = 0

# Construct the tour starting from depot
visited = set()
for _ in range(num_cities):
    for j in range(num_cities):
        if x[current_position, j].varValue == 1 and j not in visited:
            tour.append(j)
            dist = distance[current_position, j]
            total_distance += dist
            max_distance_between_cities = max(max_distance_between_cities, dist)
            current_position = j
            visited.add(j)
            break

# Adding the return to the depot
tour.append(0)
total_distance += distance[current_position, 0]
max_distance_between_cities = max(max_distance_between_cities, distance[current_position, 0])

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")
print(f"Maximum distance between consecutive cities: {max_distance_between_cities}")