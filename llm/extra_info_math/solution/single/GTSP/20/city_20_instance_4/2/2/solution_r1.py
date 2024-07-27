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

# Variable: x_ij = 1 if travel from city i to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), 0, 1, pulp.LpBinary)

# Objective Function
objective = pulp.lpSum(cost306.25_matrix[i, j] * x[i, j] for i in cities for j in cities if i != j)
prob += objective

# Constraints: Each group should have exactly one outgoing and one incoming node
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in set(cities) - set(group)) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in set(cities) - set(group)) == 1

# Flow conservation constraint
for i in cities:
    prob += (pulp.lpSum(x[j, i] for j in cities if i != j) == pulp.lpSum(x[i, j] for j in cities if i != j))

# Solve the problem
prob.solve()

# Extract the solution
tour = [0]
current_city = 0

# Sequentially find the next city visited from each group
for _ in range(len(groups)):
    next_city = [j for j in cities if j != current_city and x[current_city, j].varValue == 1]
    if next_city:
        next_city = next_city[0]
        tour.append(next_city)
        current_city = next_city

# Return to depot if it's not a cyclic inclusion from the last node
if tour[-1] != 0:
    tour.append(0)

# Calculate the total travel cost
total_travel_cost = sum(cost_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost}")