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

# Constants
all_cities = set(cities.keys())
selected_from_group = {}

# Setup the problem using pulp
problem = pulp.LpProblem("TSP_variant", pulp.LpMinimize)

# Variables x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in all_cities for j in all_cities if i != j), cat=pulp.LpBinary)

# Objective Function
problem += pulp.lpSum(euclidean_distance(i, j) * x[i, j] for i in all_cities for j in all_cities if i != j)

# Constraints for each group exactly 1 outgoing to a node outside the group
for group_idx, group in groups.items():
    problem += pulp.lpSum(x[i, j] for i in group for j in all_cities if j not in group) == 1
    problem += pulp.lpSum(x[j, i] for i in group for j in all_cities if j not in group) == 1

# Flow conservation at each node
for k in all_cities:
    problem += pulp.lpSum(x[i, k] for i in all_cities if i != k) == pulp.lpSum(x[k, j] for j in all_cities if j != k)

# Subtour Elimination Constraints
u = pulp.LpVariable.dicts('u', all_cities, lowBound=0, cat=pulp.LpContinuous)
for i in all_cities:
    for j in all_cities:
        if i != j and i != 0 and j != 0:
            problem += u[i] - u[j] + len(all_cities) * x[i, j] <= len(all_cities) - 1

# Solve the problem
problem.solve(pulp.PULP_CBC_CMD(msg=False, timeLimit=120))

# Extract solution
tour = []
seen = set()
current = 0

while True:
    next_cities = [j for j in all_cities if j != current and pulp.value(x[current, j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    if next_city in seen:
        break
    seen.add(next_city)
    tour.append(current)
    current = next_city

# Ensuring tour returns to the depot
tour.append(0)  # Including the return to the depot in the tour list

# Calculate the travel cost
total_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")