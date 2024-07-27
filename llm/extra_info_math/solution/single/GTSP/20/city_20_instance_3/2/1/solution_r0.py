import pulp
import math

# Define the coordinates of each city
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Define the city groups
groups = [
    [4, 10, 13, 17],
    [6, 7, 14],
    [9, 12, 16],
    [2, 5, 15],
    [1, 3, 19],
    [8, 11, 18]
]

# Calculate Euclidean distance between two points
def distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create the problem variable to contain the problem data
prob = pulp.LpProblem("VRP", pulp.LpMinimize)

# A dictionary called 'vars' is created to contain the referenced variables (routes between cities)
vars = {(i, j): pulp.LpVariable(f"x_({i},{j})", cat='Binary') for i in cities for j in cities if i != j}

# Objective function
prob += pulp.lpSum(distance(cities[i], cities[j]) * vars[i, j] for i in cities for j in cities if i != j), "Total_Distance"

# Constraints
# Each group must have exactly one outgoing edge to a node outside the cluster
for group in groups:
    prob += sum(vars[i, j] for i in group for j in cities if j not in group) == 1

# Each group must have exactly one incoming edge from a node outside the cluster
for group in groups:
    prob += sum(vars[j, i] for i in group for j in cities if j not in group) == 1

# Flow conservation constraint for nodes, to maintain the tour, except the depot
for k in cities:
    if k != 0:
        prob += sum(vars[i, k] for i in cities if i != k) == sum(vars[k, j] for j in cities if j != k)

# Flow constraints specific for depot
prob += sum(vars[0, j] for j in cities if j != 0) == sum(vars[i, 0] for i in cities if i != 0)  # Equal in and out edges

# Solve the problem and print results
prob.solve()

# Fetching the results
tour = []
cost = 0
if pulp.LpStatus[prob.status] == 'Optimal':
    print("Optimal solution found!")
    # Calculate the tour route and the total travel cost
    visited = {0}
    current = 0
    while True:
        next_city = None
        for j in cities:
            if j != current and vars[current, j].varValue == 1:
                next_city = j
                break
        if next_city is None or next_city == 0:
            tour.append(0)
            break
        tour.append(next_city)
        cost += distance(cities[current], cities[next_city])
        current = next_city
else:
    print("Optimal solution not found.")

# Print the final tour and cost
print(f"Tour: {tour}")
print(f"Total travel cost: {cost:.2f}")