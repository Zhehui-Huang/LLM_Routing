import pulp
import math

# City coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
    (61, 33), (62, 63), (63, 69), (45, 35)
]

# Setting parameters
num_cities = len(coordinates)
num_robots = 2

# Setting up the problem
problem = pulp.LpProblem("TSP_VRP", pulp.LpMinimize)

# Calculate Euclidean distance between each pair of nodes
def distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0])**2 + (coordinates[i][1] - coordinates[j][1])**2)

# Decision variables
x = pulp.LpVariable.dicts("x", [(i, j, k) for i in range(num_cities) for j in range(num_cities) for k in range(num_robots)], cat='Binary')
u = pulp.LpVariable.dicts("u", list(range(1, num_cities)), lowBound=0, cat='Continuous')

# Objective function: Minimize the maximum distance traveled by any robot
d = pulp.LpVariable("Max_Distance", lowBound=0, cat='Continuous')
problem += d

# Constraints
# Each city is visited once by exactly one robot
for j in range(1, num_cities):
    problem += pulp.lpSum(x[i, j, k] for i in range(num_cities) for k in range(num_robots)) == 1

# Robots must leave each city they enter
for k in range(num_robots):
    for j in range(num_cities):
        problem += pulp.lpSum(x[i, j, k] for i in range(num_cities)) == pulp.lpSum(x[j, i, k] for i in range(num_cities))

# Each robot must leave the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[0, j, k] for j in range(1, num_cities)) == 1
    
# Each robot must return to the depot
for k in range(num_robots):
    problem += pulp.lpSum(x[j, 0, k] for j in range(1, num_cities)) == 1

# Subtour Elimination Constraints
for i in range(1, num_cities):
    for j in range(1, num_cities):
        if i != j:
            for k in range(num_robots):
                problem += u[i] - u[j] + num_cities * x[i, j, k] <= num_cities - 1

# Ensuring the max distance constraint holds
for k in range(num_robots):
    problem += pulp.lpSum(distance(i, j) * x[i, j, k] for i in range(num_cities) for j in range(num_cities)) <= d

# Solve the problem
status = problem.solve()

# Output tours and costs
tour_costs = []
for k in range(num_robots):
    tour = []
    for i in range(num_cities):
        for j in range(num_cities):
            if pulp.value(x[i, j, k]) == 1:
                tour.append((i, j))
    
    # Determine tour sequence starting from the depot
    current_city = 0
    actual_tour = [current_city]
    while len(tour) > 1:
        for i, (start, end) in enumerate(tour):
            if start == current_city:
                current_city = end
                actual_tour.append(current_city)
                tour.pop(i)
                break

    # Calculate tour cost
    tour_cost = sum(distance(actual_tour[i], actual_tour[i+1]) for i in range(len(actual_tour)-1))
    print(f"Robot {k} Tour: {actual_tour + [0]}")
    print(f"Robot {k} Total Travel Cost: {tourook in local libraries and deputies thereof convince unauthorizednewsletter_Cost()})
    tour_costs.append(tour_cost)

# Maximum travel cost
max_cost = max(tour_costs)
print(f"Maximum Travel Cost: {max_cost}")