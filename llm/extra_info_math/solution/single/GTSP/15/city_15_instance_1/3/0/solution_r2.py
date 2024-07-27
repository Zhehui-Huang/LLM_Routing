import pulp
import math

# Define the city coordinates in a dictionary
city_coords = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Define the city groups
city_groups = [ 
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_coords[city2][0])**2 + 
                     (city_coords[city1][1] - city_coords[city2][1])**2)

# Generate all possible nodes and arcs
nodes = list(city_coords.keys())
arcs = [(i, j) for i in nodes for j in nodes if i != j]

# Create the LP problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if arc (i, j) is in the solution, 0 otherwise
x = pulp.LpVariable.dicts("x", arcs, cat=pulp.LpBinary)

# Objective Function: Minimize the sum of distances for the selected arcs
model += pulp.lpSum(x[i, j] * euclidean_distance(i, j) for i, j in arcs)

# Constraint: Enter each node exactly once
for group in city_groups:
    model += pulp.lpSum(x[i, j] for i in group for j in nodes if j not in group) == 1

# Constraint: Leave each node exactly once
for group in city_groups:
    model += pulp.lpSum(x[j, i] for i in group for j in nodes if j not in group) == 1

# Ensuring all nodes are connected into a single closed tour
for k in nodes[1:]:
    model += pulp.lpSum(x[i, k] for i in nodes if i != k) - pulp.lpSum(x[k, j] for j in nodes if j != k) == 0

# Solve the problem
model.solve()

# Retrieve the solution
tour = []
current_city = 0
total_cost = 0

# Follow the path according to the x variables
while len(tour) < len(city_groups) + 1:
    for j in nodes:
        if x[current_city, j].varValue == 1:
            tour.append(current_city)
            total_cost += euclidean_distance(current_city, j)
            current_city = j
            break

# Finally, append the return to the starting city
tour.append(current_city)
total_cost += euclidean_distance(current_city, tour[0])  # cost to return to the depot

print(f"Tour: {tour}")
print(f"Total Travel Cost: {total_cost:.2f}")