import pulp
import math
import itertools

# Coordinates of cities including the depot
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
    19: (19, 72)
}

n = len(cities)  # Total number of cities including the depot

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Setup the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective Function
prob += pulp.lpSum(x[(i, j)] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1, f"One_out_{i}"
    prob += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1, f"One_in_{i}"

# Subtour elimination constraints
for S in range(3, n):
    for subset in itertools.combinations(range(1, n), S):
        prob += pulp.lpSum(x[(i, j)] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
prob.solve()

# Check if a feasible solution was found
if pulp.LpStatus[prob.status] == "Optimal":
    path = []
    current = 0
    count = 0
    while len(path) < n:
        path += [current]
        next_moves = [j for j in range(n) if j not current and pulp.value(x[current, j]) == 1]
        if next_moves:
            current = next_moves[0]
        count += 1
        if count > n:
            break
    path.append(0)  # return to depot
    total_distance = sum(euclidean_distance(path[i], path[i + 1]) for i in range(len(path) - 1))

    print(f"Tour: {path}")
    print(f"Total travel cost: {total_distance:.2f}")
else:
    print("No optimal solution found. Status is", pulp.LpStatus[prob.status])