import math
import pulp

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

# Calculate Euclidean distance
def euclidean(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Prepare the LP problem
problem = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), 
                          cat='Binary')

# Objective function:
problem += pulp.lpSum(x[i, j] * euclidean(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraints:
# Each group must have one outgoing connection
for group in groups:
    problem += sum(x[i, j] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Each group must have one incoming connection
for group in groups:
    problem += sum(x[j, i] for i in group for j in range(len(coordinates)) if j not in group) == 1

# Conservation of flow constraints
for k in range(len(coordinates)):
    problem += sum(x[j, k] for j in range(len(coordinates)) if j != k) == sum(x[k, i] for i in range(len(coordinates)) if i != k)

# Solve the problem
problem.solve(pulp.PULP_CBC_CMD())

# Extract the tour
tour = []
for k in range(len(coordinates)):
    for j in range(len(coordinates)):
        if pulp.value(x[k, j]) == 1:
            tour.append((k, j))

# Formulate tour from variable output
final_tour = [0]
while len(final_tour) < len(groups) + 1:
    current_city = final_tour[-1]
    for (i, j) in tour:
        if i == current_city:
            final_tour.append(j)
            break
final_tour.append(0)  # Return to depot

# Calculate tour cost
tour_cost = sum(euclidean(final_tour[i], final_tour[i+1]) for i in range(len(final_tour) - 1))

print("Tour: ", final_tour)
print("Total travel cost: ", tour_cost)