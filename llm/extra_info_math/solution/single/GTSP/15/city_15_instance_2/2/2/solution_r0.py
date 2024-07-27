import pulp
import math

# Helper function to calculate Euclidean distance
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Define the cities with their coordinates
cities = [
    (54, 87), (21, 84), (69, 84), (53, 40), (54, 42),
    (36, 30), (52, 82), (93, 44), (21, 78), (68, 14),
    (51, 28), (44, 79), (56, 58), (72, 43), (6, 99)
]

# Define the city groups
groups = [
    [8, 12, 14],
    [7, 10, 11],
    [4, 6, 9],
    [1, 3, 13],
    [2, 5]
]

# Number of total vertices and choosing vertices from each cluster + depot
total_nodes = 1 + sum(len(g) for g in groups)

# Adding depot to the groups
updated_groups = [[0]] + groups

# Problem definition
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(total_nodes) for j in range(total_nodes) if i != j), cat='Binary')

# Objective: Minimize the travel cost
costs = {}
for i in range(total_nodes):
    for j in range(total_nodes):
        if i != j:
            if i == 0:  # From depot
                ci = cities[0]
                cj = cities[updated_groups[j][0]]
            elif j == 0:  # To depot
                ci = cities[updated_groups[i][0]]
                cj = cities[0]
            else:
                ci = cities[updated_groups[i][0]]
                cj = cities[updated_groups[j][0]]
            costs[(i, j)] = distance(ci, cj)
            prob += x[(i, j)] * costs[(i, j)]

# Constraints
# Ensuring one city from each group is visited
for g in range(1, len(updated_groups)):
    prob += pulp.lpSum(x[(i, j)] for i in range(total_nodes) for j in range(total_nodes) if i in updated_groups[g] and j not in updated_groups[g]) == 1
    prob += pulp.lpSum(x[(j, i)] for i in range(total_nodes) for j in range(total_nodes) if i in updated_groups[g] and j not in updated_groups[g]) == 1

# Subtour elimination constraints are slightly complex and typically require additional auxiliary variables; let's define those
u = pulp.LpVariable.dicts('u', range(1, total_nodes), lowBound=0, upBound=total_nodes-1, cat='Continuous')

for i in range(1, total_nodes):
    for j in range(1, total_nodes):
        if i != j:
            prob += u[i] - u[j] + (total_nodes-1) * x[(i, j)] <= total_nodes - 2

# Solving the problem
prob.solve()

# Extracting the Solution
if pulp.LpStatus[prob.status] == 'Optimal':
    tour = [0]
    current = 0
    while True:
        next_city = None
        for j in range(total_nodes):
            if j != current and pulp.value(x[(current, j)]) == 1:
                next_city = j
                tour.append(j)
                current = j
                break
        if next_city == 0:
            break

    # Convert the tour to original city indices from selected group members
    final_tour = [0]  # Start at the depot
    for index in tour[1:]:
        real_index = updated_groups[index][0]
        final_tour.append(real_index)
    final_tour.append(0)  # Return to the depot

    # Calculate the total travel cost
    total_cost = sum(costs[(final_tour[i], final_tour[i+1])] for i in range(len(final_tour) - 1))

    print(f"Tour: {final_tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("No optimal solution found.")