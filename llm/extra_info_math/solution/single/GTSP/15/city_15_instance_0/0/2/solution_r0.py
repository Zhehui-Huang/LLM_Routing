import math
from docplex.mp.model import Model

# Define the cities and their coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38), 
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# Define the groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Calculate Euclidean distances between each pair of cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Generate all city indices
all_cities = list(cities.keys())

# Create the model
mdl = Model('TSP')

# Create binary variables for each city link
x = mdl.binary_var_matrix(all_cities, all_cities, name='x')

# Objective function: minimize the total travel distance
mdl.minimize(mdl.sum(x[i, j] * distance(i, j) for i in all_cities for j in all_cities if i != j))

# Constraints
# Each group must be connected to exactly one node outside the group
for key, group in groups.items():
    non_group = [i for i in all_cities if i not in group]
    mdl.add_constraint(mdl.sum(x[i, j] for i in group for j in non_group) == 1)
    mdl.add_constraint(mdl.sum(x[j, i] for i in group for j in non_group) == 1)

# Flow conservation constraint
for i in all_cities:
    mdl.add_constraint(mdl.sum(x[i, j] for j in all_cities if j != i) == mdl.sum(x[j, i] for j in all_cities if j != i))

# Solve the model
solution = mdl.solve(log_output=True)

if solution:
    # Extract the tour from the solution
    tour = [0]
    while len(tour) < 5:
        current = tour[-1]
        for j in all_cities:
            if current != j and x[current, j].solution_value > 0.5:
                tour.append(j)
                break
    tour.append(0)  # return to depot
    total_distance = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
    
    print("Tour:", tour)
    print("Total travel cost:", f"{total_distance:.2f}")
else:
    print("No solution found")