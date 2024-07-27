import pulp
import math

# Coordinates for the depot and the cities
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Groups of cities
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
    [2, 4, 14], [10, 17], [7, 15]
]

# Number of groups plus depot
num_groups = len(groups) + 1  # Adding 1 for the depot group which is [0]

# Calculate Euclidean distances between each pair of cities
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

distances = {}
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        if i != j:
            distances[(i, j)] = calculate_distance(coordinates[i], coordinates[j])

# Integer Programming Model
model = pulp.LpProblem("TSP_Grouped", pulp.LpMinimize)

# Decision variables: x_ij indicating travel between city i and j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(20) for j in range(20) if i != j), cat='Binary')

# Objective function: Minimize total travel cost
model += pulp.lpSum(distances[i, j] * x[i, j] for i in range(20) for j in range(20) if i != j)

# Each group must connect to exactly one node in a different group and vice versa
# Adding constraints for connections leaving and entering groups
for group in [range(20)] + groups:  # Include a "group" for the depot
    model += pulp.lpSum(x[i, j] for i in group for j in range(20) if i != j and j not in group) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in range(20) if i != j and j not in group) == 1

# Subtour Elimination Constraints
u = pulp.LpVariable.dicts("u", range(1, 20), lowBound=0, cat='Continuous')
k = 20

for i in range(1, 20):
    for j in range(1, 20):
        if i != j:
            model += u[i] - u[j] + k * x[i, j] <= k - 1

# Solve model
model.solve()

# Collect the results
tour = []
visited = set()
current = 0
while True:
    next_city = [j for j in range(20) if pulp.value(x[current, j]) == 1][0]
    tour.append(current)
    visited.add(current)
    current = next_city
    if current == 0:
        break
tour.append(0)  # go back to the depot

# Calculate total cost
total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output results
print("Tour: ", tour)
print("Total travel cost: ", total_cost)