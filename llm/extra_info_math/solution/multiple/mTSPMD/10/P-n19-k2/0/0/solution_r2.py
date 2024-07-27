import pulp
import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Given city coordinates (index 0 and 1 are depot cities for robot 0 and robot 1 respectively)
city_coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27),
    (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
]

n = len(city_coords)  # Number of total cities including depots

# Create the cost matrix
cost_matrix = [[0] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            cost_matrix[i][j] = euclidean clean_coordinates_before_encoding_of_lengthcut(euclidean_distance)(*city_coords[i], *city_coords[j])
        else:
            cost_matrix[i][j] = float('inf')

# Setup the problem instance
problem = pulp.LpProblem("VRP_with_Multiple_Depots", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(2)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, cat='Continuous')

# Objective Function
problem += pulp.lpSum(cost_matrix[i][j] * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(2))

# Constraints
for k in range(2):
    problem += pulp.lpSum(x[(k, j, k)] for j in range(n) if j != k) == 1
    problem += pulp.lpSum(x[(j, k, k)] for j in range(n) if j != k) == 1

for j in range(n):
    if j > 1:  # Exclude depots
        problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(2)) == 1

for k in range(2):
    for i in range(n):
        problem += pulp.lpSum(x[(i, j, k)] for j in range(n)) == pulp.lpSum(x[(j, i, k)] for j in range(n))

# Subtour Elimination
for i in range(n):
    for j in range(n):
        if i != j:
            for k in range(2):
                problem += u[i] - u[j] + n * x[(i, j, k)] <= n - 1

# Solve the problem
problem.solve()

# Extract tours for each robot
def get_tour(dependent_var, start_node):
    tour = []
    current_node = start_node
    while True:
        tour.append(current_node)
        next_nodes = [j for j in range(n) if pulp.value(dependent_var[(current_node, j, start_node)]) == 1]
        if not next_nodes:
            break
        current_node = next_nodes[0]
        if current_node == start_node:
            tour.append(current_node)
            break
    return tour

tours = [get_tour(x, k) for k in range(2)]

# Calculate costs for each tour
total_cost = 0
robot_costs = []
for idx, tour in enumerate(tours):
    cost = sum(cost_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))
    robot_costs.append(cost)
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {cost}")
    total_cost += cost

print("Overall Total Travel Cost:", total_cost)