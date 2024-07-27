import math
import pulp

# Coordinates of cities including the depot
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Function to calculate Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Calculate distances between each pair of cities
n = len(cities)
distances = { (i, j): distance(i, j) for i in range(n) for j in range(n) if i != j }

# Prepare the linear programming problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
z = pulp.LpVariable("z", lowBound=0)

# Minimize the maximum distance
model += z

# Constraints for maximum distance and connections
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1
    for j in range(n):
        if i != j:
            model += x[i, j] * distances[i, j] <= z

# Subtour prevention (MTZ constraints)
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n - 1) * x[i, j] <= n - 2

# Solve the problem
model.solve()

# Extract the results
tour = []
current_node = 0
sequence = [0]  # Start at the depot
while len(sequence) < n:
    next_nodes = [j for j in range(n) if j != current_node and pulp.value(x[current_node, j]) == 1]
    if next_nodes:
        next_node = next_nodes[0]
        sequence.append(next_node)
        current_node = next_node

sequence.append(0)  # Return to depot at end

total_cost = sum(distances[sequence[i], sequence[i+1]] for i in range(len(sequence) - 1))
max_distance = max(distances[sequence[i], sequence[i+1]] for i in range(len(sequence) - 1))

# Print the solution
print(f"Tour: {sequence}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")