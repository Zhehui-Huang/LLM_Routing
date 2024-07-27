import pulp
import math

# Define the city coordinates
city_coords = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Define city groups
city_groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Helper function to calculate Euclidean distance between cities
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost dictionary (distance between each pair of cities)
cost = {(i, j): calc_distance(city_coords[i], city_coords[j]) for i in city_coords for j in city_coords if i != j}

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("RobotMinimumDistanceTour", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in city_coords for j in cityelts if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum([cost[i, j] * x[i, j] for i in city_coords for j in city_coords if i != j])

# Constraints
for group in city_groups.values():
    problem += pulp.lpSum(x[i, j] for i in group for j in city_coords if j not in group) == 1
    problem += pulp.lpSum(x[j, i] for i in group for j in city_coords if j not in group) == 1

# Flow conservation constraints
for i in city_coords:
    problem += pulp.lpSum(x[j, i] for j in city_coords if j != i) == pulp.lpSum(x[i, j] for j in city_coords if j != i)

# Solve the problem
problem.solve()

# Extract tour
tour = []
visited = set()
current_node = 0
while True:
    next_node = next(j for j in city_coords if j != current_node and x[current_node, j].value() == 1)
    tour.append(current_node)
    visited.add(current_node)
    if next_node == 0:
        tour.append(next_node)
        break
    current_node = next_node

# Calculate total travel cost
total_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Output the results
print("Tour:", tour)
print("Total travel cost:", total_cost)