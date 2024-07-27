import pulp
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# City coordinates including the depot
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

# Number of cities including the depot
n = len(cities)

# Distance matrix
distance_matrix = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Define the LP problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x[i, j] is 1 if the tour goes from city i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function: minimize the travel cost
prob += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    prob += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Subtour elimination (additionally handles subtours)
for i in range(n):
    for j in range(1, n):
        if i != j:
            prob += pulp.lpSum(x[i, j] + x[j, i]) <= 1

# Solve the LP problem
prob.solve()

# Extract the tour from the decision variables
tour = []
current_city = 0
while True:
    tour.append(current_city)
    next_cities = [j for j in range(n) if pulp.value(x[current_city, j]) == 1]
    if not next_cities:  # No outgoing edge found (shouldn't happen ideally)
        break
    current_city = next_cities[0]
    if current_city == 0:  # Return to the depot if it's chosen again
        break

tour.append(0)  # To ensure the tour completes back at the depot

# Calculate the tour cost
total_travel_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

# Output the tour and its cost
print(f"Tour: {tour}")
print(f"Total travel cost: {total_travel_cost:.2f}")