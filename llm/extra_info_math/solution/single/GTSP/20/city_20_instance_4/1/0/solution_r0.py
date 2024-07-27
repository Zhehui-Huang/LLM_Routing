import pulp
import math
from itertools import product

# City Coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), 
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), 
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# City Groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9], 
    [2, 4, 14], [10, 17], [7, 15]
]

# Total number of cities (including the depot)
num_cities = len(coordinates)

def euclidean_distance(coords1, coords2):
    """Calculate Euclidean distance between two points."""
    return math.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)

# Distance matrix
distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)] 
             for i in range(num_cities)]

# Problem setup
prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Defining decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), 
                          cat='Binary')

# Objective function
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints
# Each group must have exactly one outgoing edge to a node outside the cluster
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in range(num_cities) if j not in group) == 1

# Each group must have exactly one incoming edge from a node outside the cluster
for group in groups:
    prob += pulp.lpSum(x[j, i] for i in group for j in range(num_cities) if j not in group) == 1

# Flow conservation constraint
for i in range(1, num_cities):
    prob += pulp.lpSum(x[j, i] for j in range(num_cities) if j != i) == pulp.lpSum(x[i, j] for j in range(num_cities) if j != i)

# Subtour constraints
u = pulp.LpVariable.dicts("u", (i for i in range(1, num_cities)), lowBound=0, cat='Continuous')
k = num_cities
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            prob += u[i] - u[j] + k * x[i, j] <= k - 1

# Solving the problem
status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

# Extracting results
tour = []
current = 0
visited = set([0])
tour_cost = 0

for _ in range(num_cities):
    found = False
    for j in range(num_cities):
        if x[current, j].varValue > 0.5 and j not in visited:
            tour_cost += distances[current][j]
            tour.append(j)
            visited.add(j)
            current = j
            found = True
            break
    if not found:
        break

tour = [0] + tour + [0]
tour_cost += distances[tour[-2]][0]  # Adding the cost to return to the depot

# Output the tour and total cost
print(f'Tour: {tour}')
print(f'Total travel cost: {tour_cost}')