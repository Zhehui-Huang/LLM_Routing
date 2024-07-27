import math
import pulp

# Coordinates of cities
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# City groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
    [2, 4, 14], [10, 17], [7, 15]
]

# Calculate Euclidean distances between each pair of cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Define the problem
prob = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Variables - x[i][j] is 1 if the path from city i to j is chosen; otherwise it's 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), cat='Binary')

# Objective Function
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraints
# Each group must connect to the tour exactly twice (once in, once out)
for group in groups:
    # Sum of all incoming edges to nodes in the group should be 1
    prob += pulp.lpSum(x[j][i] for i in group for j in range(len(coordinates)) if j != i) == 1
    # Sum of all outgoing edges from nodes in the group should be 1
    prob += pulp.lpSum(x[i][j] for i in group for j in range(len(new_coordinates)) if j != i) == 1

# Flow conservation for each city means that each city j must have exactly one incoming and one outgoing edge
for j in range(1, len(coordinates)):
    prob += pulp.lpSum(x[i][j] for i in range(len(coordinates)) if i != j) == pulp.lpSum(x[j][k] for k in range(len(coordinates)) if k != j)

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current_city = 0
visited = [False] * len(coordinates)
visited[0] = True
count = 0

while not all(visited) and count < len(coordinates):
    for next_city in range(1, len(coordinates)):
        if x[current_city][next_city].value() == 1 and not visited[next_city]:
            tour.append(next_city)
            visited[next_city] = True
            current_city = next_city
            break
    count += 1

# Appending back to the depot
tour.insert(0, 0) # Start at depot
tour.append(0) # Return to depot

# Compute the total tour distance
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)