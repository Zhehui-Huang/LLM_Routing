import pulp
import math

# Coordinates of cities including the depot city
cities = {
    0: (30, 56),
    1: (53, 42),
    2: (1, 95),
    3: (25, 61),
    4: (69, 57),
    5: (6, 58),
    6: (12, 84),
    7: (72, 77),
    8: (98, 95),
    9: (11, 0),
    10: (61, 25),
    11: (52, 0),
    12: (60, 95),
    13: (10, 94),
    14: (96, 73),
    15: (14, 47),
    16: (18, 16),
    17: (4, 43),
    18: (53, 76),
    19: (19, 72),
}

# Number of cities
n = len(cities)

# Helper function to calculate Euclidean distance
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), 0, 1, pulp.LpBinary)

# Objective function
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += (pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1, f"leave_{i}")
    prob += (pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1, f"enter_{i}")

# Subtour elimination
for S in range(3, n):
    for subset in itertools.combinations(range(1, n), S):
        prob += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = prob.solve()

# Check if a valid solution was found
if pulp.LpStatus[status] == "Optimal":
    tour = []
    current = 0
    while True:
        tour.append(current)
        next_cities = [j for j in range(n) if x[(current, j)].varValue == 1]
        if not next_cities:
            break
        current = next_cities[0]
    tour.append(0)  # Append the depot city at the end
    total_cost = pulp.value(prob.objective)

    # Output the results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")