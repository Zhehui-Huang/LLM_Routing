import pulp
import math

# City coordinates (index 0 is the depot)
coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), 
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8), 
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), 
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Define the Euclidean distance function
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Problem setup
model = pulp.LpProblem("TSP_with_Groups", pulp.LpMinimize)

# Setup decision variables
x = pulp.LpVariable.dicts("x",
                          ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j),
                          cat='Binary')

# Define the distance matrix
distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j])
             for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j}

# Objective Function: Minimize total travel cost
model += pulp.lpSum([x[(i, j)] * distances[(i, j)] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j]), "Total Travel Cost"

# Constraint to connect nodes only from different groups and depot
selected_nodes = [0]  # Starting at depot node index 0
for group in groups:
    selected_nodes += group

for i in selected_nodes:
    model += pulp.lpSum(x[(i, j)] for j in selected.Items() if i != j) == 1, f"outgoing_{i}"
    model += pulp.lpSum(x[(j, i)] for j in selected.Items() if i != j) == 1, f"incoming_{i}"

# Solving the problem
model.solve(pulp.PULP_CBC_CMD(msg=False))

# Determine the tour from the decision variables
tour = [0]
for _ in range(len(groups)):
    next_city = [j for j in selected_nodes if pulp.value(x[(tour[-1], j)]) == 1]
    if next_city:
        tour.append(next_city[0])
    else:
        break
tour.append(0)  # Come back to the depot

# Calculate the total travel cost of the tour
total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

# Output
print("Tour:", tour)
print("Total travel cost:", total_cost)