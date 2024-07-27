import pulp
import math

# Define cities and coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

n = len(cities)

# Euclidean distance calculation function
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distances = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Define the problem
prob = pulp.LpProblem("MinimizeMaxDistance", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')
d_max = pulp.LpVariable("max_distance", lowBound=0, cat='Continuous')

# Objective function
prob += d_max

# Constraints
# Ensuring one exit and one entry per city
for k in cities:
    prob += pulp.lpSum(x[i, k] for i in cities if i != k) == 1
    prob += pulp.lpSum(x[k, j] for j in cities if k != j) == 1

# Subtour elimination constraints using Miller-Tucker-Zemlin formulation
u = pulp.LpVariable.dicts('u', cities, lowBound=0, upBound=n, cat='Integer')
for i in cities:
    for j in cities:
        if i != j and (i != 0 and j != 0):
            prob += u[i] - u[j] + n*x[i, j] <= n-1

# Connect max_distance to distances using variables
for i in cities:
    for j in cities:
        if i != j:
            prob += distances[i, j] * x[i, j] <= d_max

# Solve the LP
prob.solve()

# Result Analysis
tour = [0]
current_city = 0
visited_cities = set()
visited_cities.add(current_city)

for _ in range(len(cities)-1):
    next_city = None
    for j in cities:
        if j != current_city and pulp.value(x[current_city, j]) == 1:
            next_city = j
            break
    if next_city is None:  # No valid next city found
        print("Failed to find a valid tour.")
        break
    tour.append(next_city)
    visited_cities.add(next_city)
    current_city = next_city

tour.append(0)  # Return to the start

# Calculate travel cost and max segment distance
total_travel_cost = sum(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))
max_distance_between_cities = max(distances[tour[i], tour[i+1]] for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)
print("Maximum distance between consecutive cities:", pulp.value(d_max))