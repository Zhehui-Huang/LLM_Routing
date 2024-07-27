import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

# Define the groups
groups = [
    [5, 6, 16],
    [8, 18, 19],
    [11, 12, 13],
    [1, 3, 9],
    [2, 4, 14],
    [10, 17],
    [7, 15]
]

# Number of groups
k = len(groups)

# Total number of cities including depot
n = len(cities)

# Function to calculate the Euclidean distance
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Create the cost matrix
cost_matrix = {}
for i in cities:
    for j in cities:
        if i != j:
            cost_matrix[i, j] = euclidean_distance(cities[i], cities[j])

# Setup the problem
prob = pulp.LpProblem("GroupedTSP", pulp.LpMinimize)

# Variables: x_ij = 1 if travel from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), 0, 1, pulp.LpBinary)

# Objective Function
objective = pulp.lpSum(cost_matrix[i, j] * x[i, j] for i in cities for j in cities if i != j)
prob += objective

# Constraint: Each cluster must have exactly one outgoing and one incoming connection
for group in groups:
    # Outgoing
    prob += pulp.lpSum(x[i, j] for i in group for j in set(cities) - set(group)) == 1
    # Incoming
    prob += pulp.lpSum(x[j, i] for i in group for j in set(cities) - set(group)) == 1

# Constraint: Flow conservation to maintain the tour
for i in cities:
    prob += pulp.lpSum(x[i, j] for j in cities if (i, j) in x) == pulp.lpSum(x[j, i] for j in cities if (j, i) in x)

# Solve the problem
status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

# Output the results
if status == pulp.LpStatusOptimal:
    tour = []
    current_city = 0
    visited = set([0])
    tour.append(current_city)

    # Retrieve the tour
    for _ in range(7):  # Since it visits 1 city from each of 7 groups
        next_cities = [j for j in cities if j not in visited and x[current_city, j].value() == 1]
        if next_cities:
            current_city = next_cities[0]
            visited.add(current_city)
            tour.append(current_city)

    # Returning to the depot
    tour.append(0)

    # Calculate the total cost
    total_travel_cost = sum(cost_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cost:.2f}")
else:
    print("No feasible solution found.")