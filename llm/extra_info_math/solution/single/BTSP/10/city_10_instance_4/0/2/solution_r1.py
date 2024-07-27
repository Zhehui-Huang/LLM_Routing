import pulp
import math

# City coordinates
cities = {
    0: (79, 15),
    1: (79, 55),
    2: (4, 80),
    3: (65, 26),
    4: (92, 9),
    5: (83, 61),
    6: (22, 21),
    7: (97, 70),
    8: (20, 99),
    9: (66, 62)
}

n = len(cities)  # Number of cities including depot

# Function to calculate Euclidean distance between two cities
def euclidean_distance(a, b):
    return math.sqrt((cities[a][0] - cities[b][0])**2 + (cities[a][1] - cities[b][1])**2)

# Distance matrix
distance = {(i, j): euclidean_distance(i, j) for i in range(n) for j in range(n) if i != j}

# Setting up the problem: Minimize the maximum distance traveled between two consecutive cities
prob = pulp.LpProblem("Minimax_TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Variable to minimize (maximum distance between any two consecutive cities)
max_dist = pulp.LpVariable("max_dist")

# Objective
prob += max_dist

# Constraints
# Each city must be left exactly once
for i in range(n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Each city must be entered exactly once
for j in range(n):
    prob += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += x[(i, j)] * distance[(i, j)] <= max_dist

# Solve the problem
status = prob.solve(pulp.PULP_CBC_CMD(msg=1))

# Checking the solution and gathering results
tour = [0]  # start at the depot
current_city = 0
total_cost = 0
max_cost = 0

# Forming the tour from the decision variables
for _ in range(n-1):
    next_city = next(j for j in range(n) if j != current_city and pulp.value(x[(current_city, j)]) == 1)
    tour.append(next_city)
    travel_cost = distance[(current_city, next_city)]
    total_cost += travel_cost
    max_cost = max(max_cost, travel_cost)
    current_city = next_city

# Return to depot
tour.append(0)
total_cost += distance[(current_city, 0)]
max_cost = max(max_cost, distance[(current_city, 0)])

# Output
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_cost}")