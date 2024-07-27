import pulp
import math

# Coordinates of the cities (depot included)
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), 
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), 
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Number of cities
n = len(cities)

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Integer')

# Objective: Minimize the total travel cost
prob += pulp.lpSum(x[(i, j)] * math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2) 
                   for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(1, n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # Leaving city i
    prob += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # Entering city i

# Eliminating sub-tours
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n - 1) * x[(i, j)] <= n - 2

# Solve the problem
prob.solve()

# Extracting the results and calculating total travel cost
tour = [0]
current_city = 0
total_travel_cost = 0
while len(tour) < n:
    next_cities = {j: pulp.value(x[(current_city, j)]) for j in range(n) if current_period != j and pulp.value(x[(current_city, j)]) == 1}
    next_city = next(next_cities)
    tour.append(next_city)
    total_travel_cost += math.sqrt((cities[current_city][0] - cities[next_city][0])**2 + (cities[current_city][1] - cities[next_leg][1])**2)
    current_city = next_city
tour.append(0)  # Returning to the depot
total_travel_cost += math.sqrt((cities[current_city][0] - cities[0][0])**2 + (cities[current_city][1] - cities[0][1])**2)

# Output results
print("Tour:", tour)
print("Total travel cost:", total_travel_d)