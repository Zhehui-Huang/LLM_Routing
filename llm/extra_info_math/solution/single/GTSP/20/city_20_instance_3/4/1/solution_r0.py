import pulp
import math

# Define the cities and their coordinates
city_coords = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Define the groups
groups = {
    0: [4, 10, 13, 17],
    1: [6, 7, 14],
    2: [9, 12, 16],
    3: [2, 5, 15],
    4: [1, 3, 19],
    5: [8, 11, 18]
}

# Utility function to calculate Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create the problem
prob = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

k = len(groups) + 1  # including the depot
N = sum(len(v) for k, v in groups.items()) + 1  # all cities + depot

# Variable u for subtour elimination
u = pulp.LpVariable.dicts("u", range(k), lowBound=0, cat='Continuous')

# x_ij variables indicating if edge from i to j is used
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(N) for j in range(N) if i != j], 
                          cat="Binary", lowBound=0)

# Define edges and their costs
costs = {}
for i in range(N):
    for j in range(N):
        if i != j:
            if i in city_coords and j in city_coords:
                costs[(i, j)] = euclidean_distance(city_coords[i], city_coords[j])
                prob += x[(i, j)] * costs[(i, j)], "Cost_{}_{}".format(i, j)

# Objective function
prob += pulp.lpSum([x[(i, j)] * costs[(i, j)] for i in city_coords for j in city_coords if i != j]), "Total Travel Cost"

# Constraints
# Each group must connect to exactly one node outside the group
for p, nodes in groups.items():
    prob += pulp.lpSum([x[(i, j)] for i in nodes for j in range(N) if j not in nodes]) == 1
    prob += pulp.lpSum([x[(j, i)] for i in nodes for j in range(N) if j not in nodes]) == 1

# Flow conservation
for i in range(1, N):
    prob += pulp.lpSum([x[(j, i)] for j in range(N) if j != i]) == pulp.lpSum([x[(i, j)] for j in range(N) if i != j])

# Subtour elimination
for p in range(1, k):
    for q in range(1, k):
        if p != q:
            prob += (u[p] - u[q] + k * pulp.lpSum([x[(i, j)] for i in groups[p] for j in groups[q]]) +
                     (k - 2) * pulp.lpSum([x[(j, i)] for i in groups[p] for j in groups[q]]) <= k - 1)

# Solve the problem
prob.solve()

# Extracting the tour
tour = []
current_city = 0
tour.append(current_city)
# A simple extraction (might be improved to handle subtour cycles explicitly)
while True:
    next_cities = [j for j in range(N) if pulp.value(x[(current_city, j)]) == 1]
    if next_cities:
        next_city = next_cities[0]
        tour.append(next_city)
        current_city = next_city
        if next_city == 0:
            break

# Calculate total travel cost
total_cost = sum([costs[(tour[i], tour[i+1])] for i in range(len(tour)-1)])

print("Tour: ", tour)
print("Total travel cost: ", total_cost)