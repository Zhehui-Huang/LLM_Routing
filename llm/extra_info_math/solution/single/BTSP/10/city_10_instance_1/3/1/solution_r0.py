import math
from pulp import LpProblem, LpVariable, LpInteger, LpMinimize, lpSum, LpStatus, value
from itertools import combinations

# Define the coordinates for the cities
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Calculate Euclidean distances between all pairs of cities
def euclidean_distance(c1, c2):
    return math.sqrt((cities[c1][0] - cities[c2][0])**2 + (cities[c1][1] - cities[c2][1])**2)

n = len(cities)
distances = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Create the problem
prob = LpProblem("Minimize_the_maximum_distance_between_consecutive_cities", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=LpInteger, lowBound=0, upBound=1)
d = LpVariable("maximum_distance", lowBound=0, cat='Continuous')

# Objective function
prob += d

# Constraints
# Each city is entered and left exactly once
for i in range(n):
    prob += lpSum(x[i, j] for j in range(n) if i != j) == 1  # leave city i
    prob += lpSum(x[j, i] for j in range(n) if i != j) == 1  # enter city i

# Maximum distance constraint
for i in range(n):
    for j in range(n):
        if i != j:
            prob += distances[i][j] * x[i, j] <= d

# Subtour elimination constraints
for s in range(2, n):
    for S in combinations(range(1, n), s):
        prob += lpSum(x[i, j] for i in S for j in S if i != j) <= len(S) - 1

# Solve the problem
prob.solve()

# Extract the solution
tour = []
max_dist = value(d)
current_city = 0
visited = [0] * n
tour.append(current_city)
visited[current_city] = 1

while True:
    next_city = None
    for j in range(n):
        if current_city != j and x[current_city, j].varValue == 1:
            next_city = j
            break
    if next_city is None or next_city == 0:
        break
    tour.append(next_city)
    current_city = next_city

tour.append(0)  # Return to depot

# Calculate the total travel cost
total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {round(total_cost, 2)}")
print(f"Maximum distance between consecutive cities: {round(max_dist, 2)}")