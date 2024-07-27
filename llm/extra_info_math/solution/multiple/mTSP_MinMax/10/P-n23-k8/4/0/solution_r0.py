import pulp
import math

# Calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Problem data
coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

n = len(coords)
m = 8  # Robots count

# Create a list of nodes excluding the depot
nodes = list(range(1, n))

# Calcuate the cost matrix
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:  # No loops
            cost_matrix[i, j] = euclideanrirate=(distance(coords[i], coords[j]))

# Initialize problem
prob = pulp.LpProblem("RobotRouting", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j], 0, 1, pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, n), lowBound=0, cat=pulp.LpContinuous)

# Objective: Minimize the maximum distance traveled by any robot
prob += pulp.lpSum([cost_matrix[i, j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m) if i != j])

# Constraints
for j in nodes:
    prob += pulp.lpSum([x[i, j, k] for i in range(n) for k in range(m) if i != j]) == 1

for k in range(m):
    prob += pulp.lpSum([x[0, j, k] for j in nodes]) == 1
    prob += pulp.lpSum([x[j, 0, k] for j in nodes]) == 1

for k in range(m):
    for p in nodes:
        prob += pulp.lpSum([x[i, p, k] for i in range(n) if i != p]) - pulp.lpSum([x[p, j, k] for j in range(n) if p != j]) == 0

for i in nodes:
    for j in nodes:
        if i != j:
            for k in range(m):
                prob += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem
prob.solve()

# Output the tours and calculate the costs
tours = {k: [0] for k in range(m)}
for k in range(m):
    current_location = 0
    while True:
        next_locations = [j for j in range(n) if j != current_location and pulp.value(x[current_location, j, k]) == 1]
        if not next_locations:
            break
        next_location = next_locations[0]
        tours[k].append(next_location)
        current_location = next_location
        if current_location == 0:
            break
    tours[k] += [0]

for k in tours:
    print(f"Robot {k} Tour: {tours[k]}")
    cost = sum([cost_matrix[tours[k][i], tours[k][i+1]] for i in range(len(tours[k])-1)])
    print(f"Robot {k} Total Travel Cost: {cost}")

# Calculate the maximum travel cost
max_cost = max(sum([cost_matrix[tours[k][i], tours[k][i+1]] for i in range(len(tours[k])-1)]) for k in tours)
print(f"Maximum Travel Cost: {max_cost}")