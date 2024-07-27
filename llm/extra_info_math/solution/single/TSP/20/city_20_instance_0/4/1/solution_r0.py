import pulp
import math

# Coordinates of the cities including the depot (city 0)
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18), 
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91), 
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59), 
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Number of cities
n = len(cities)

# Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0]) ** 2 + (cities[city1][1] - cities[city2][1]) ** 2)

# Create the problem variable to contain the problem data
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function
model += pulp.lpSum(x[(i, j)] * distance(i, j) for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += pulp.lpSum(x[(i, j)] for j in range(n) if i != j) == 1  # leave city i
    model += pulp.lpSum(x[(j, i)] for j in range(n) if i != j) == 1  # enter city i

# Subtour elimination constraints
for s in range(2, n):
    for S in itertools.combinations(range(1, n), s):
        model += pulp.lpSum(x[(i, j)] for i in S for j in S if i != j) <= len(S) - 1

# Solve the model
model.solve()

# Extract the tour
tour = []
visited = 0
while True:
    for i in range(n):
        if x[(visited, i)].varValue == 1:
            tour.append(visited)
            visited = i
            break
    if visited == 0:
        break

tour.append(0)  # add the depot city to complete the tour

# Calculate the total travel cost
total_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

# Output the tour and the total travel cost
print("Tour:", tour)
print("Total travel cost:", total_cost)