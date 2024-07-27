import pulp
import math

# City positions as given
positions = [
    (35, 40), # City 0 (Depot)
    (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47),
    (41, 74), (53, 80), (21, 21), (12, 39)
]

# Grouping of cities as given
groups = [
    [3, 8], # Group 0
    [4, 13], # Group 1
    [1, 2], # Group 2
    [6, 14], # Group 3
    [5, 9], # Group 4
    [7, 12], # Group 5
    [10, 11] # Group 6
]

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0])**2 + (pos1[1] - pos2[1])**2)

distances = {}
for i, pos1 in enumerate(positions):
    for j, pos2 in enumerate(positions):
        if i != j:
            distances[(i, j)] = euclidean_distance(pos1, pos2)

# Integer programming model
model = pulp.LpProblem("TSP_Group_Selection", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(positions)) for j in range(len(positions)) if i != j), cat='Binary')

# Objective: Minimize total travel cost
model += pulp.lpSum(distances[(i, j)] * x[(i, j)] for i in range(len(positions)) for j in range(len(positions)) if i != j)

# Constraints
# Each group must send and receive exactly 1 link outside of its group
for group in groups:
    # Outgoing links exactly 1
    model += pulp.lpSum(x[(i, j)] for i in group for j in range(len(positions)) if j not in group) == 1
    # Incoming links exactly 1
    model += pulp.lpSum(x[(j, i)] for i in group for j in range(len(positions)) if j not in group) == 1

# Flow conservation for depot city
model += pulp.lpSum(x[(0, j)] for j in range(1, len(positions))) == 1 # Leaving depot
model += pulp.lpSum(x[(j, 0)] for j in range(1, len(positions))) == 1 # Coming back to depot

# Subtour Elimination Constraints using Miller-Tucker-Zemlin approach:
u = pulp.LpVariable.dicts("u", range(1, len(positions)), lowBound=0, cat='Continuous')

# Subtour constraints for the connection besides depot
for i in range(1, len(positions)):
    for j in range(1, len(positions)):
        if i != j:
            model += u[i] - u[j] + (len(positions) - 1) * x[(i, j)] <= len(positions) - 2

# Solve the problem
status = model.solve()

# Gather results
if status == pulp.LpStatusOptimal:
    tour = [0]
    current_position = 0
    while len(tour) < (num_groups + 1):  # Since we have 7 groups and 1 return to depot
        for j in range(len(positions)):
            if x[(current_position, j)].varValue == 1:
                tour.append(j)
                current_position = j
                break
    tour.append(0)  # Return to the depot
    total_cost = pulp.value(model.objective)

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("The problem is not optimal or no solution was found.")