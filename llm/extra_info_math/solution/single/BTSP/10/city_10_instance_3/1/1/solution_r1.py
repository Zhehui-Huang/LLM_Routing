import pulp
import math
import itertools

# Provided city coordinates
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Calculate Euclidean distances between cities
def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2)

# Distance matrix
num_cities = len(cities)
distances = [[euclidean_distance(cities[i], cities[j]) for j in range(num_cities)] for i in range(num_cities)]

# Solving the TSP using PuLP
problem = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variable x_ij, where i, j are city indices
x = pulp.LpVariable.dicts("x", (range(num_cities), range(num_cities)), 0, 1, pulp.LpBinary)

# Dummy max variable for the objective
max_dist = pulp.LpVariable("max_dist", lowBound=0)

# Add objective to minimize the maximum distance
problem += max_dist

# Each city must be arrived at from exactly one other city
for j in range(num_cities):
    problem += pulp.lpSum(x[i][j] for i in range(num_cities) if i != j) == 1

# Each city must be left to exactly one other city
for i in range(num_cities):
    problem += pulp.lpSum(x[i][j] for j in range(num_cities) if i != j) == 1

# Subtour elimination (using Miller-Tucker-Zemlin formulation):
u = pulp.LpVariable.dicts("u", range(num_cities), 0, num_cities-1, pulp.LpInteger)
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            problem += u[i] - u[j] + num_cities * x[i][j] <= num_cities - 1

# Constraint to ensure that the max-dist variable is at least as large as every edge included in the tour
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            problem += max_dist >= distances[i][j] * x[i][j]

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Check if an optimal solution is found
if pulp.LpStatus[status] == 'Optimal':
    # Extract the tour from the decision variables
    tour = []
    current_city = 0
    for _ in range(num_cities):
        tour.append(current_city)
        next_cities = [j for j in range(num_cities) if pulp.value(x[current_city][j]) == 1]
        if not next_cities:
            break
        current_city = next_cities[0]
    tour.append(0) # Return to the depot

    # Calculate the total travel cost and max distance
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    # Display the output
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("Failed to find an optimal solution.")