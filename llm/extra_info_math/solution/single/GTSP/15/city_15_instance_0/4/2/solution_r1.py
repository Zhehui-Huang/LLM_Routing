import pulp
import math

# Define the function to calculate Euclidean distance between two points
def euclidean_distance(loc1, loc2):
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

# Given cities coordinates
locations = [
    (9, 93),   # Depot City 0
    (8, 51),
    (74, 99),
    (78, 50),
    (21, 23),
    (88, 59),
    (79, 77),
    (63, 23),
    (19, 76),
    (21, 38),
    (19, 65),
    (11, 40),
    (3, 21),
    (60, 55),
    (4, 39)
]

# Groups of cities
groups = [
    [0, 2, 7, 10, 11, 14],
    [0, 1, 3, 5, 8, 13],
    [0, 4, 6, 9, 12]
]

# Number of nodes
n = len(locations)

# Create distance matrix
distance_matrix = [[euclidean_distance(locations[i], locations[j]) for j in range(n)] for i in range(n)]

# Set up the problem variable to minimize total distance travelled
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables: x_ij = 1 if travel from i to j, else 0
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective: Minimize the total distance traveled
prob += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Each node must be entered and left exactly once
for j in range(n):
    prob += pulp.lpSum(x[i, j] for i in range(n) if i != j) == 1  # entering city j
    prob += pulp.lpSum(x[j, i] for i in range(n) if i != j) == 1  # leaving city j

# Subtour Elimination Constraints:
for group in groups:
    # Exclusive visit to one city from each group
    prob += pulp.lpSum(x[i, j] for i in group for j in range(n) if i != j and j not in group) == 1  # exactly one going from group
    prob += pulp.lpSum(x[j, i] for i in group for j in range(n) if i != j and j not in group) == 1  # exactly one coming to group

# Solve the problem using the solver
prob.solve()

# Output results
tour = []
current_location = 0
while True:
    tour.append(current_location)
    next_locations = [j for j in range(n) if j != current_location and pulp.value(x[current_location, j]) == 1]
    if not next_locations:
        break
    current_location = next_locations[0]

print("Tour:", tour)
print("Total travel cost:", sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1)))