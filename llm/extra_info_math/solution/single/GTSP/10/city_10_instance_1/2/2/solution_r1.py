from pulp import *
import math

# Define the coordinates of the depot and the cities
coordinates = {
    0: (53, 68),  # Depot
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

# Define city groups
city_groups = {
    0: [5, 6, 7],
    1: [2, 3],
    2: [1, 9],
    3: [4, 8]
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Calculate distances between every pair of cities
distances = {(i, j): euclidean_distance(i, j) for i in coordinates for j in coordinates if i != j}

# Create list of all nodes except the depot
nodes = list(coordinates.keys())[1:]

# Create a list of all possible edges
edges = [(i, j) for i in nodes for j in nodes if i != j]

# Initialize the problem
model = LpProblem("TSP_Group_Constraint", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", distances, 0, 1, LpBinary)

# Objective function: Minimize the total cost of travel
model += lpSum([distances[(i, j)] * x[(i, j)] for (i, j) in distances])

# Constraints for leaving and entering each group exactly once
for group in city_groups.values():
    model += lpSum([x[(i, j)] for i in group for j in coordinates if j not in group]) == 1  # Leaving each group
    model += lpSum([x[(j, i)] for i in group for j in coordinates if j not in group]) == 1  # Entering each group

# Flow conservation constraints
for k in nodes:
    model += lpSum([x[(i, k)] for i in coordinates if (i, k) in distances]) == lpSum([x[(k, j)] for j in coordinates if (k, j) in distances])

# Connect depot to the tour
model += lpSum([x[(0, j)] for j in nodes]) == 1
model += lpSum([x[(j, 0)] for j in nodes]) == 1

# Solve the problem
model.solve()

# Output tour and cost info
tour = [0]
while len(tour) < len(city_groups) + 1:
    for j in nodes:
        if x[(tour[-1], j)].varValue == 1:
            tour.append(j)
            break
tour.append(0)  # Return to the depot

total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)