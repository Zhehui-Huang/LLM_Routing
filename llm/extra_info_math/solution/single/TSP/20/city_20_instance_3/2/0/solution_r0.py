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

# Calculate Euclidean distance matrix
def distance(i, j):
    return math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2)

# Create the problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective: Minimize the total travel cost
prob += pulp.lpSum(x[(i, j)] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
# Each city is left exactly once
for i in range(n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1

# Each city is entered exactly once
for j in range(n):
    prob += pulp.lpSum(x[(i, j)] for i in range(n) if i != j) == 1

# Subtour elimination (using pulp's built-in functionality)
pulp.addTSPSubtourElimination(prob, x, n, cities)

# Solve the problem
prob.solve()

# Extracting the results
tour = []
current_city = 0
next_city = None
visited = set([0])
for _ in range(1, n):
    for j in range(n):
        if j not in visited and pulp.value(x[(current_city, j)]) == 1:
            tour.append(current_city)
            current_city = j
            visited.add(j)
            break

# Close the tour
tour.append(current_city)
tour.append(0)  # Returning to the depot

# Calculate the total travel cost
total_travel_cost = sum(distance(tour[k], tour[k+1]) for k in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)