import pulp
import math

# City coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Groups of cities
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Distance matrix
n = len(coordinates)
distances = [[euclidean_info for _ in range(n)] for __ in range(n)]
for i in range(n):
    for j in range(n):
        distances[i][j] = euclidean_distance(coordinates[i], coordinates[j])

# Setting up the problem
model = pulp.LpProblem("TSP_Group_Selection", pulp.LpMinimize)

# Binary decision variables x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), 
                          cat='Binary')

# Objective function
model += pulp.lpSum(x[i, j] * distances[i][j] for i in range(n) for j in range(n) if i != j)

# Flow conservation constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Outflow_{i}"
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Inflow_{i}"

# Exactly one city from each group
for group in groups:
    model += pulp.lpSum(x[0, j] for j in group) == 1, f"One_from_group_to_{group}"
    model += pulp.lpSum(x[j, 0] for j in group) == 1, f"One_to_group_from_{group}"

# Solve the problem
model.solve()

# Interpret the model output and parse the results
tour = []
current_city = 0
visited = set()
visited.add(current_city)
tour.append(current_city)

while len(tour) < len(groups) + 1:
    for j in range(n):
        if pulp.value(x[current_city, j]) == 1 and j not in visited:
            tour.append(j)
            visited.add(j)
            current_city = j
            break

# Append return to the depot
tour.append(0)

# Calculate the total travel cost
total_travel_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")