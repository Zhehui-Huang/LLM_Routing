import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Define the cities coordinates
cities = [
    (9, 93), (8, 51), (74, 99), (78, 50), (21, 23),
    (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
    (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)
]

# Define groups of cities
city_groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Initialize the problem
prob = LpProblem("RobotTour", LpMinimize)

# Create the variables: x[i][j] is 1 if the tour goes from city i to city j
x = {i: {j: LpVariable(f"x_{i}_{j}", cat=LpBinary) for j in cities if i != j} for i in cities}

# Objective function: Minimize the sum of distances between consecutive cities
distances = lambda c1, c2: math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)
cost = lpSum(x[i][j] * distances(cities[i], cities[j]) for i in cities for j in cities if i != j)
prob += cost

# Constraints
# Each group must connect exactly once to the rest of the graph
for group_id, members in city_groups.items():
    prob += lpSum(x[i][j] for i in members for j in cities if j not in members) == 1
    prob += lpSum(x[j][i] for i in members for j in cities if j not in members) == 1

# Each city must have exactly one inbound and one outbound connection
for i in cities:
    prob += lpSum(x[i][j] for j in cities if i != j) == 1
    prob += lpSum(x[j][i] for j in cities if i != j) == 1

# Subtour elimination constraints
u = {i: LpVariable(f"u_{i}", lowBound=0) for i in cities}
k = len(city_groups) + 1  # Number of groups plus one for the depot
for i in cities:
    for j in cities:
        if i != j and i != 0 and j != 0:
            prob += u[i] - u[j] + (k * x[i][j]) <= k - 1

# Solve the problem
prob.solve()

# Extract tour from variables
tour = [0]
current_city = 0
while True:
    next_city = [j for j in cities if j != current_city and x[current_city][j].varValue >= 0.99][0]
    if next_query == 0:
        break
    tour.append(next_city)
    current_city = next_city
tour.append(0)

# Calculate the total travel cost of the tour
total_cost = sum(distances(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Output result
print("Tour:", tour)
print("Total travel cost:", total_cost)