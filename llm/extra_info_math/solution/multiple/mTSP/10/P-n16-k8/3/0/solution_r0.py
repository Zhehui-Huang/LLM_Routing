import pulp
import math

# Define the coordinates of the cities (including the depot city at index 0)
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69)
]

# Number of robots
m = 8

# Number of cities (including the depot)
n = len(coordinates)

# Calculate Euclidean distance between any two cities
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix c_ij
c = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n)}

# Set up the problem
prob = pulp.LpProblem("mTSP", pulp.LpMinimize)

# Decision variables x_ijk: binary
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m)],
                          cat=pulp.LpBinary)

# Auxiliary variables u_i: continuous (position in the tour)
u = pulp.LpVariable.dicts("u", [i for i in range(1, n)], lowBound=1, upBound=n-1, cat=pulp.LpContinuous)

# Objective: Minimize total cost
prob += pulp.lpSum([c[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m)])

# Constraints:
# 1. Each city (except depot) is visited exactly once by any salesman
for j in range(1, n):
    prob += pulp.lpSum([x[i, j, k] for i in range(n) for k in range(m) if i != j]) == 1

# 2. Salesmen leave and enter each visited city exactly once
for k in range(m):
    for j in range(1, n):
        prob += pulp.lpSum([x[i, j, k] for i in range(n) if i != j]) \
                - pulp.lpSum([x[j, i, k] for i in range(n) if i != j]) == 0

# 3. Each salesman starts from the depot
for k in range(m):
    prob += pulp.lpSum([x[0, j, k] for j in range(1, n)]) == 1

# 4. Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
prob.solve()

# Output the solution
if prob.status == 1:  # Check if the problem was solved successfully
    total_cost = 0
    for k in range(m):
        tour = []
        for i in range(n):
            for j in range(n):
                if pulp.value(x[i, j, k]) == 1:
                    tour.append((i, j))
        # Construct the actual tour from the starting node
        current_location = 0
        actual_tour = [0]
        tour_cost = 0
        while True:
            next_step = next((j for i, j in tour if i == current_location), None)
            if next_step is None or next_step == 0:
                tour_cost += c[current_location, 0]
                actual_tour.append(0)
                break
            actual_tour.append(next_step)
            tour_cost += c[current_location, next_step]
            current_location = next_step
        print(f"Robot {k} Tour: {actual_tour}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")
        total_cost += tour_cost
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No solution found.")