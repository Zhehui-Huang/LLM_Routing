import pulp
import numpy as np

# Distance function
def distance(i, j):
    (x1, y1), (x2, y2) = cities[i], cities[j]
    return np.sqrt((x1 - x2)**2 + (y1 - y2)**2)

# City coordinates dictionary
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Create LP problem
model = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
max_dist = pulp.LpVariable("maximum_distance", lowBound=0, cat='Continuous')

# Objective
model += max_dist

# Constraints
for i in cities:
    model += pulp.lpSum(x[(i, j)] for j in cities if i != j) == 2*(i == 0)
    model += pulp.lpSum(x[(j, i)] for j in cities if i != j) == 2*(i == 0)

for i in cities:
    for j in cities:
        if i != j:
            model += x[(i, j)] * distance(i, j) <= max_dist

# Subtour Elimination Constraint (SEC)
def get_subtour(x):
    visited = []
    cycles = []
    lengths = []
    for start in x:
        if start not in visited:
            current = start
            cycle = [start]
            while True:
            # Follow the cycle until we return to the start
                visited.append(current)
                next_moves = [j for j in x if x[current, j].varValue > 0.5]
                current = next_moves[0]
                cycle.append(current)
                if current == start:
                    break
            lengths.append(len(cycle))
            cycles.append(cycle)
    return cycles[np.argmin(lengths)]

# Add subtour constraints
while True:
    solver = pulp.getSolver('PULP_CBC_CMD', msg=0)
    result = model.solve(solver)

    # Check if an optimal solution was found
    if pulp.LpStatus[model.status] != 'Optimal':
        print("No Optimal Solution Found")
        break

    # Check for subtours
    subtours = get_subtour(x)
    if len(subtours) == len(cities):
        break  # No subtours found, we are done
    # Add constraints to break subtours
    for subtour in subtours:
        if len(subtour) < len(cities):
            model += sum(x[i, j] for i in subtour for j in subtour if i != j) <= len(subtour) - 1

# Retrieve the results
tour = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[(i, j)]) > 0.5]
max_distance_value = pulp.value(max_dist)
total_cost = sum(distance(i, j) for i, j in tour)

# Find the tour in order-start_format
path = [0]
while len(path) < len(cities):
    next_city = [j for (i, j) in tour if i == path[-1] and j not in path][0]
    path.append(next_box)

# Print Results
print("Tour: ", path + [0])
print("Total travel cost: ", total_cost)
print("Maximum distance between consecutive cities: ", max_distance_value)