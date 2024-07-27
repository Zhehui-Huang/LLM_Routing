import pulp
import math
import itertools

# Coordinates of the cities including the depot
coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Calculate Euclidean distance
def euclidean_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

n = len(coordinates)

# Setup the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)
x = {}
for i in range(n):
    for j in range(n):
        if i != j:
            x[(i, j)] = pulp.LpVariable(f"x_{i}_{j}", cat='Binary')

# Objective Function
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Subtour elimination
for m in range(2, n):
    for subset in itertools.combinations(range(1, n), m):
        prob += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

if prob.status == 1:  # 1 means the problem was solved optimally
    tour = [0]
    while len(tour) < n:
        for j in range(n):
            if j not in tour and x[(tour[-1], j)].varValue == 1:
                tour.append(j)
                break

    # Adding the return step to the depot
    tour.append(0)

    # Calculate the total distance
    total_distance = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance:.2f}")
else:
    print("Failed to find an optimal solution.", "Status Code:", prob.status)