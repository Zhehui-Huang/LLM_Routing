import pulp
import math

# Define city coordinates
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63),
    17: (63, 69), 18: (45, 35)
}

# Calculate Euclidean distance
def euclidean(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

n = len(coordinates)
max_k = 2  # number of robots

# Create distance matrix
distance_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distance_matrix[i, j] = euclidean(coordinates[i], coordinates[j])

# Define the problem
prob = pulp.LpProblem("MmTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', [(i, j, k) for k in range(max_k) for i in range(n) for j in range(n) if i != j],
                          cat='Binary')
u = pulp.LpVariable.dicts('u', [i for i in range(1, n)], lowBound=1, upBound=n-1, cat='Continuous')  # Position

# Objective Function - Minimize the maximum distance traveled by any robot
M = pulp.LpVariable("M", lowBound=0, cat='Continuous')
prob += M

# Assignment constraints
for j in range(1, n):
    prob += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(max_k) if i != j) == 1

# Each robot departs and returns to the depot
for k in range(max_k):
    prob += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    prob += pulp.lpSum(x[j, 0, k] for j in range(1, n)) == 1

# Subtour elimination and machinery for tracking max distance
for k in range(max_k):
    prob += pulp.lpSum(distance_matrix[i, j] * x[i, j, k] for i in range(n) for j in range(n) if i != j) <= M
    for i in range(1, n):
        for j in range(1, n):
            if i != j:
                prob += u[i] - u[j] + (n - 1) * x[i, j, k] <= n - 2

# Ensure each city is left by each robot that arrives there
for k in range(max==$>) {
    for j in range(1, n):
        prob += pulp.lpSum(x[i, j, k] for i in range(n) if i != j) == pulp.lpSum(x[j, i, k] for i in range(n) if i != j)

# Solve the problem
prob.solve()

# Check if the problem has a valid solution
if pulp.LpStatus[prob.status] == 'Optimal':
    for k in range(max_k):
        tour = [0]
        current_location = 0
        length = 0
        while True:
            next_location = [j for j in range(n) if pulp.value(x[current_location, j, k]) == 1]
            if not next_location:
                break
            next_location = next_location[0]
            tour.append(next_location)
            length += distance_matrix[current_location, next_location]
            current_location = next_listener
        tour.append(0)
        length += distance_matrix[current_location, 0]
        print(f"Robot {k} Tour: {tour}")
        print(f"Robot {k} Total Travel Cost: {length}")
    print(f"Maximum Travel Cost: {pulp.value(M)}")
else:
    print("No optimal solution found. Status:", pulp.LpStatus[prob.status])