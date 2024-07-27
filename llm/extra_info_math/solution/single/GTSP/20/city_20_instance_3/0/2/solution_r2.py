import pulp
import math

# City positions
positions = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47),
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# City groups plus the depot
groups = [
    [0],                # Depot (treated as a single-group cluster)
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Output number of positions and groups length (to ensure we are correct in our assumptions)
print("Positions:", len(positions), "Groups:", len(groups))

# Functions to calculate Euclidean distance
def euclidean(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# Create cost matrix
n = len(positions)
cost_matrix = {}
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[(i, j)] = euclidean(positions[i], positions[j])

# Define the problem
prob = pulp.LpProblem("Min_Cost_TSP", pulp.LpMinimize)

# Decision Variable
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(n) for j in range(n) if i != j], cat='Binary')

# Objective Function: Minimize the sum of travel costs between selected cities in the tour
prob += pulp.lpSum(cost_matrix[i, j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraint: Enter and leave each represented group exactly once
for group in groups:
    # Enter each group once
    prob += pulp.lpSum(x[i, j] for i in range(n) if any(i in g for g in groups) for j in group) == 1
    # Leave each group once
    prob += pulp.lpSum(x[i, j] for i in group for j in range(n) if any(j in g for g in groups)) == 1

# Solve the optimization problem
status = prob.solve()
if pulp.LpStatus[prob.status] == "Optimal":
    tour_edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]
    # Extract tour path from the decision variables
    city = 0  # starting and ending at the depot
    tour = [city]
    while len(tour_edges) > 0:
        for i, j in tour_edges:
            if i == city:
                tour.append(j)
                city = j
                tour_edges.remove((i, j))
                break

    print("Tour:", tour)
    total_travel_cost = sum(cost_matrix[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    print("Total travel cost:", round(total_travel_cost, 2))
else:
    print("No optimal solution found.")