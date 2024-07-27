import pulp
import math

# City coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254),
    4: (128, 252), 5: (163, 247), 6: (146, 246), 7: (161, 242),
    8: (142, 239), 9: (163, 236), 10: (148, 232), 11: (128, 231),
    12: (156, 217), 13: (129, 214), 14: (146, 208), 15: (164, 208),
    16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Total number of nodes including depots
n = len(cities)

# Distance matrix
dist_matrix = [[math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2) for j in range(n)] for i in range(n)]

# Initialize problem
prob = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the tour goes from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat=pulp.LpBinary)

# Objective: Minimize the sum of the distances
prob += pulp.lpSum(dist_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each city must be entered and left exactly once
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Subtour Elimination
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, cat=pulp.LpInteger)
for i in range(n):
    for j in range(1, n):  # Not allowing return to depot, depot has no u value
        if i != j:
            prob += u[j] - u[i] + (n * x[i, j]) <= n - 1

# Solve the problem
status = prob.solve()
print("Status:", pulp.LpStatus[status])

# Extract the results
tours = {i: [] for i in range(4)}  # 4 robots as per depots starting from each depot
departure = [0, 1, 2, 3]  # depot indices

for k in departure:
    # Find the starting point
    next_city = k
    tour = [k]
    while True:
        next_step = [j for i, j in x if i == next_city and pulp.value(x[i, j]) == 1]
        if not next_step:
            break
        next_city = next_step[0]
        tour.append(next_city)
        if next_city in departure:
            break
    tours[k] = tour

# Calculate costs
total_cost = 0
for k, tour in tours.items():
    cost = sum(dist_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    total_cost += cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")