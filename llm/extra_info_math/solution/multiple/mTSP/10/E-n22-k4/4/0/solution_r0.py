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

n = len(coordinates)  # Total cities + depot
m = 4  # Number of robots

# Calculate Euclidean distance between any two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the cost matrix
cost = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(n)] for i in range(n)]

# Define the problem
problem = pulp.LpProblem("VRP_with_Robots", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j, k) for i in range(n) for j in range(n) for k in range(m) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(1, n)), lowBound=0, upBound=n-1, cat='Continuous')

# Objective
problem += pulp.lpSum(cost[i][j] * x[(i, j, k)] for i in range(n) for j in range(n) for k in range(m) if i != j)

# Constraints
# Every city is visited exactly once by one salesman
for j in range(1, n):
    problem += pulp.lpSum(x[(i, j, k)] for i in range(n) for k in range(m) if i != j) == 1

# Salesmen must leave the depot
for k in range(m):
    problem += pulp.lpSum(x[(0, j, k)] for j in range(1, n)) == 1

# Each salesman returns to depot
for k in range(m):
    problem += pulp.lpSum(x[(i, 0, k)] for i in range(1, n)) == 1

# Flow conservation
for k in range(m):
    for p in range(1, n):
        problem += (pulp.lpSum(x[(i, p, k)] for i in range(n) if i != p) -
                    pulp.lpSum(x[(p, j, k)] for j in range(n) if j != p)) == 0

# Subtour elimination
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            for k in range(m):
                problem += u[i] - u[j] + (n-1) * x[(i, j, k)] <= n-2

# Solve the problem
problem.solve()

# Output solution details
overall_total_cost = 0

for k in range(m):
    tour = [0]
    current_location = 0
    tour_cost = 0

    while True:
        next_city = None
        for j in range(n):
            if j != current_location and pulp.value(x[(current_location, j, k)]) == 1:
                next_city = j
                tour_cost += cost[current_location][next_city]
                break
        if next_city is None:
            break
        current_location = next_city
        tour.append(current_location)
        if current_location == 0:
            break
    
    tour.append(0)  # End the tour at the depot
    tour_cost += cost[current_location][0]

    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_data_cost}")

    overall_total_cost += tour_cost

print(f"Overall Total Travel Travel Cost: {overall_total_cost}")