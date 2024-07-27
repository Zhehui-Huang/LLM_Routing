import pulp
import math

# City coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38), 
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Number of cities including the depot
n = len(cities)

# Create the distance matrix
cost = {(i, j): distance(cities[i], cities[j]) for i in range(n) for j in range(n) if i != j}

# Define the TSP problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables: x_ij = 1 if tour goes from city i to city j
x = pulp.LpVariable.dicts('x', cost.keys(), cat=pulp.LpBinary)

# Objective function: Minimize the total cost of the tour
model += pulp.lpSum([x[(i, j)] * cost[(i, j)] for (i, j) in cost.keys()]), "Total Cost"

# Each city is left exactly once
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if (i, j) in x) == 1

# Each city is visited exactly once
for j in range(n):
    model += pulp.lpSum(x[(i, j)] for i in range(n) if (i, j) in x) == 1

# Eliminating subtours using additional constraints
u = pulp.LpVariable.dicts('u', range(n), lowBound=0, upBound=n-1, cat=pulp.LpContinuous)
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            model += u[i] - u[j] + (n-1) * x[(i, j)] <= n-2

# Solve the model
model.solve()

# Extract the tour and calculate total cost
tour = [0]
current_city = 0
while True:
    next_cities = [j for j in range(n) if (current_city, j) in x and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities or current_city == 0 and len(tour) > 1:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city

# Close the tour by returning to the depot
tour.append(0)  # Return to depot

# Compute total travel cost of the tour
total_cost = sum(cost[(tour[i], tour[i + 1])] for i in range(len(tour) - 1))

# Output tour and total travel cost
print("Tour:", tour)
print("Total travel cost:", total_cost)