import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 5: (34, 73),
    6: (6, 61), 7: (86, 69), 8: (30, 50),  9: (35, 73), 10: (42, 64), 11: (64, 30),
    12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Compute Euclidean distance
def distance(city1, city2):
    return math.sqrt(((city1[0] - city2[0]) ** 2) + ((city1[1] - city2[1]) ** 2))

# Generate cost dictionary
costs = {}
n = len(cities)
for i in range(n):
    for j in range(n):
        if i != j:
            costs[(i, j)] = distance(cities[i], cities[j])
        else:
            costs[(i, j)] = float('inf')  # ensure no self-loops

# Integer programming formulation
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Create variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')

# Objective function
prob += pulp.lpSum(costs[(i, j)] * x[(i, j)] for i in range(n) for j in range(n))

# Each city is left exactly once
for i in range(1, n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Each city is entered exactly once
for j in range(1, n):
    prob += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Subtour elimination (using Miller-Tucker-Zemlin formulation)
u = pulp.LpVariable.dicts("u", (i for i in range(n)), lowBound=0, upBound=n-1, cat='Continuous')
for i in range(1, n):
    for j in range(1, n):
        if i != j:
            prob += u[i] - u[j] + (n-1)*x[(i, j)] <= n-2

# Solve the problem
prob.solve()

# Extract the tour
tour = []
current_city = 0
remaining_cities = set(range(n))
# Follow the path
while remaining_cities:
    next_cities = [j for j in remaining_cities if pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(current_city)
    remaining_cities.remove(current_city)
    current_city = next_city

tour.append(0)  # return to depot

# Calculate the total cost of the tour
total_cost = sum(costs[(tour[i], tour[i+1])] for i in range(len(tour) - 1))

# Print the output as specified
print("Tour:", tour)
print("Total travel cost:", total_cost)