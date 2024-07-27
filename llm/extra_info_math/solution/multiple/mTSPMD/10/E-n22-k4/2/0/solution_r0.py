import pulp
import math

# Define city coordinates
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Number of robots and their depots
num_robots = 4
depots = [0, 1, 2, 3]
depot_city_map = {depots[i]: i for i in range(num_robots)}

# Creating the LP problem
prob = pulp.LpProblem("MDVRP", pulp.LpMinimize)

# Decision variables
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", 0, 1, pulp.LpBinary)
     for i in range(22) for j in range(22) if i != j for k in depots}

# Subtour elimination helper variables
u = {i: pulp.LpVariable(f"u_{i}", 0, 22, pulp.LpInteger) for i in range(22)}

# Objective function
prob += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(22) for j in range(22) if i != j for k in depots)

# Constraints
# Salesmen exit from each depot
for k in depots:
    prob += pulp.lpSum(x[k, j, k] for j in range(22) if j != k) == 1

# Each city is visited exactly once
for j in range(4, 22):  # excluding depots
    prob += pulp.lpSum(x[i, j, k] for i in range(22) for k in depots if i != j) == 1
    prob += pulp.lpSum(x[j, i, k] for i in range(22) for k in depots if i != j) == 1

# Route continuity
for i in range(22):
    for k in depots:
        prob += (pulp.lpSum(x[i, j, k] for j in range(22) if i != j) ==
                pulp.lpSum(x[j, i, k] for j in range(22) if i != j))

# Subtour elimination
for i in range(4, 22):
    for j in range(4, 22):
        if i != j:
            for k in depots:
                prob += u[i] - u[j] <= 21 * (1 - x[i, j, k]) - 1

# Solve the problem
solve_status = prob.solve()

# Extract solution
tours = {k: [] for k in depots}
for k in depots:
    tour = [k]
    next_city = k
    while True:
        next_city = next(j for j in range(22) if pulp.value(x[next_city, j, k]) == 1)
        if next_city == k:
            break
        tour.append(next_city)
    tour.append(k)
    tours[k] = tour

# Calculate each robot's travel cost
costs = {}
total_cost = 0
for k in depots:
    cost = sum(distance(tours[k][i], tours[k][i+1]) for i in range(len(tours[k])-1))
    costs[k] = cost
    total_cost += cost

# Print the outputs
for k in depots:
    print(f"Robot {depot_city_map[k]} Tour: {tours[k]}")
    print(f"Robot {depot_city_map[k]} Total Travel Cost: {costs[k]}")

print(f"Overall Total Travel Cost: {total_cost}")