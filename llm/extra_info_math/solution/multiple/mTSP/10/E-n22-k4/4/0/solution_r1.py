import pulp
import math

# City coordinates (including the depot)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Total number of cities including the depot
n = len(coordinates)
# Number of robots
m = 4

# Euclidean distance calculation function
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create cost matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Problem initialization
problem = pulp.LpProblem("Multiple_TSP_with_Robots", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, upBound=n-1, cat='Continuous')

# Objective function
problem += pulp.lpSum(cost[i][j] * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# Each city is visited exactly once by any salesman
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(m) if i != j) == 1

# Flow conservation and depot constraints
for k in range(m):
    problem += sum(x[(0, j, k)] for j in range(1, n)) == 1
    problem += sum(x[(j, 0, k)] for j in range(1, n)) == 1
    for p in range(1, n):
        problem += sum(x[(i, p, k)] for i in range(n) if i != p) - sum(x[(p, j, k)] for j in range(n) if j != p) == 0

# Subtour elimination constraints
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n-1) * x[(i, j, k)] <= n-2

# Solve the problem
problem.solve()

# Collecting results
for k in range(m):
    print(f"Robot {k} Tour:", end=" ")
    path = []
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[(i, j, k)]) == 1:
                path.append((i, j))
    
    # Order path to a readable format starting from the depot
    if path:
        ordered_path = [0]  # start at depot
        while path:
            for i, (a, b) in enumerate(path):
                if ordered_path[-1] == a:
                    ordered_owned_cost = pulp.value(cost[a][b])
                    ordered_path.append(b)
                    path.pop(i)
                    break
        ordered_path.append(0)  # return to depot
        print(ordered_path)

        # Calculate costs for robot
        tour_costs = sum(cost[ordered_path[i]][ordered_path[i + 1]] for i in range(len(ordered_path) - 1))
        print(f"Robot {k} Total Travel Cost: {tour_costs}")

# Calculate total cost
total_cost = sum(cost[ordered_path[i]][ordered_path[i + 1]] for i in range(len(ordered_path) - 1) for ordered_path in path)
print("Overall Total Travel Cost:", total_cost)