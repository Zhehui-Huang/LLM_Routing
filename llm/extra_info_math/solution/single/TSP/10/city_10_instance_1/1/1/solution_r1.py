import pulp
import numpy as

# Define coordinates for each city, with city index 0 being the depot.
cities = {
    0: (53, 68),
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

# Total number of cities, including the depot
n = len(cities)

# Calculate Euclidean distance between two points
def euclidean_distance(pt1, pt2):
    return ((pt1[0] - pt2[0])**2 + (pt1[1] - pt2[1])**2)**0.5

# Cost matrix (travel cost between each pair of cities)
cost = {(i, j): euclidean_distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Initialize the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x[i, j] is 1 if travel from city i to city j is in the tour
x = pulp.LpVariable.dicts("x", cost.keys(), 0, 1, pulp.LpBinary)

# Objective function: Minimize total travel cost
prob += sum(x[i, j] * cost[i, j] for i, j in cost.keys())

# Constraint: each city (except depot) must be arrived at from exactly one other city
for j in range(n):
    prob += sum(x[i, j] for i in range(n) if i != j) == 1  # Arriving

# Constraint: from each city, one must travel to exactly one other city
for i in range(n):
    prob += sum(x[i, j] for j in range(n) if i != j) == 1  # Departing

# Solving the problem
prob.solve()

# Get resulting tour
tour = []
visited = [0]
while len(visited) < n:
    for i in range(n):
        if i not in visited:
            if x[visited[-1], i].varValue == 1:
                tour.append(i)
                visited.append(i)
                break

# Adding the depot to the beginning and end to complete the tour
tour = [0] + tour + [0]

# Calculate total travel cost
total_cost = sum(cost[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)