import math
import itertools
from pulp import LpProblem, LpMinimize, LpVariable, lpSum, LpBinary, PULP_CBC_CMD

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
problem = LpProblem("TSP", LpMinimize)

n = len(coordinates)
vars = LpVariable.dicts("x", (range(n), range(n)), cat=LpBinary)

# Objective function
problem += lpSum(vars[i][j] * euclidean_distance(i, j) for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    problem += lpSum(vars[i][j] for j in range(n) if i != j) == 1
    problem += lpSum(vars[j][i] for j in range(n) if i != j) == 1

# Subtour Elimination Constraints
for size in range(2, n):
    for subset in itertools.combinations(range(n), size):
        problem += lpSum(vars[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
problem.solve(PULP_CBC_CMD(msg=0))

# Find the sequence from the result
tour = []
visited = [0]
current = 0

while len(visited) < n:
    next_cities = [j for j in range(n) if j not in visited and vars[current][j].varValue == 1]
    if next_cities:
        next_city = next_cities[0]
        tour.append((current, next_city))
        visited.append(next_city)
        current = next_city

# Close the tour by returning to the start city
tour.append((current, 0))

# Calculate the total distance
total_distance = sum(euclidean_distance(i, j) for i, j in tour)

# Convert the list of tuples to a list of indices for the tour
tour_indices = [i for i, _ in tour] + [0]

print(f"Tour: {tour_indices}")
print(f"Total travel code