import pulp
import math

# Coordinates of cities
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Calculate euclidean distance matrix
def euclidean_distance(p1, p2):
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

# Number of cities and depots
num_cities = len(coordinates)
depots = 4  # Depots are from 0 to 3
cities = list(range(num_cities))

# Construct cost matrix
cost_matrix = {}
for i in cities:
    for j in cities:
        if i != j:
            cost_matrix[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

# Problem setup
prob = pulp.LpProblem("MDVRP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')  # travel from i to j
u = pulp.LpVariable.dicts("u", (i for i in cities), lowBound=0, cat='Continuous')  # Position in the tour

# Objective function
prob += pulp.lpSum(cost_matrix[i, j] * x[i, j] for i in cities for j in cities if i != j)

# Constraints
# Each city is visited exactly once
for j in cities[depots:]:
    prob += pulp.lpSum(x[i][j] for i in cities if i != j) == 1
    prob += pulp.lpSum(x[j][i] for i in cities if i != j) == 1

# Each robot leaves a depot
for i in range(depots):
    prob += pulp.lpSum(x[i][j] for j in cities if i != j) == 1

# Each robot is assigned to end at any city (not necessary a depot)
for i in range(depots):
    prob += pulp.lpSum(x[j][i] for j in cities if i != j) == 0

# Subtour elimination
for i in cities:
    for j in cities:
        if i != j and (i >= depots and j >= depots):
            prob += u[i] - u[j] + (num_cities) * x[i][j] <= num_cities - 1

# Solve the problem
status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

# Gather results
if pulp.LpStatus[status] == 'Optimal':
    tours = {k: [] for k in range(depots)}
    for i in cities:
        for j in cities:
            if i != j and pulp.value(x[i][j]) == 1:
                tours[i if i < depots else j if j < depots else None].append(j)
    
    # Reconstruct tours from edges and calculate costs
    for k in range(depots):
        path = [k]
        while len(path) <= num_cities // depots + 1:
            next_city = next(j for j in cities if pulp.value(x[path[-1], j]) == 1)
            path.append(next_city)
            if next_city < depots:
                break
        
        tour_cost = sum(cost_matrix[path[i], path[i + 1]] for i in range(len(path) - 1))
        print(f"Robot {k} Tour: {path}")
        print(f"Robot {k} Total Travel Cost: {tour_cost}")

    total_cost = pulp.value(prob.objective)
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No optimal solution available.")