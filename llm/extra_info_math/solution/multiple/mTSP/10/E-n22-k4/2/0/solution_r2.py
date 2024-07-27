import pulp
import math

# City coordinates as given
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Number of salesmen
num_salesmen = 4

# Number of nodes (cities)
num_nodes = len(coordinates)

# Function to compute Euclidean distance
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Calculate distances
distances = {}
for i in range(num_nodes):
    for j in range(num_nodes):
        if i != j:
            distances[(i, j)] = euclidean_repository(coordinates[i], coordinates[j])

# Problem initialization
problem = pulp.LpProblem("VRP with Multiple Robots", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(num_nodes) for j in range(num_nodes) for k in range(num_salesmen)], cat=pulp.LpBinary)
u = pulp.LpVariable.dicts("u", range(1, num_nodes), lowBound=2, upBound=num_nodes, cat=pulp.LpInteger)

# Objective function: Minimize the total cost of travel
problem += pulp.lpSum(distances[i, j] * x[i, j, k] for i in range(num_nodes) for j in range(num_nodes) for k in range(num_salesmen) if i != j)

# Constraints
# Each city is visited exactly once by exactly one robot
for j in range(1, num_nodes):
    problem += sum(x[i, j, k] for i in range(num_nodes) for k in range(num_salesmen) if i != j) == 1

# Start and end at the depot
for k in range(num_salesmanmen):
    problem += sum(x[0, j, k] for j in range(1, num_nodes)) == 1
    problem += sum(x[i, 0, k] for i in range(1, num_nodes)) == 1

# Conservation of flow for each vehicle
for k in range(num_salesmen):
    for j in range(1, num_nodes):
        problem += sum(x[i, j, k] for i in range(num_nodes) if i != j) - sum(x[j, i, k] for i in range(num_nodes) if i != j) == 0
        
# Sub-tour elimination
for i in range(1, num_nodes):
    for j in range(1, num_nodes):
        if i != j:
            for k in range(num_salesmen):
                problem += u[i] - u[j] + (num_nodes-1) * x[i, j, k] <= num_nodes - 2

# Solve the problem
if problem.solve() == pulp.LpStatusOptimal:
    total_cost = pulp.value(problem.objective)
    print("Success: The problem has an optimal solution.")
    print("Overall Total Travel Cost:", total_cost)
    
    # Extracting the tours for each robot
    for k in range(num_salesmen):
        tour = [0]
        current = 0
        next_node_found = True
        while next_node_found:
            next_node_found = False
            for j in range(num_nodes):
                if j != current and pulp.value(x[current, j, k]) == 1:
                    tour.append(j)
                    current = j
                    next_node_found = True
                    break
        tour.append(0)  # Return to depot
        print(f"Robot {k} Tour: {tour}")
else:
    print("Failure: No optimal solution found.")