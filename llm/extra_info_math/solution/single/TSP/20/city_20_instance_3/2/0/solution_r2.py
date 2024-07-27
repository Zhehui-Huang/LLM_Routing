import pulp
import math

# Define the coordinates of the cities including the depot city
cities = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84),
    (72, 77), (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94),
    (96, 73), (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

# Calculate distances between all pairs of cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

n = len(cities)
dist = [[distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Set up the optimization problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function: minimize the travel distance
prob += pulp.lpSum(x[(i, j)] * dist[i][j] for i in range(n) for j in range(n) if i != j)

# Constraints that ensure every city is visited exactly once
for i in range(n):
    prob += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1
    prob += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1

# Subtour elimination constraints
for i in range(2, n):
    S = range(i)
    prob += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract the solution
tour = []
current_city = 0
tour.append(current_city)
visited = [False] * n
visited[0] = True
total_cost = 0
for _ in range(1, n):
    next_cities = [j for j in range(n) if not visited[j] and pulp.value(x[(current_city, j)]) == 1]
    if not next_cities:
        continue
    next_city = next_cities[0]
    tour.append(next_city)
    total_cost += dist[current_city][next_city]
    current_city = next_city
    visited[next_city] = True

# Return to the depot
tour.append(0)
total_cost += dist[current_city][0]

# Display the tour and the total cost
print("Tour:", tour)
print("Total travel cost:", total_cost)