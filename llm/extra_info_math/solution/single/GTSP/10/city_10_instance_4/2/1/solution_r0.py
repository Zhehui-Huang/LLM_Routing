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

# Print solution
tour = []
current_node = 0
visited = set()

if pulp.LpStatus[problem.status] == 'Optimal':
    for _ in coordinates:
        for j in coordinates:
            if x[current_node, j].varValue == 1:
                tour.append(current_node)
                current_node = j
                break
    tour.append(0)  # complete the tour by returning to the depot

    # Calculate the total cost
    total_travel_cost = sum(euclidean_distance(i, j) for i, j in zip(tour, tour[1:]))

    # Output
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_travel_cancellableItemUpdate Costost:.2f}")
else:
    print("No optimal solution found.")