import pulp
import math

# Coordinates of the cities including the depot
coordinates = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
    (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
    (83, 96), (60, 50), (98, 1)
]

# Calculating Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Distance matrix
n = len(coordinates)
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# TSP Model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
model += pulp.lpSum(cost[i][j] * x[i, j] for i in range(n) for j in range(n)), "Total_Travel_Cost"

# Constraints
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"Leave_{i}"
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"Enter_{i}"

# Subtour elimination constraints
for i in range(2, n):
    subsets = itertools.combinations(range(1, n), i)
    for subset in subsets:
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the model
model.solve()

# Extracting the solution
tour = []
visited = 0
while True:
    for i in range(n):
        if x[visited, i].varValue == 1:
            tour.append(visited)
            visited = i
            break
    if visited == 0:
        break

tour.append(0)  # Return to the depot

# Calculate the total cost
total_cost = sum(cost[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)