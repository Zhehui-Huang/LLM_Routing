import pulp
from math import sqrt

# City coordinates
coordinates = [
    (79, 15),  # City 0: Depot
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Groups of cities
groups = [
    [1, 4],
    [2, 6],
    [7],
    [5],
    [9],
    [8],
    [3]
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(idx1, idx2):
    return sqrt((coordinates[idx1][0] - coordinates[idx2][0]) ** 2 + (coordinates[idx1][1] - coordinates[idx2][1]) ** 2)

# List of all cities including the depot
all_nodes = [0] + [node for group in groups for node in group]
distances = {(i, j): euclidean 	    distance(i, j) for i in all_nodes for j in all_nodes if i != j}

# Create the problem
problem = pulp.LpProblem("Minimum_Cost_Tour", pulp.LpMinimize)

# Decision variables: x[i,j] is 1 if the path from city i to city j is chosen
x = pulp.LpVariable.dicts("x", distances.keys(), cat="Binary")

# Objective function: Minimize the total distance travelled
problem += pulp.lpSum(x[(i, j)] * distances[(i, j)] for i, j in distances.keys()), "Total_Distance"

# Constraint: Enter each group exactly once
for group in groups:
    problem += pulp.lpSum(x[(i, j)] for i in group for j in all_nodes if j not in group) == 1

# Constraint: Exit each group exactly once
for group in groups:
    problem += pulp.lpSum(x[(j, i)] for i in group for j in all_nodes if j not in group) == 1

# Subtour prevention: Only allow one outgoing connection from every node
for node in all_nodes:
    problem += pulp.lpSum(x[(node, j)] for j in all_nodes if (node, j) in x) == 1

# Subtour prevention: Only allow one incoming connection to every node
for node in all_nodes:
    problem += pulp.lpSum(x[(i, node)] for i in all_nodes if (i, node) in x) == 1

# Solve problem
problem.solve()

# Output the tour
tour = [0]
current_city = 0

while True:
    next_cities = [(current_city, j) for j in all_nodes if (current_city, j) in x and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0][1]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

total_cost = sum(distances[(tour[i], tour[i+1])] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", round(total_cost, 2))