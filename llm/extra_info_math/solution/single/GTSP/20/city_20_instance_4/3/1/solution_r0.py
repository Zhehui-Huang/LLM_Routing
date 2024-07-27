import pulp
import math

# City coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# City groups
groups = {
    0: [5, 6, 16],
    1: [8, 18, 19],
    2: [11, 12, 13],
    3: [1, 3, 9],
    4: [2, 4, 14],
    5: [10, 17],
    6: [7, 15]
}

# Calculate distances between each pair of cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# All cities list
all_cities = cities.keys()

# Setup the problem using pulp
problem = pulp.LpProblem("TSP_variant", pulp.LpMinimize)

# Variables x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), cat=pulp.LpBinary)

# Objective Function
problem += pulp.lpSum(euclidean_distance(i, j) * x[i, j] for i in all_cities for j in all_cities if i != j)

# Constraints for each group exactly 1 outgoing to a node outside the group
for group in groups.values():
    problem += pulp.lpSum(x[i, j] for i in group for j in all_cities if j not in group) == 1

# Constraints for each group exactly 1 incoming from a node outside the group
for group in groups.values():
    problem += pulp.lpSum(x[j, i] for i in group for j in all_cities if j not in group) == 1

# Flow conservation at each node
for k in all_cities:
    problem += pulp.lpSum(x[i, k] for i in all_cities if i != k) - pulp.lpSum(x[k, j] for j in all_cities if j != k) == 0

# Solve the problem
solver = pulp.PULP_CBC_CMD(msg=False, maxSeconds=30)  # Using CBC solver
problem.solve(solver)

# Extract solution
tour = []
seen = set()
current = 0
while True:
    seen.add(current)
    tour.append(current)
    next_cities = [j for j in all_cities if pulp.value(x[current, j]) == 1]
    if not next_cities:
        break
    current = next_cities[0]
    if current in seen:
        break

tour.append(0)  # return to depot

# Calculate the travel cost
total_cost = sum(euclideanMoreSalientnce(tour[i], tour[i+1]) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")