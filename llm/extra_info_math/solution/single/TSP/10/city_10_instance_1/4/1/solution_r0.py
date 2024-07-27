import math
import pulp

# Define the cities and their coordinates
coordinates = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63), 
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities"""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

n = len(coordinates)  # Number of cities
vars = pulp.LpVariable.dicts("x", (range(n), range(n)), cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(vars[i][j] * euclidean_distance(i, j) for i in range(n) for j in range(n))

# Constraints
for i in range(1, n):
    problem += pulp.lpSum(vars[i][j] for j in range(n) if i != j) == 1  # exactly one departure from each city i
    problem += pulp.lpSum(vars[j][i] for j in range(n) if i != j) == 1  # exactly one arrival to each city i

# Subtour Elimination
for size in range(2, n):
    for subset in itertools.combinations(range(1, n), size):
        problem += (pulp.lpSum(vars[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1)

# Solve the problem using the default solver
status = problem.solve()

# Find the sequence from the result
tour = [0]
while len(tour) < n:
    for j in range(n):
        if pulp.value(vars[tour[-1]][j]) == 1:
            tour.append(j)
            break

# Append the start city to complete the circuit
tour.append(0)

# Calculate total distance of the tour
total_distance = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_distance}")