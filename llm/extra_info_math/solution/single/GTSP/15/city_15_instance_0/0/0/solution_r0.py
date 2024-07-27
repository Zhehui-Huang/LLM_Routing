import math
import pulp

# Helper function to calculate Euclidean distance between two points
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City coordinates
coordinates = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 5: (88, 59), 6: (79, 77),
    7: (63, 23), 8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 12: (3, 21),
    13: (60, 55), 14: (4, 39)
}

# Groups of cities
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Number of groups
k = 3

# Total number of cities including the depot
n = len(coordinates)

# Initialize the problem
problem = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Create variables x_ij for i, j in cities that denote whether path i to j is used
x = pulp.LpVariable.dicts("x", [(i, j) for i in coordinates for j in coordinates if i != j], cat='Binary')

# Objective function: Minimize the distance traveled
problem += pulp.lpSum(x[i, j] * euclidean_distance(coordinates[i], coordinates[j]) for i in coordinates for j in coordinates if i != j)

# Constraints:
# Ensure exactly one leaving and one entering edge from depot
problem += pulp.lpSum(x[0, j] for j in coordinates if j != 0) == 1
problem += pulp.lpSum(x[j, 0] for j in coordinates if j != 0) == 1

# For each group
for group in groups.values():
    # Ensure one selected city connects to outside and vice versa
    problem += pulp.lpSum(x[i, j] for i in group for j in coordinates if j not in group) == 1
    problem += pulp.lpSum(x[i, j] for j in group for i in coordinates if i not in group) == 1

# Solve the problem
problem.solve()

# Extract the tour and calculate the total distance
if pulp.LpStatus[problem.status] == 'Optimal':
    edges = [(i, j) for i in coordinates for j in coordinates if i != j and x[i, j].varValue == 1]
    # Initialize tour from the depot
    tour = [0]
    current_location = 0
    while len(tour) < 5:  # We know there will be 5 unique visits including depot
        next_locations = [j for i, j in edges if i == current_location and x[i, j].varValue == 1]
        if next_locations:
            current_location = next_locations[0]
            tour.append(current_location)
    # Close the tour by returning to the depot
    tour.append(0)
    
    # Calculate the distance
    total_distance = sum(euclidean_distance(coordinates[i], coordinates[j]) for i, j in edges)
    print("Tour:", tour)
    print("Total travel cost:", total_distance)
else:
    print("Failed to find a solution")