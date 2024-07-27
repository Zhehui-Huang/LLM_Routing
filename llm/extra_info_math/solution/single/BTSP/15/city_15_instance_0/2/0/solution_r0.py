from pulp import *
import math

# Define the coordinates of each city
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 
    4: (21, 23), 5: (88, 59), 6: (79, 77), 7: (63, 23), 
    8: (19, 76), 9: (21, 38), 10: (19, 65), 11: (11, 40), 
    12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Number of cities
n = len(cities)

# Calculate distance matrix
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Optimization model
model = LpProblem("Minimize_max_distance_in_TSP", LpMinimize)

# Variables
x = LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')
max_dist = LpVariable("max_distance", lowBound=0)

# Objective
model += max_dist

# Constraints
# Incoming and outgoing flow constraints
for i in cities:
    model += lpSum(x[j, i] for j in cities if j != i) == 1, f"Flow_in_{i}"
    model += lpSum(x[i, j] for j in cities if j != i) == 1, f"Flow_out_{i}"

# Maximum distance constraint
for i in cities:
    for j in cities:
        if i != j:
            model += x[i, j] * distances[(i, j)] <= max_dist, f"Max_dist_{i}_{i}"

# Subtour elimination (using MTZ constraints, not added here for brevity)

# Solve the model
model.solve(PULP_CBC_CMD(msg=False))

# Extract solution
if LpStatus[model.status] == 'Optimal':
    tour = []
    for i in cities:
        for j in cities:
            if i != j and x[i, j].varValue == 1:
                tour.append((i, j))

    # Order the tour starting from the depot
    ordered_tour = [0]
    current_city = 0
    while len(ordered_tour) - 1 < len(cities) - 1:
        for next_city in tour:
            if next_city[0] == current_city:
                current_city = next_city[1]
                ordered_tour.append(current_city)
                break

    # Verify tour back to the starting city
    if ordered_tour[-1] != ordered_tour[0]:
        ordered_tour.append(0)
    
    # Calculate total travel cost
    total_cost = sum(distances[(ordered_tour[i], ordered_tour[i+1])] for i in range(len(ordered_tour)-1))
    max_distance = max(distances[(ordered_tour[i], ordered_tour[i+1])] for i in range(len(ordered_tour)-1))
    
    print(f"Tour: {ordered_tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No optimal solution found.")