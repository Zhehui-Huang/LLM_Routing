import pulp
import math

# City coordinates (index 0 is the depot)
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Initialize the problem
model = pulp.LpProblem("TSP_with_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x",
                          ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j),
                          cat='Binary')

# The Euclidean distance matrix
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j])
             for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j}

# Objective function
model += pulp.lpSum([x[(i, j)] * distances[(i, j)] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j]), "Total Travel Cost"

# Constraints for exactly one out-connection and one in-connection per city group and inclusion in the tour
for k, group in enumerate(groups, start=1):
    model += pulp.lpSum([x[(i, j)] for i in group for j in range(len(coordinates)) if j not in group]) == 1, f"Outflow_from_group_{k}"
    model += pulp.lpSum([x[(j, i)] for i in group for j in range(len(coordinates)) if j not in group]) == 1, f"Inflow_to_group_{k}"

# Subtour prevention across groups
for i, gi in enumerate(groups):
    for j, gj in enumerate(groups):
        if i != j:
            model += pulp.lpSum(x[(a, b)] for a in gi for b in gj) + pulp.lpSum(x[(b, a)] for a in gi for b in gj) <= 1

# Solve the model
model.solve()

# Extract the solution
tour = []
visited = [0]
current = 0
while len(visited) < len(groups) + 1:
    for j in range(len(coordinates)):
        if j != current and pulp.value(x[(current, j)]) == 1:
            tour.append(j)
            visited.append(j)
            current = j
            break
tour.append(0)

# Calculate total distance
total_cost = sum(distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

# Output the result
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")