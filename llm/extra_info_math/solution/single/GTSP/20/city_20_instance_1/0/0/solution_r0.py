import pulp
import math

# City coordinates
coordinates = [
    (14, 77),  # Depot 0
    (34, 20),  # 1
    (19, 38),  # 2
    (14, 91),  # 3
    (68, 98),  # 4
    (45, 84),  # 5
    (4, 56),   # 6
    (54, 82),  # 7
    (37, 28),  # 8
    (27, 45),  # 9
    (90, 85),  # 10
    (98, 76),  # 11
    (6, 19),   # 12
    (26, 29),  # 13
    (21, 79),  # 14
    (49, 23),  # 15
    (78, 76),  # 16
    (68, 45),  # 17
    (50, 28),  # 18
    (69, 9)    # 19
]

# City groups
groups = [
    [5, 6, 7, 11, 17],    # Group 0
    [1, 4, 8, 13, 16],    # Group 1
    [2, 10, 15, 18, 19],  # Group 2
    [3, 9, 12, 14]        # Group 3
]

# Number of cities (including depot)
num_cities = len(coordinates)
# Total groups
num_groups = len(groups)

# Calculate Euclidean distances
def euclidean(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Cost matrix
cost_matrix = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            cost_matrix[(i, j)] = euclidean(i, j)

# Create the LP problem
problem = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j),
                          cat='Binary')

# Objective function
problem += pulp.lpSum(cost_matrix[i, j] * x[i, j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Add constraints
# Exactly one city in each group can have a path exiting and entering the group
for group in groups:
    problem += pulp.lpSum(x[i, j] for i in group for j in range(num_cities) if j not in group) == 1
    problem += pulp.lpSum(x[j, i] for i in group for j in range(num_cities) if j not in group) == 1

# Conservation of flows for depots and cities
for i in range(num_cities):
    problem += (pulp.lpSum(x[j, i] for j in range(num_cities) if j != i) -
                pulp.lpSum(x[i, j] for j in range(num_cities) if j != i)) == 0

# Solve the problem using a suitable solver
problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Extract solution
tour = []
visited = set()
current = 0
while True:
    visited.add(current)
    tour.append(current)
    next_city = next(j for j in range(num_cities) if j != current and pulp.value(x[current, j]) == 1)
    if next_city == 0:
        tour.append(next_city)
        break
    current = next_city

# Calculate total cost
total_cost = sum(cost_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Display the tour and total travel cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")