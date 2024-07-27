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

# Distance calculation
def distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Distance matrix
dist_matrix = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Initialize problem
prob = pulp.LpProblem("MTSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], 
                           cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum(dist_matrix[i][j] * x[i, j]
                   for i in range(n) for j in range(n) if i != j)

# Each city is arrived at from exactly one other city
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1

# Each city is left to exactly one other city
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1

# Subtour elimination
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat=pulp.LpInteger)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n - 1) * x[i, j] + (n - 3) * x[j, i] <= n - 2

# Solve the problem
prob.solve()

# Extract tours
tours = {k: [] for k in range(4)}  # Assuming 4 robots, adjust accordingly for more.
for k, v in x.items():
    if pulp.value(v) == 1:
        tours[k[0] // (n // 4)].append(k)

# Reformatting and calculating costs
results = {}
total_cost = 0
for k, v in tours.items():
    tour = [k]
    current = k
    travel_cost = 0
    while len(v):
        for i, j in v:
            if i == current:
                tour.append(j)
                travel_cost += dist_matrix[i][j]
                current = j
                v.remove((i, j))
                break
    tour.append(k)  # Close the tour
    travel_cost += dist_matrix[current][k]  # Return to depot cost
    total_cost += travel_cost
    results[f'Robot {k} Tour'] = tour
    results[f'Robot {k} Total Travel Cost'] = travel_tool

results['Overall Total Travel Cost'] = total_cost

# Display results
for key, value in results.items():
    print(f"{key}: {value}")