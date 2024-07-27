import pulp
import math
import itertools

# Define the city coordinates
coordinates = [
    (26, 60),  # City 0 (Depot)
    (73, 84),
    (89, 36),
    (15, 0),
    (11, 10),
    (69, 22),
    (28, 11),
    (70, 2),
    (47, 50),
    (60, 29),
    (29, 26),
    (85, 68),
    (60, 1),
    (71, 73),
    (82, 47),
    (19, 25),
    (75, 9),
    (52, 54),
    (64, 72),
    (14, 89)
]

n = len(coordinates)  # Including the depot

# Distance calculation
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance dictionary
distances = {(i, j): distance(coordinates[i], coordinates[j]) for i in range(n) for j in range(n) if i != j}

# ILP Setup
problem = pulp.LpProblem("Min_Max_TSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
max_dist = pulp.LpVariable("max_dist", lowBound=0)

# Objective
problem += max_dist

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distances[i, j] <= max_dist

# Adding subtour elimination constraints
for s in range(2, n):
    for S in itertools.combinations(range(n), s):
        problem += pulp.lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve Problem
problem.solve()

# Extract solution if optimal
if pulp.LpStatus[problem.status] == 'Optimal':
    tour = []
    position = 0
    while len(tour) < n:
        for j in range(n):
            if position != j and pulp.value(x[position, j]) == 1:
                tour.append(position)
                position = j
                break
    tour.append(0)  # Return to depot to complete cycle

    # Calculate maximum distance and total cost
    max_distance = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

    # Output result
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No optimal solution found.")