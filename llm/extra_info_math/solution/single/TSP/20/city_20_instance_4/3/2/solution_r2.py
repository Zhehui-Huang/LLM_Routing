import pulp
import math

# Coordinates of the cities including the depot city
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10), 5: (69, 22),
    6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29), 10: (29, 26), 11: (85, 68),
    12: (60, 1), 13: (71, 73), 14: (82, 47), 15: (19, 25), 16: (75, 9), 17: (52, 54),
    18: (64, 72), 19: (14, 89)
}

n = len(cities)  # Number of cities

# Euclidean distance calculator
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Cost matrix
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[(i, j)] = euclidean_distance(cities[i], cities[j])

# Set up the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts('x', cost_matrix.keys(), cat=pulp.LpBinary)

# Objective function
prob += pulp.lpSum([cost_matrix[(i,j)] * x[(i,j)] for (i, j) in x]), "Minimize_Total_Travel_Cost"

# Constraints
for i in range(n):
    prob += pulp.lpSum([x[(i, j)] for j in range(n) if j != i]) == 1, f"Leave_{i}"
    prob += pulp.lpSum([x[(j, i)] for j in range(n) if j != i]) == 1, f"Enter_{i}"

# Subtour elimination constraints (add later if necessary)
def get_subtours(x):
    subtours = []
    visited = [False]*n
    for i in range(n):
        if not visited[i]:
            subtour = []
            j = i
            while not visited[j]:
                subtour.append(j)
                visited[j] = True
                j = next(k for k in range(n) if pulp.value(x[(j, k)]) == 1)
            if len(subtour) > 1:  # Cycle needs at least 2 nodes
                subtours.append(subtour)
    return subtours

# Solve the problem
prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Extract subtours and impose further constraints if subtours existing
while True:
    subtours = get_subtours(x)
    if any(len(st) < n for st in subtours):
        for st in subtours:
            if len(st) < n:
                prob += pulp.lpSum([x[i, j] for i in st for j in st if i != j]) <= len(st) - 1
        prob.solve(pulp.PULP_CBC_CMD(msg=0))
    else:
        break

# Extract solution
tour = []
current_city = 0
while len(tour) < n:
    tour.append(current_city)
    next_cities = [j for j in range(n) if pulp.value(x[(current_city, j)]) == 1]
    current_city = next_cities[0]

tour.append(tour[0])  # Back to the depot
total_cost = sum(cost_matrix[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)