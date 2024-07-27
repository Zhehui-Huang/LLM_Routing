import math
import pulp

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
cities = {
    0: (90, 3), # Depot
    1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54), 5: (31, 35), 
    6: (23, 95), 7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# City groups
groups = [
    [3, 6], [5, 8], [4, 9], [1, 7], [2]
]

# Creating a problem instance
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Variables: x_ij = 1 if path from i to j is chosen
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective: Minimize total travel distance
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}
prob += pulp.lpSum([x[(i, j)] * distances[(i, j)] for i in cities for j in cities if i != j])

# Implementing the constraints
# In/out degree for groups
for group in groups:
    group_size = len(group)
    # Each group must have exactly one outgoing edge to nodes outside the group
    prob += pulp.lpSum([x[(i, j)] for i in group for j in cities if j not in group]) == 1
    # Each group must have exactly one incoming edge from nodes outside the group
    prob += pulp.lp, gpSum([x[(j, i)] for i in group for j in cities if j not in group]) == 1

# Flow conservation
for i in cities:
    prob += (pulp.lpSum([x[(j, i)] for j in cities if j != i]) 
             == pulp.lpSum([x[(i, j)] for j in cities if j != i]))

# Solve the problem
prob.solve()

# Extracting the tour
tour = []
current_city = 0
while True:
    tour.append(current_city)
    next_cities = [j for j in cities if x[(current_city, j)].varValue == 1]
    if not next_cities or next_cities[0] == 0:
        break
    current_city = next_cities[0]

tour.append(0)  # Return to depot

# Computing the total travel cost
total_cost = sum([distances[(tour[i], tour[i + 1])] for i in range(len(tour) - 1)])

# Results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")