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
problem = pulp.LxProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Decision variables x_ij
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary')
     for i in coordinates for j in coordinates if i != j}

# Objective function
problem += pulp.lpSum(distances[i, j] * x[i, j] for i, j in x), "Total_Travel_Cost"

# Constraints for each group
for group in groups:
    other_cities = [i for i in coordinates if i not in group]
    problem += pulp.lpSum(x[j, i] for j in group for i in other_cities) == 1
    problem += pulp.lpSum(x[i, j] for j in group for i in other_cities) == 1

# Adding flow conservation constraints for all cities including depot
for i in coordinates:
    if i != 0:
        problem += (pulp.lpSum(x[j, i] for j in coordinates if i != j) ==
                    pulp.lpSum(x[i, j] for j in coordinates if i != j))

# Ensure that the depot also conforms to the flow constraint
problem += pulp.lpSum(x[0, j] for j in coordinates if j != 0) == len(groups)
problem += pulp.lpSum(x[j, 0] for j in coordinates if j != 0) == len(groups)

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=1))

# Checking if the problem was solved successfully
if status == pulp.LpStatusOptimal:
    tour = [0]
    current_city = 0
    for _ in range(len(coordinates) - 1):
        next_city = next(j for j in coordinates if j != current_city and pulp.value(x[current_city, j]) == 1)
        tour.append(next_city)
        current_city = next_city
    tour.append(0)  # Complete the tour by returning to the depot

    # Calculate the total distance traveled
    total_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))

    # Output results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("The optimization problem did not find an optimal solution.")