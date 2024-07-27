import pulp
import math

# Define the city coordinates
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

n = len(cities)  # Total cities

# Calculate distances between each pair of cities
distances = {}
for i in range(n):
    for j in range(n):
        if i != j:
            distances[(i, j)] = math.sqrt((cities[i][0] - cities[j][0])**2 + (cities[i][1] - cities[j][1])**2)
        else:
            distances[(i, j)] = float('inf')

# Setting up the optimization problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')
z = pulp.LpVariable("z", cat='Continuous')

# Objective function
problem += z, "Maximization of the minimum distance"

# Constraints
# Every city needs to be arrived at from exactly one other city
for j in cities:
    problem += pulp.lpSum(x[(i, j)] for i in cities if i != j) == 1

# Every city needs to be left to exactly one other city
for i in cities:
    problem += pulp.lpSum(x[(j, i)] for j in cities if i != j) == 1

# Subtour elimination
for S in range(2, n):
    for subset in combinations(cities, S):
        problem += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Maximum distance constraint
for i in cities:
    for j in cities:
        if i != j:
            problem += x[(i, j)] * distances[(i, j)] <= z

# Solve the problem
status = problem.solve()
if status == pulp.LpStatusOptimal:
    print("Solution is optimal!")

# Extract solution
edges = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[(i, j)]) == 1]
print("Edges in the tour:", edges)

# Reconstruct the tour from the solution edges
tour = [0]  # Start at the initial city
while len(tour) < n:
    for i, j in edges:
        if i == tour[-1]:
            tour.append(j)
            break
tour.append(0)  # Return to the start

# Calculate the total cost and maximum leg distance
total_cost = sum(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
max_leg_distance = max(distances[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_leg_distance)