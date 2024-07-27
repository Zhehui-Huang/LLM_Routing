import pulp
import math

# City Coordinates
cities = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Groups of cities
groups = [
    [7, 9],
    [1, 3],
    [4, 6],
    [8],
    [5],
    [2]
]

# Calculate Euclidean distances
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {}
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = calculatecurrency_distance(cities[i], cities[j])

# Sets and indices
all_nodes = list(cities.keys())
all_groups = {i: g for i, g in enumerate(groups)}

# Optimization model
model = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variable: x_ij = 1 if travel from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j) for i in all_nodes for j in all_nodes if i != j], cat='Binary')

# Objective function: Minimize total distance
model += pulp.lpSum([distances[(i, j)] * x[i, j] for i in all_nodes for j in all_nodes if (i, j) in distances]), "Total_Distance_Traveled"

# Constraints for ensuring exactly one exit and entry for each group
for group in all_groups.values():
    model += pulp.lpSum(x[i, j] for i in group for j in all_nodes if j not in group) == 1, f"One_exit_{group}"
    model += pulp.lpSum(x[j, i] for i in group for j in all_nodes if j not in group) == 1, f"One_entry_{group}"

# Flow conservation constraint
for i in all_nodes:
    model += pulp.lpSum(x[j, i] for j in all_nodes if j != i) == pulp.lpSum(x[i, k] for k in all_nodes if k != i), f"Flow_conservation_{i}"

# Subtour elimination
u = pulp.LpVariable.dicts("u", [i for i in all_nodes if i != 0], lowBound=0, upBound=len(all_nodes)-1, cat='Continuous')
for i in all_nodes:
    for j in all_nodes:
        if i != j and i != 0 and j != 0:
            model += u[i] - u[j] + (len(all_nodes)-1) * x[i, j] <= len(all_nodes) - 2

# Solve the problem
model.solve()

# Output the solution
tour = []
total_cost = 0
for i in all_nodes:
    for j in all_nodes:
        if i != j and pulp.value(x[i, j]) == 1:
            tour.append((i, j))
            total_cost += distances[(i, j)]

# Reconstruct tour start and end at depot (0)
sorted_tour = [0]
while len(sorted_tour) < len(tour):
    last = sorted_tour[-1]
    for l in tour:
        if l[0] == last:
            sorted_tour.append(l[1])
            break

sorted_tour.append(0)  # Append the depot city at the end

print("Tour:", sorted_tour)
print("Total travel cost:", total_cost)