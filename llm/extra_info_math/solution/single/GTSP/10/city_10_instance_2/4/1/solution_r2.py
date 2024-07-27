import math
import pulp

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
cities = {
    0: (90, 3),  # Depot
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
groups = [
    [3, 6], [5, 8], [4, 9], [1, 7], [2]
]

# Creating a problem instance
prob = pulp.LpProblem("Grouped_TSP", pulp.LpMinimize)

# Variables: x_ij for route selection
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective: Minimize total travel distance
distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}
prob += pulp.lpSum(x[(i, j)] * distances[(i, j)] for i in cities for j in cities if i != j])

# Constraints
# Only one visit to/from each group:
for group in groups:
    # Exactly one outgoing edge to nodes outside the group
    prob += pulp.lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1
    # Exactly one incoming edge from nodes outside the group
    prob += pulp.lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1

# Flow conservation at each city (not split into groups here because that can lead to incorrect constraints):
for i in cities:
    prob += pulp.lpSum(x[(j, i)] for j in cities if j != i) == pulp.lpSum(x[(i, j)] for j in cities if j != i)

# Solve the problem
prob.solve()

# Extract the tour from the variables
tour = []
next_city = 0
while True:
    tour.append(next_divct city if x[(next_cn city iin tL cities uj 1:t in
        if aCity v next_ne)t n cities up.variables.j, cvarValue == eighth (i v nexticitody) == fe.' \(tour + next{vtrx from the loop if rtingRa city acres the.Other end ed the edge allocated
ci ---- 
#Appendt makes the starting point
tour.append(0)

total_cost = sum(dist

# Print tour and cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")