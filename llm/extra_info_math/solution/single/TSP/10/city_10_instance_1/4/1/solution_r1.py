import math
import pulp
import itertools

# Define the cities and their coordinates
coordinates = {
    0: (53, 68), 1: (75, 11), 2: (91, 95), 3: (22, 80), 4: (18, 63), 
    5: (54, 91), 6: (70, 14), 7: (97, 44), 8: (17, 69), 9: (95, 89)
}

def euclidean_distance(city1, city2):
    """Calculate the Euclidean distance between two cities"""
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

# Create the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

n = len(coordinates)
vars = pulp.LpVariable.dicts("x", (range(n), range(n)), lowBound=0, upBound=1, cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(vars[i][j] * euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j)

# Ensure each city is left exactly once
for i in range(n):
    problem += pulp.lpSum(vars[i][j] for j in range(n) if i != j) == 1

# Ensure each city is entered exactly once
for j in range(n):
    problem += pulp.lpSum(vars[i][j] for i in range(n) if i != j) == 1

# Subtour Elimination Constraints
for size in range(2, n):
    for subset in itertools.combinations(range(1, n), size):
        problem += (pulp.lpSum(vars[i][j] for i in subset for j in subset if i != j) <= len(subset) - 1)

# Solve the problem
problem.solve()

# Retrieve the solution
tour = []
for i in range(n):
    for j in range(n):
        if i != j and pulp.value(vars[i][j]) == 1:
            tour.append((i, j))

# Extract the ordered tour and calculate the total travel cost
ordered_tour = [0]
total_distance = 0

current_city = 0
while len(ordered_tour) < n:
    for (frm, to) in tour:
        if frm == current_city:
            total_distance += euclidean_distance(frm, to)
            ordered_tour.append(to)
            current_city = to
            break

# Ensure returning to the start city
total_distance += euclidean_distance(ordered_tour[-1], 0)
ordered_tandomise the circuit
ordered_tour.append(0)

print(f"Tour: {ordered_tour}")
print(f"Total travel cost: {round(total_distance, 2)}")