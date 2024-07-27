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
costs = {(i, j): calculate_distance(i, j) for i in cities for j in cities if i != j}
prob += pulp.lpSum(x[i, j] * costs[i, j] for i in cities for j in cities if i != j), "Total_Travel_Cost"

# Constraints for each group
for g, group in groups.items():
    prob += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1, f"One_outgoing_from_group_{g}"
    prob += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1, f"One_incoming_to_group_{g}"

# Flow conservation for nodes, ensuring entering == leaving
for k in cities:
    prob += pulp.lpSum(x[k, j] for j in cities if (k, j) in x) == pulp.lpSum(x[j, k] for j in cities if (j, k) in x), f"Flow_conservation_at_{k}"

# Solve problem
status = prob.solve()
if status == pulp.LpStatusOptimal:
    print("Problem solved successfully.")
    # Create a list to store the path
    tour = [0]
    # Find the tour path
    while len(tour) < len(groups) + 2:
        last = tour[-1]
        next_city = next(j for j in cities if j != last and pulp.value(x[last, j]) == 1)
        tour.append(next_city)

    # Calculate the total cost from the resultant tour
    total_cost = sum(costs[tour[i], tour[i+1]] for i in range(len(tour) - 1))

    # Print results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("Failed to solve the problem to optimality.")