import pulp
import math

# Given cities and their coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60), 4: (25, 18),
    5: (67, 23), 6: (97, 32), 7: (25, 71), 8: (61, 16), 9: (27, 91),
    10: (91, 46), 11: (40, 87), 12: (20, 97), 13: (61, 25), 14: (5, 59),
    15: (62, 88), 16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Given city groups
city_groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Function to calculate the Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create a PuLP problem for minimization
problem = pulp.LpProblem("TSP_Variant", pulp.LpMinimize)

# Decision variables: x_ij is 1 if the path from city i to city j is chosen, otherwise 0
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function: minimize the total travel cost
problem += pulp.lpSum(distance(i, j) * x[i, j] for i in cities for j in cities if i != j)

# Constraints to ensure exactly one city from each group is visited
for group in citygroups:
    problem += pulp.lpSum(x[0, j] for j in group) == 1  # exactly one outgoing edge from the depot to each group
    problem += pulp.lpSum(x[j, 0] for j in group) == 1  # exactly one incoming edge to the depot from each group

# Constraint to guarantee maintenance of the tour
for i in cities:
    problem += pulp.lpSum(x[j, i] for j in cities if j != i) - pulp.lpSum(x[i, j] for j in cities if j != i) == 0

# Solve the problem using the default solver
problem.solve()

# Output the solution
tour = [0]
current_city = 0
while len(tour) <= len(city_groups):
    for j in cities:
        if j != current_city and pulp.value(x[current_city, j]) == 1:
            tour.append(j)
            current_city = j
            break
tour.append(0)  # Return to the starting city

total_travel_cost = sum(distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)