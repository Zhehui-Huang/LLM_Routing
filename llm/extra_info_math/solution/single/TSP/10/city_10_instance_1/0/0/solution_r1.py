import pulp
import math

# City coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

def calculate_distance(c1, c2):
    """ Calculate Euclidean distance between two coordinates """
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

n = len(cities)  # Number of cities total, including the depot

# Distance matrix
costs = {(i, j): calculate_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Create the problem
prob = pulp.LpProblem('TSP', pulp.LpMinimize)

# Variables
x = {
    (i, j): pulp.LpVariable(f'x_{i}_{j}', cat='Binary')
    for i in cities for j in cities if i != j
}

# Objective
prob += pulp.lpSum(x[i, j] * costs[i, j] for i in cities for j in cities if i != j)

# Constraints
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if j != i) == 1, f"Outgoing_{i}"
    prob += pulp.lpSum(x[j, i] for j in cities if j != i) == 1, f"Incoming_{i}"

# Subtour Elimination
u = pulp.LpVariable.dicts('u', cities, 1, n-1, cat='Integer')
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + n * x[i, j] <= n - 1

# Solve the problem
prob.solve()

# Extracting the tour
tour = []
current_city = 0
while len(tour) < n:
    tour.append(current_id)
    next_cities = [j for j in cities if j != current_city and pulp.value(x[current_city, j]) == 1]
    if next_cities:
        current_city = next_cities[0]
    else:
        break

tour.append(0)  # To return to depot

# Calculate total travel cost
total_cost = sum(costs[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")