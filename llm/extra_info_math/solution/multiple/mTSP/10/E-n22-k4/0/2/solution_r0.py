import pulp
import math

# Define the coordinates of the cities
cities = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 185), 21: (139, 182)
}

# Number of robots
num_robots = 4
n = len(cities)  # Total nodes (including depot)
m = num_robots + 1

# Distance matrix using Euclidean distance
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create a dictionary of costs
cost = {(i, j): distance(i, j) for i in cities for j in cities if i != j}

# Define the problem using PuLP
problem = pulp.LpProblem("Multiple_TSP", pulp.LpMinimize)

# Decision variables: x_ijk
x = {(i, j, k): pulp.LpVariable(f"x_{i}_{j}_{k}", cat='Binary') 
     for i in cities for j in cities for k in range(num_robots) if i != j}

# Auxiliary variables: u_i
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0) for i in cities if i != 0}

# Objective function
problem += pulp.lpSum(cost[i, j] * x[i, j, k] for i in cities for j in cities for k in range(num_robots) if i != j)

# Constraints
# Each city is visited exactly once by one salesman
for j in cities:
    if j != 0:
        problem += pulp.lpSum(x[i, j, k] for i in cities for k in range(num_robots) if i != j) == 1

# Each salesman leaves and enters the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in cities if j != 0) == 1
    problem += pulp.lpSum(x[j, 0, k] for j in cities if j != 0) == 1

# Each salesman departs from and arrives at each node
for k in range(num_robots):
    for j in cities:
        if j != 0:
            problem += (pulp.lpSum(x[i, j, k] for i in cities if i != j) ==
                        pulp.lpSum(x[j, i, k] for i in cities if i != j))

# Subtour elimination
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            for k in range(num_robots):
                problem += u[i] - u[j] + n * x[i, j, k] <= n - 1

# Solve the problem using the CBC solver
problem.solve()

# Print the results
total_cost = 0
for k in range(num_robots):
    tour = [0]
    current_city = 0
    while True:
        next_city = next(j for j in cities if j != current_city and pulp.value(x[current_city, j, k]) == 1)
        tour.append(next_city)
        current_city = next_city
        if current_city == 0:
            break
    tour_cost = sum(cost[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    total_cost += tour_cost
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")