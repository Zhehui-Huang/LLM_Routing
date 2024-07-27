import pulp
from math import sqrt

# Function to calculate Euclidean distance
def distance(i, j):
    x_i, y_i = cities[i]
    x_j, y_j = cities[j]
    return sqrt((x_i - x_j)**2 + (y_i - y_j)**2)

# Create the problem variable
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables: x[i][j] is 1 if we travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), 
                          cat='Binary')

# Auxiliary variable to minimize the maximum link distance
max_link = pulp.LpVariable("max_link", lowBound=0, cat='Continuous')

# Objective function: minimize the maximum length of any link in the tour
prob += max_link

# Constraints
for i in cities:
    # Exactly one edge leaves each city
    prob += sum(x[(i, j)] for j in cities if i != j) == 1
    # Exactly one edge enters each city
    prob += sum(x[(j, i)] for j in cities if i != j) == 1
# Max link constraint
for i in cities:
    for j in cities:
        if i != j:
            prob += x[(i, j)] * distance(i, j) <= max_link

# Subtour elimination constraints
subtours = []
for i in cities:
    for j in cities:
        if i != j:
            subtours.append([i, j])
prob += pulp.lpSum(x[edge] for edge in subtours if len(set(edge)) == len(edge)) <= len(cities) - 1

# Solve the problem
solver = pulp.getSolver('PULP_CBC_CMD')
status = prob.solve(solver)
    
if pulp.LpStatus[prob.status] == 'Optimal':
    # Get the optimal tour
    edges = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[(i, j)]) > 0.5]
    
    # Retrieve the cycle
    path = []
    current_location = 0
    while len(path) < len(cities):
        for j in cities:
            if (current_location, j) in edges:
                path.append(current_location)
                edges.remove((current_location, j))
                current_location = j
                break
    path.append(0)  # return to the starting city

    # Calculate the total distance and maximum link distance
    total_distance = sum(distance(path[i], path[i + 1]) for i in range(len(path) - 1))
    max_distance = max(distance(path[i], path[i + 1]) for i in range(len(path) - 1))

    # Print outputs
    print(f'Tour: {path}')
    print(f'Total travel cost: {total_distance}')
    print(f'Maximum distance between consecutive cities: {max_distance}')
else:
    print("No optimal solution found.")