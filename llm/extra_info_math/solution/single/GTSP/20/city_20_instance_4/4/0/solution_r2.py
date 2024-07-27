import pulp
import math

# Define the coordinates of the cities
coordinates = [
    (26, 60),  # Depot
    (73, 84), (89, 36), (15, 0), (11, 10),
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29),
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47),
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# Define the groups of cities
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
    [2, 4, 14], [10, 17], [7, 15]
]

# Calculate distances between each pair of cities
def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

distances = {(i, j): calculate_distance(coordinates[i], coordinates[j]) for i in range(20) for j in range(20) if i != j}

# Setup the problem
problem = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(20) for j in range(20) if i != j), cat='Binary')

# Objective
problem += pulp.lpSum(x[i, j] * distances[i, j] for i in range(20) for j in range(20) if i != j)

# Constraints for exact one exit and entry per group of city
for index, group in enumerate([[0]] + groups):
    problem += pulp.lpSum(x[i, j] for i in group for j in range(20) if j not in group and i != j) == 1, f"One_exit_from_group_{index}"
    problem += pulp.lpSum(x[j, i] for i in group for j in range(20) if j not in group and i != j) == 1, f"One_entry_to_group_{index}"

# Subtour prevention
u = pulp.LpVariable.dicts("u", range(1, 20), lowBound=0, upBound=len(coordinates)-1, cat='Integer')
for i in range(1, 20):
    for j in range(1, 20):
        if i != j:
            problem += u[i] - u[j] + (len(coordinates) - 1) * x[i, j] <= len(coordinates) - 2

# Solve the LP
problem.solve()

# Extract the solution
route = []
current_location = 0
steps_taken = 0  # To prevent infinite loops
while steps_taken < 20:
    next_step = next(j for j in range(20) if pulp.value(x[current_location, j]) == 1)
    route.append(next_step)
    current_location = next_reset = 1  # Go back to the depot if completing a cycle
    steps_taken += 1
    if next_step == 0:
        break
route.append(0)  # End at the depot

# Calculate the travel cost
travel_cost = sum(distances[route[i], route[i + 1]] for i in range(len(route) - 1))

# Provide the output
print("Tour:", route)
print("Total travel cost:", round(travel_cost, 2))