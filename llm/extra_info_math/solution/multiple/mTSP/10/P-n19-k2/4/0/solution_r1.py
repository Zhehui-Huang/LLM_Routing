import pulp
import math

# Coordinates of cities, including the depot
coords = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Number of Robots
m = 2
# Total number of nodes (including depot)
n = len(coords)

# Calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
c = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Create the optimization model
model = pulp.LpProblem("MultiVehicle_TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m)), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, cat='Continuous')

# Objective
model += pulp.lpSum(c[i][j] * x[i, j, k] for i in range(n) for j in range(n) for k in range(m))

# Constraints
# Each city is visited exactly once by exactly one salesman
for j in range(1, n):
    model += pulp.lpSum(x[i, j, k] for i in range(n) for k in range(m)) == 1

# Each salesman departs from and arrives at the depot
for k in range(m):
    model += pulp.lpSum(x[0, j, k] for j in range(1, n)) == 1
    model += pulp.lpSum(x[i, 0, k] for i in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for j in range(1, n):
        model += pulp.lpSum(x[i, j, k] for i in range(n)) - pulp.lpSum(x[j, i, k] for i in range(n)) == 0

# Subtour prevention
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                model += u[i] - u[j] + n*x[i, j, k] <= n - 1

# Solve the model
model.solve()

# Extract the tours
tours = []
for k in range(m):
    tour = []
    for node_start in range(n):
        if node_start == 0 or any([pulp.value(x[0, node_start, kr]) > 0.5 for kr in range(m)]):
            tour = [0]
            next_node = node_start
            while True:
                next_node = next(j for j in range(n) if pulp.value(x[next_node, j, k]) == 1)
                if next_node == 0:
                    break
                tour.append(next_node)
            tours.append(tour)
            break

# Calculate the tour costs
tour_costs = [sum(c[tours[k][i]][tours[k][i+1]] for i in range(len(tours[k])-1)) for k in range(len(tours))]
overall_cost = sum(tour_costs)

# Print the solutions
for idx, tour in enumerate(tours):
    print(f'Robot {idx} Tour: {tour}')
    print(f'Robot {idx} Total Travel Cost: {tour_costs[idx]}')
print(f'Overall Total Travel Cost: {overall||ular robot.solve()}')