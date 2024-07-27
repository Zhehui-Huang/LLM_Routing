import pulp
from math import sqrt
import itertools

# Define the cities and their coordinates
coordinates = {
    0: (53, 68),  # depot
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

# City groups
city_groups = {
    1: [5, 6, 7],
    2: [2, 3],
    3: [1, 9],
    4: [4, 8]
}

# Total vertices including the depot
V = list(coordinates.keys())

# Calculate Euclidean distances
def euclidean_distance(c1, c2):
    return sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

c = {}
for i in V:
    for j in V:
        if i != j:
            c[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Problem setup
prob = pulp.LpProblem("Min_Cost_Tour", pulp.LpMinimize)

# Decision variables x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in V for j in V if i != j), cat='Binary')

# Objective function
prob += pulp.lpSum(c[i, j] * x[i, j] for i in V for j in V if i != j), "Total_Cost"

# Constraints for each group for exactly one outgoing and incoming edge
for gk, cities in city_groups.items():
    prob += pulp.lpSum(x[i, j] for i in cities for j in V if j not in cities) == 1, f"Outgoing_from_group_{gk}"
    prob += pulp.lpSum(x[i, j] for j in cities for i in V if i not in cities) == 1, f"Incoming_to_group_{gk}"

# Flow conservation constraints for each vertex
for i in V:
    prob += pulp.lpSum(x[j, i] for j in V if j != i) == pulp.lpSum(x[i, j] for j in V if j != i), f"Flow_conservation_{i}"

# Subtour elimination
u = pulp.LpVariable.dicts('u', V[1:], lowBound=0, cat='Continuous')
k = len(V)
for i, j in itertools.permutations(V[1:], 2):
    prob += u[i] - u[j] + k * x[i, j] <= k - 1

# Solve the problem
prob.solve()

# Validate the solution is optimal
if pulp.LpStatus[prob.status] == "Optimal":
    tour = []
    total_cost = 0
    # Extract the tour and cost
    for i in V:
        for j in V:
            if i != j and pulp.value(x[i, j]) == 1:
                tour.append((i, j))
                total_cost += c[i, j]
    # Order the tour from the depot (0)
    ordered_tour = [0]
    next_city = next(j for i, j in tour if i == 0)
    while next_city != 0:
        ordered_tour.append(next_city)
        next_city = next(j for i, j in tour if i == next_city)
    ordered_tour.append(0) # return to depot

    print(f"Tour: {ordered_tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("Failed to find an optimal solution.")