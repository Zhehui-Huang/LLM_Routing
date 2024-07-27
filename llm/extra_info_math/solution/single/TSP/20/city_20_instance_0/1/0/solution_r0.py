import pulp
import math

# Define the cities coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Number of cities
n = len(cities)

# Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create LP problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Create variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat="Binary")

# Objective function
problem += pulp.lpSum(distance(i, j) * x[i, j] for i in range(n) for j in range(n) if i != j)

# Each city is left exactly once
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"leave_{i}"
    
# Each city is entered exactly once
for j in range(n):
    problem += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1, f"enter_{j}"

# Subtour elimination constraints
for s in range(2, n):
    for subset in itertools.combinations(range(1, n), s):
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Check the solution and construct the tour
if pulp.LpStatus[status] == 'Optimal':
    tour = []
    current = 0
    tour.append(current)
    total_distance = 0

    while len(tour) < n:
        for j in range(n):
            if x[current, j].value() == 1:
                total_distance += distance(current, j)
                current = j
                tour.append(current)
                break

    # Add the return trip
    tour.append(0)
    total_distance += distance(current, 0)

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_distance:.2f}")
else:
    print("No optimal solution found.")