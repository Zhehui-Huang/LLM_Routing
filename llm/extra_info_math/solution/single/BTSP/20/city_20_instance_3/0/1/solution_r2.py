import math
import pulp

# Define the coordinates of each city including the depot
cities = [
    (30, 56),   # Depot city 0
    (53, 42),   # City 1
    (1, 95),    # City 2
    (25, 61),   # City 3
    (69, 57),   # City 4
    (6, 58),    # City 5
    (12, 84),   # City 6
    (72, 77),   # City 7
    (98, 95),   # City 8
    (11, 0),    # City 9
    (61, 25),   # City 10
    (52, 0),    # City 11
    (60, 95),   # City 12
    (10, 94),   # City 13
    (96, 73),   # City 14
    (14, 47),   # City 15
    (18, 16),   # City 16
    (4, 43),    # City 17
    (53, 76),   # City 18
    (19, 2)     # City 19
]

n = len(cities)

# Calculate the Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Create the problem
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')
z = pulp.LpVariable("z", lowBound=0, cat='Continuous')

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * euclidean_distance(cities[i], cities[j]) <= z

# Eliminate sub-tours
for sub_set in (set(comb) for comb in itertools.combinations(range(1, n), r) for r in range(2, n)):
    problem += pulp.lpSum(x[i, j] for i in sub_set for j in sub_set if i != j) <= len(sub_set) - 1

# Objective function
problem += z

# Solve the problem
problem.solve()

# Collect the result
tour = []
current_city = 0
initial = True

while initial or current_city != 0:
    initial = False
    for j in range(n):
        if x[current_city, j].varValue == 1:
            tour.append(j)
            current_city = j
            break

# Calculate the total and maximum distance
total_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))
max_distance = max(euclidean_distance(cities[tour[i]], cities[tour[i + 1]]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)
print("Maximum distance between consecutive cities:", max_distance)