import pulp
import math

# City coordinates
cities = {
    0: (90, 3),
    1: (11, 17),
    2: (7, 27),
    3: (95, 81),
    4: (41, 54),
    5: (31, 35),
    6: (23, 95),
    7: (20, 56),
    8: (49, 29),
    9: (13, 17)
}

# City groups
groups = {
    0: [3, 6],
    1: [5, 8],
    2: [4, 9],
    3: [1, 7],
    4: [2]
}

# Calculate Euclidean distance between two cities
def calculate_distance(id1, id2):
    x1, y1 = cities[id1]
    x2, y2 = cities[id2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Define the problem
prob = pulp.LpProblem("TSP_Variant_Minimal_Tour", pulp.LpMinimize)

# Variables: x_ij, whether travel from city i to city j occurs
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in cities for j in cities if i != j}

# Objective Function: Minimize the total travel cost
prob += pulp.lpSum(x[i, j] * calculate_distance(i, j) for i in cities for j in cities if i != j), "Total_Travel_Cost"

# Constraints for each group
for group in groups.values():
    # Exactly one outgoing edge to a node outside the group
    prob += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1

    # Exactly one incoming edge from a node outside the group
    prob += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

# Flow conservation for nodes (ensuring entering == leaving)
for k in cities:
    prob += pulp.lpSum(x[k, j] for j in cities if (k, j) in x) == pulp.lpSum(x[j, k] for j in cities if (j, k) in x)

# Solve the problem
status = prob.solve()
if status == pulp.LpStatusOptimal:
    print("Problem is successfully solved.")
else:
    print("Failed to find optimal solution.")

# Extracting the solution
tour = []
visited = {k: False for k in cities}
current_node = 0
tour.append(current_node)
visited[current_node] = True

# Following the path of the robot
while len(tour) < len(groups) + 1:
    for next_node in cities:
        if current_node != next_node and pulp.value(x[current_node, next_node]) == 1:
            tour.append(next_node)
            current_node = next_node
            break
# Adding the return to depot
tour.append(0)

# Calculate total travel cost from the tour
total_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Outputting the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")