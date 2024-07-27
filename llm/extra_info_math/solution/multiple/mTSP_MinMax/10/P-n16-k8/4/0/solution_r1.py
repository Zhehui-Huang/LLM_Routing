import pulp
import math

# Input data
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64),
    4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}
num_robots = 8
n = len(coordinates)  # Includes the depot

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in coordinates.keys() for j in coordinates.keys() if i != j}

# Problem
model = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Variables
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary') for k in range(num_robots) for i in range(n) for j in range(n) if i != j}
u = {i: pulp.LpVariable(f"u_{i}", lowBound=1, upBound=n-1, cat='Continuous') for i in range(1, n)}

# Objective
model += pulp.lpSum(distances[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(num_robots) if i != j)

# Constraints
for j in range(1, n):  # Exclude depot
    model += sum(x[i, j, k] for i in range(n) for k in range(num_robots) if i != j) == 1

for k in range(num_robots):
    model += sum(x[0, j, k] for j in range(1, n)) == 1
    model += sum(x[j, 0, k] for j in range(1, n)) == 1

for k in range(num_robots):
    for j in range(1, n):
        model += sum(x[i, j, k] for i in range(n) if i != j) - sum(x[j, i, k] for i in range(n) if i != j) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(num_robots):
                model += u[i] - u[j] + (n-1) * x[i, j, k] <= n-2

# Solve
model.solve()

# Display results
for k in range(num_robots):
    tour = [0]
    costs = []
    while True:
        candidates = [(j, x[tour[-1], j, k]) for j in range(n) if (tour[-1], j, k) in x and pulp.value(x[tour[-1], j, k]) == 1]
        if not candidates:
            break
        next_city = candidates[0][0]
        tour.append(next_city)
        costs.append(distances[tour[-2], next_city])
        if next_city == 0:
            break

    if len(tour) > 2:
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {sum(costs)}")

# Fetching maximum distance traveled
max_distance = max(sum(distances[tour[i - 1], tour[i]] * (tour[i - 1] != tour[i]) for i in range(1, len(tour))) for tour in tours if len(tour) > 1)
print(f"Maximum Travel Cost: {max_distance}")