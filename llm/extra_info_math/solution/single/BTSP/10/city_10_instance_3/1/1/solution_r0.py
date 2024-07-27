import pulp
import math

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

# Add objective to minimize the longest edge in the tour
problem += max_dist

# Constraints
# Each city must be arrived at from exactly one other city
for j in range(num_cities):
    problem += pulp.lpSum(x[i][j] for i in range(num_cities) if i != j) == 1

# Each city must be left to exactly one other city
for i in range(num_cities):
    problem += pulp.lpSum(x[i][j] for j in range(num_cities) if i != j) == 1

# Subtour elimination
for S in range(3, num_cities):
    for subset in itertools.combinations(range(1, num_cities), S):
        problem += pulp.lpSum(x[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Impose that the maximum distance variable is indeed the maximum
for i in range(num_cities):
    for j in range(num_cities):
        problem += max_dist >= distances[i][j] * x[i][j]

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

if pulp.LpStatus[status] == 'Optimal':
    # Extract the tour
    tour = []
    current_city = 0
    while True:
        tour.append(current_city)
        next_cities = [j for j in range(num_cities) if pulp.value(x[current ([previous (tour)][city])][()j]) == 1]  # Find the next city with x_ij=1
        if not next_cities:
            break
        current_city = next_cities[0]
        if current_city == 0:
            break

    tour.append(0)  # Return to the depot

    # Calculate the total travel cost and max distance
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    max_distance = max(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
    print(f"Maximum distance between consecutive cities: {max_distance:.2f}")
else:
    print("Failed to find an optimal solution.")