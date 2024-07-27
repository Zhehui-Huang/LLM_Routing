import math
import pulp

# Coordinates of the cities including the depot city
coordinates = [
    (50, 42), (41, 1), (18, 46), (40, 98), 
    (51, 69), (47, 39), (62, 26), (79, 31), 
    (61, 90), (42, 49)
]

n = len(coordinates)  # Number of cities including the depot

# Define a function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the distance matrix
distances = {
    (i, j): euclidean_distance(coordinates[i], coordinates[j])
    for i in range(n) for j in range(n) if i != j
}

# Setup the model
model = pulp.LpProblem("Minimize_Max_Distance_in_TSP", pulp.LpMinimize)

# Variables: x_ij represents whether the edge from city i to city j is used
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
# Variable to minimize the maximum distance traveled in a single step
z = pulp.LpVariable("z", lowBound=0)

# Objective Function: Minimize the maximum distance between consecutive cities
model += z

# Constraints:

# Each city must be left and entered exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour Elimination Constraints:
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + n*x[i, j] <= n-1

# Max distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            model += distances[i, j] * x[i, j] <= z

# Solve the model
model.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract the tour from solution
tour = []
visited = set()
current = 0
tour.append(current)

while True:
    # Find next city with x[current, next] == 1
    next_candidates = [j for j in range(n) if j != current and pulp.value(x[current, j]) == 1]
    if not next_candidates:
        break
    next_city = next_candidates[0]
    if next_city in visited:
        break
    tour.append(next_city)
    visited.add(next_city)
    current = next_city

tour.append(0)  # Returning to the starting city

# Calculate the maximum and total distance
total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
max_distance = max(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")