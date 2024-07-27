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

num_cities = len(coordinates)
depots = 4
cities = list(range(num_cities))

# Calculate Euclidean distance matrix
cost_matrix = {}
for i in cities:
    for j in cities:
        if i != j:
            cost_matrix[(i, j)] = euclidean_distance(coordinates[i], coordinates[j])

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary') 
u = pulp.LpVariable.dicts("u", (i for i in cities), lowBound=0, cat='Continuous')

# Problem
prob = pulp.LpProblem("MDVRP", pulp.LpMinimize)
prob += pulp.lpSum(cost_matrix[i, j] * x[i, j] for i in cities for j in cities if i != j)

# Ensure each city is visited exactly once and left once
for j in cities:
    prob += pulp.lpSum(x[i][j] for i in cities if i != j and (i, j) in x) == 1
    prob += pulp.lpSum(x[j][i] for i in cities if i != j and (j, i) in x) == 1

# Subtour elimination
N = num_cities + 1  # Large number for subtour elimination 
for i in cities:
    for j in cities:
        if i != j and i < depots and (i, j) in x:
            prob += u[i] - u[j] + N * x[i][j] <= N - 1

# Solve the problem
solver_status = prob.solve(pulp.PULP_CBC_CMD(msg=0))

# Extracting the solution
routes = [[] for _ in range(depots)]
if pulp.LpStatus[solver_status] == 'Optimal':
    for k in range(depots):
        current_city = k
        while True:
            for j in cities:
                if j != current_city and pulp.value(x[current_city][j]) == 1:
                    routes[k].append(j)
                    current_city = j
                    break
            if current_city < depots:
                break

    # Reformatting output
    for d in range(depots):
        tour_path = [d] + routes[d]
        tour_cost = sum(cost_matrix[tour_path[i], tour_path[i + 1]] for i in range(len(tour_path) - 1))
        print(f"Robot {d} Tour: {tour_path}")
        print(f"Robot {d} Total Travel Cost: {tour_cost}")

    total_travel_cost = sum(pulp.value(prob.objective))
    print(f"Overall Total Travel Cost: {total_travel_cost}")
else:
    print("No optimal solution was found. Status:", pulp.LpStatus[solver_status])