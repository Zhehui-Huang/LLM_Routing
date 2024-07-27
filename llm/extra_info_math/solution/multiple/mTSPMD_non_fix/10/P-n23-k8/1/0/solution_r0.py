import pulp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
    (45, 35), (32, 39), (56, 37)
]

# Parameters
num_robots = 8
depots = list(range(7 + 1))  # Depots from city 0 to city 7
customer_nodes = list(range(8, 23))  # Customers from city 8 to city 22
nodes = depots + customer_nodes

# Calculate distances
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

distances = {(i, j): euclidean_distance(coordinates[i], coordinates[j]) for i in nodes for j in nodes if i != j}

# Linear programming model
model = pulp.LpProblem("VRP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in nodes for j in nodes if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in customer_nodes), lowBound=0, upBound=len(nodes), cat='Integer')

# Objective function
model += pulp.lpSum([distances[i, j] * x[i, j] for i in nodes for j in nodes if i != j])

# Constraints
# Only one tour ends at each node
for j in customer_nodes:
    model += pulp.lpSum([x[i, j] for i in nodes if (i, j) in x]) == 1

# Continuity of tours
for i in customer_nodes:
    model += pulp.lpSum([x[i, j] for j in nodes if (i, j) in x]) == 1

# Number of robots constraint
for d in depots:
    model += pulp.lpSum(x[d, j] for j in nodes if (d, j) in x) == (num_robots if d == 0 else 0)

# Sub-tour prevention
for i in customer_nodes:
    for j in customer_nodes:
        if i != j:
            model += u[i] - u[j] + (len(customer_nodes) * x[i, j]) <= len(customer_nodes) - 1

# Solve the model
model_status = model.solve()

# Retrieve results
tours = {r: [] for r in range(num_robots)}
robot = 0
for d in depots:
    current = d
    if model.value(x[d, d]) == 1:  # Only proceed if the tour starts here
        while True:
            next_city = next(j for j in nodes if model.value(x[current, j]) == 1)
            tours[robot].append(current)
            current = next_city
            if current == d:
                tours[robot].append(current)
                break
        robot += 1

# Printing the results
overall_cost = 0
for robot, tour in tours.items():
    tour_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour) - 1))
    overall_cost += tour_cost
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_cost}")