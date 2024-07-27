import pulp
import math

# Calculate the Euclidean distance between two points
def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# City Coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Parameters
num_cities = len(coordinates)
num_robots = 4
depot = 0

# Create problem
prob = pulp.LpProblem("Vehicle_Routing_Problem", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(num_cities)
                               for j in range(num_cities) 
                               for k in range(num_robots)], cat='Binary')

u = pulp.LpVariable.dicts("u", range(num_cities), lowBound=0, cat='Continuous')

# Objective function - Minimize the maximum distance traveled by any robot
z = pulp.LpVariable("z", lowBound=0)
prob += z

# Define costs and add to objective
costs = {}
for i in range(num_cities):
    for j in range(num_cities):
        if i != j:
            costs[(i, j)] = calculate_distance(coordinates[i], coordinates[j])
            for k in range(num_robots):
                prob += x[i, j, k] * costs[i, j] <= z

# Constraints
# Each city is visited exactly once by one salesman
for j in range(1, num_cities):
    prob += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots)) == 1

# Flow conservation constraints for each robot and each city
for k in range(num_robots):
    for j in range(num_cities):
        prob += pulp.lpSum(x[i, j, k] for i in range(num_cities)) == \
                pulp.lpSum(x[j, i, k] for i in range(num_cities))

# Each robot leaves the depot
for k in range(num_robots):
    prob += pulp.lpSum(x[depot, j, k] for j in range(1, num_cities)) == 1

# Subtour elimination constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                prob += u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1

# Solve the problem
prob.solve()

# Output the results
tours = {k: [depot] for k in range(num_robots)}
costs = {k: 0 for k in range(num_robots)}
for k in range(num_robots):
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[i, j, k]) == 1:
                tours[k].append(j)
                costs[k] += calculate_distance(coordinates[i], coordinates[j])
    tours[k].append(depot)  # Return to depot

max_cost = max(costs.values())
for k in tours:
    print(f"Robot {k} Tour: {tours[k]}")
    print(f"Robot {k} Total Travel Cost: {costs[k]}")
print(f"Maximum Travel Travel Cost: {max_cost}")