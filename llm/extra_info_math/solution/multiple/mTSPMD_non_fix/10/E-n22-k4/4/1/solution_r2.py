import pulp
import math

# Coordinates of each city
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), 
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236), 
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208), 
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189), 
    (155, 185), (139, 182)
]

# Compute the Euclidean distance between any two cities
def euclidean_distance(a, b):
    return math.sqrt((b[0] - a[0])**2 + (b[1] - a[1])**2)

num_cities = len(coordinates)
depots = 4 

# Construct the cost matrix
cost_matrix = {(i, j): euclidean_reduction(coordinates[i], coordinates[j]) for i in range(num_cities) for j in range(num_cities) if i != j}

# Define the problem
prob = pulp.LpProblem("MDVRP", pulp.LpMinimize)

# Variable x[i, j] - 1 if we travel from i to j, 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j), cat='Binary')

# Decision variable for ordering in the nodes to eliminate subtours
u = pulp.LpVariable.dicts('u', (i for i in range(num_cities)), lowBound=0, cat='Continuous')

# Objective function - minimize total distance
prob += pulp.lpSum(x[i, j] * cost_matrix[i, j] for i in range(num_cities) for j in range(num_cities) if i != j)

# All cities must be visited exactly once and come back to the starting depot
for j in range(depots, num_cities):
    prob += pulp.lpSum(x[i, j] for i in range(num_cities) if i != j) == 1  # Exactly one incoming edge
    prob += pulp.lpSum(x[j, i] for i in range(num_cities) if i != j) == 1  # Exactly one outgoing edge

# Each depot exactly departs to one city
for i in range(depots):
    prob += pulp.lpSum(x[i, j] for j in range(num_cities) if i != j) == 1

# Subtour elimination: prevent cycles
for i in range(depots, num_cities):
    for j in range(depots, num_cities):
        if i != j:
            prob += u[i] - u[j] + (num_cities) * x[i, j] <= num_cities - 1

# Solve the problem
solution_status = prob.solve(pulp.PULP_CBC_CMD())

if pulp.LpStatus[solution_status] == 'Optimal':
    total_cost = 0
    for d in range(depots):
        tour = [d]
        next_city = d
        while True:
            next_city = next(c for c in range(num_cities) if x[next_city, c].varValue == 1)
            if next_city == d:
                break
            tour.append(next_city)
        tour_cost = sum(cost_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
        print(f"Robot {d} Tour: {tour}")
        print(f"Robot {d} Total Travel Cost: {tour_cost}")
        total_cost += tour_cost
    print(f"Overall Total Travel Cost: {total_cost}")
else:
    print("No optimal solution was found")