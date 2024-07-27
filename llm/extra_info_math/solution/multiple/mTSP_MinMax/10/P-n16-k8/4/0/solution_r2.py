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
n = len(coordinates)

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in coordinates.keys() for j in coordinates.keys() if i != j}

# Problem
model = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Variables
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary')
     for k in range(num_robots) for i in range(n) for j in range(n) if i != j}
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in range(1, n)}

# Objective
model += pulp.lpSum(x[i, j, k] * distances[i, j] for k in range(num_robots) for i in range(n) for j in range(n) if i != j and (i, j, k) in x)

# Constraints
# Visit each city exactly once and return
for j in range(1, n): 
    model += pulp.lpSum(x[i, j, k] for k in range(num_robots) for i in range(n) if i != j) == 1

# Each robot leaves and comes back to the depot exactly once
for k in range(num_robots):
    model += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    model += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Each city must be connected in tour
for k in range(num_robots):
    for j in range(1, n):
        model += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) - pulp.lpSum(x[j, i, k] for i in range(n) if i != j) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(num_robots):
                model += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Solve model
model.solve()

# Output results
max_distance_traveled = 0
for k in range(num_robots):
    tour = [0]
    current_location = 0
    while True:
        found_next = False
        for j in range(n):
            if j != current_location and pulp.value(x[current_location, j, k]) == 1:
                tour.append(j)
                current_location = j
                found_next = True
                break
        if not found_next or current_location == 0:
            break
    cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    max_distance_traveled = max(max_distance_traveled, cost)

    print(f"Robot {k} Tour: {tour + [0]}")
    print(f"Robot {k} Total Travel Cost: {cost}")

print(f"Maximum Travel Cost: {max_distance_traveled}")