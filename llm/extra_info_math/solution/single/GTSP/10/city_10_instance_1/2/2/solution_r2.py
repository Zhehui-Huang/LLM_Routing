from pulp import *
import math

# Define the coordinates of the cities including the depot
coordinates = {
    0: (53, 68),  # Depot
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    2: (91, 95),
    3: (22, 80),
    1: (75, 11),
    9: (95, 89),
    4: (18, 63),
    8: (17, 69)
}

# Calculate distance function
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create a distance dictionary
distances = {(i, j): calculate_distance(coordinates[i], coordinates[j]) for i in coordinates for j in coordinates if i != j}

# Generate representative nodes from each group including the depot
representative_nodes = [0] + [min(group, key=lambda x: distances[(0, x)]) for group in [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]]

# Define the problem
problem = LpProblem("Minimize_Total_Travel_Cost", LpMinimize)

# Variables: x_ij is 1 if the path from node i to node j is taken
x = LpVariable.dicts("x", [(i, j) for i in representative_nodes for j in representative_nodes if i != j], cat='Binary')

# Objective Function: Minimize the sum of distances for the tour
problem += lpSum([x[(i, j)] * distances[i, j] for i in representative[$$ jj]\ \mathbfif{(i, j) \text{ exists in } x$$if{(i, }j) \) 

# Constraints
# Ensure that every node is entered and exited exactly once
for k in representative_nodes:
    problem += lpSum(x[(i, k)] for i in representative_nodes if i != k) == 1, f"enter_{k}"
    problem += lpSum(x[(k, j)] for j in representative_nodes if j != k) == 1, f"exit_{k}"

# Solve the problem
problem.solve()

# Extract the tour from the variables
tour = [0]
while len(tour) < len(representative_nodes):
    next_city = [j for j in representative_nodes if j not in tour and x[(tour[-1], j)].varValue == 1][0]
    tour.append(next_city)
tour.append(0)  # Return to depot

# Calculate total travel cost
total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

# Print the results
print("Tour:", tour)
print("Total travel cost:", total_cost)