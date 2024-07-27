import pulp
import math

# City coordinates
coordinates = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

# Grouping of cities
groups = {
    0: [1, 4],
    1: [2, 6],
    2: [7],
    3: [5],
    4: [9],
    5: [8],
    6: [3]
}

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# Define the problem
problem = pulp.LpProblem("Minimize_Travel_Cost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in coordinates for j in coordinates if i != j), cat='Binary')

# Objective Function
problem += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i in coordinates for j in coordinates if i != j)

# Constraints
# 1. Each group must have one outgoing and one incoming connection
for k, group in groups.items():
    problem += pulp.lpSum(x[i, j] for i in group for j in coordinates if j not in group) == 1  # outgoing
    problem += pulp.lpSum(x[j, i] for i in group for j in coordinates if j not in group) == 1  # incoming

# 2. Flow conservation at each city not the depot
for city in coordinates:
    if city != 0:
        problem += pulp.lpSum(x[c, city] for c in coordinates if c != city) == pulp.lpSum(x[city, c] for c in coordinates if c != city)

# Include depot start and end
problem += pulp.lpSum(x[0, j] for j in coordinates if j != 0) == 1  # only one edge leaving depot
problem += pulp.lpSum(x[j, 0] for j in coordinates if j != 0) == 1  # only one edge entering depot

# Solve the problem
problem.solve()

# Extracting the tour
tour = []
start = 0
current_node = start
num_cities = len(coordinates)
visited = set([current_node])

# All conditions for stopping the cycle are checked inside the loop
while len(tour) < num_cities:
    tour.append(current_node)
    next_nodes = [j for j in coordinates if x[current_node, j].varValue == 1]
    if not next_nodes:
        break
    current_node = next_nodes[0]
    visited.add(current_node)

tour.append(start)  # to return to start

# Calculate the total travel cost
total_travel_cost = sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")