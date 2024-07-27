import pulp
from itertools import product
from math import sqrt

# Define the cities and their coordinates
coordinates = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80),
    4: (18, 63), 5: (54, 91), 6: (70, 14), 7: (97, 44),
    8: (17, 69), 9: (95, 89)
}

# Groups of cities
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Compute Euclidean distances between each pair of cities
def distance(i, j):
    return sqrt((coordinates[i][0] - coordinates[j][0])**2 +
               (coordinates[i][1] - coordinates[j][1])**2)

distances = {(i, j): distance(i, j) for i, j in product(coordinates.keys(), repeat=2) if i != j}

# Create the LP problem
problem = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Decision variables x_ij
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary')
     for i in coordinates for j in coordinates if i != j}

# Objective function
problem += pulp.lpSum(distances[i, j] * x[i, j] for i, j in x), "Total_Travel_Cost"

# Adding constraints to ensure exactly one city from each group is visited
for group in groups:
    other_cities = [i for i in coordinates if i not in group]
    # Exactly one outgoing edge to some city not in this group
    problem += pulp.lpSum(x[j, i] for j in group for i in other_cities) == 1
    # Exactly one incoming edge from some city not in this group
    problem += pulp.lpSum(x[i, j] for j in group for i in other_cities) == 1

# Flow conservation constraints, for each city exactly one incoming and one outgoing edge
for i in coordinates:
    if i != 0:
        problem += (pulp.lpSum(x[i, j] for j in coordinates if j != i) == 
                    pulp.lpSum(x[j, i] for j in coordinates if j != i), f"Flow conservation at {i}")

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Check if the problem was solved successfully
if pulp.LpStatus[status] != 'Optimal':
    print(f"An optimal solution could not be found, Status: {pulp.LpStatus[status]}")
else:
    # Extract tour from the result
    tour = []
    current_city = 0
    visited = set([0])
    tour.append(current_city)
    
    # Extracting the path
    while True:
        next_cities = [j for j in coordinates if j != current_city and pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        next_city = next_cities[0]
        if next_city in visited:
            break
        visited.add(next_city)
        tour.append(next_city)
        current_city = next_city
    
    # Close the tour back to the depot
    tour.append(0)

    # Calculate the total cost
    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

    # Output results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")