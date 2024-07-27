import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# Define the cities coordinates
cities = {
    0: (9, 93), # Depot
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 39)
}

# Define groups of cities
city_groups = [
    [2, 7, 10, 11, 14],
    [1, 3, 5, 8, 13],
    [4, 6, 9, 12]
]

# Initialize the problem
prob = LpProblem("RobotTour", LpMinimize)

# Create the variables: x[i][j] is 1 if the tour goes from city i to city j
x = {i: {j: LpVariable(f"x_{i}_{j}", cat="Binary") for j in cities if i != j} for i in cities}

# Objective function: Minimize the sum of distances between consecutive cities
def euclidean(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

prob += lpSum(x[i][j] * euclidean(cities[i], cities[j])
              for i in cities for j in cities if i != j and j in x[i])

# Add constraints ensuring only one city from each group is visited
for idx, group in enumerate(city_groups):
    prob += lpSum(x[i][j] for i in group for j in cities if i != j and j not in group) == 1
    prob += lpSum(x[j][i] for i in group for j in cities if i != j and j not in group) == 1

# Flow conservation constraints for each city
for i in cities:
    prob += lpSum(x[i][j] for j in cities if j in x[i]) == 1
    prob += lpSum(x[j][i] for j in cities if i in x[j]) == 1

# Solve the problem using PuLP's default solver
prob.solve()

# Gather the solution
tour = [0]
current_city = 0

while True:
    next_cities = [j for j in cities if j != current_city and x[current_city][j].varValue > 0.99]
    if not next_cities:
        break
    next_city = next_cities[0]
    if next_city == 0:
        break
    tour.append(next_city)
    current_city = next_city
tour.append(0)  # return to the depot

# Calculate the total travel cost of the tour
total_cost = sum(euclidean(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))

# Output result
print("Tour:", tour)
print("Total travel cost:", total_cost)