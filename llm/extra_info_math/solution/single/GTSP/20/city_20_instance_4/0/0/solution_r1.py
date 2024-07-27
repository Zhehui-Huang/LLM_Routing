import math
import pulp

# Coordinates of cities
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# City groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
    [2, 4, 14], [10, 17], [7, 15]
]

# Calculate distances
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

num_cities = len(coordinates)
distances = [[euclidean-distances(coordinates[i], coordinates[j]) for j in range(num_cities)] for i in range(num_cities)]

# Creating a flattened list of selectable nodes per group
group_nodes = {node for group in groups for node in group}
all_nodes = [0] + list(group_nodes)

# Define the LP problem as a minimization problem
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables, one for each possible direction travel
x = pulp.LpVariable.dicts("x", ((i, j) for i in all_nodes for j in all_nodes if i != j), cat='Binary')

# Adding the objective function
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in all_nodes for j in all_nodes if i != j), "Total_Distance"

# Constraints ensuring that one node per group including depot (0) is selected
for group in groups + [[0]]:
    prob += pulp.lpSum(x[i, j] for i in all_nodes for j in group if i != j) == 1, f"entry_{group}"
    prob += pulp.lpSum(x[j, i] for i in all_nodes for j in group if i != j) == 1, f"exit_{group}"

# Solving the LP problem
prob.solve()

# Output the results
tour = [0]
current_city = 0
sequential = 0  # To help exit the loop in a flawed logical condition

while len(tour) <= len(group_nodes) and sequential < 200:  # Limiting to prevent infinite loops, 200 as arbitrary limit for safety
    for j in all_nodes:
        if x[(current_city, j)].value() == 1:
            current_city = j
            tour.append(current_city)
            break
    sequential += 1

# Ensure the tour ends at the depot
tour.append(0)

# Calculate the total travel cost
total_distance = sum(distances[tour[n]][tour[n + 1]] for n in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_distance)