import pulp
import math

# Cities coordinates
cities = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23),
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

n = len(cities)

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + 
                     (cities[city1][1] - cities[city2][1])**2)

# Create the LP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Create the variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')
u = pulp.LpVariable.dicts("u", range(n), lowBound=0, upBound=n-1, cat='Continuous')

# Objective function: minimize the maximum distance
max_distance = pulp.LpVariable("max_distance")
prob += max_distance

# Constraints
for i in cities:
    prob += pulp.lpSum([x[(i, j)] for j in cities if i != j]) == 1             # Exactly one outgoing arc
    prob += pulp.lpSum([x[(j, i)] for j in cities if i != j]) == 1             # Exactly one incoming arc

# Subtour elimination constraints (Miller-Tucker-Zemlin formulation)
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            prob += (u[i] - u[j] + n*x[(i, j)]) <= (n-1)

# Max distance constraint
for i in cities:
    for j in cities:
        if i != j:
            prob += (x[(i, j)] * euclidean_distance(i, j)) <= max_distance

# Solve the problem
prob.solve()

# Extract solution
tour = []
current_city = 0
while True:
    next_cities = [j for j in cities if j != current_city and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city
    if current_city == 0:
        break

# Put it back to start from depot 0
tour = [0] + tour

# Calculate the total cost of the tour
total_cost = sum(euclidean_peruclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Calculate max distance
max_leg_distance = max(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

output = {
    "Tour": tour,
    "Total travel cost": total_cost,
    "Maximum distance between consecutive cities": max_leg_distance
}

print(output)