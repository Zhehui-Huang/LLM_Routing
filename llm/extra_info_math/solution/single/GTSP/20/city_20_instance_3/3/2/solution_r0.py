import math
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary

# City coordinates
coordinates = [
    (30, 56), # depot
    (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), 
    (12, 84), (72, 77), (98, 95), (11, 0), (61, 25), 
    (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), 
    (18, 16), (4, 43), (53, 76), (19, 72)
]

# Groups: lists of city indices
groups = [[4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]]

# Calculate Euclidean distance between two cities
def distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

# Set of all cities including the depot
cities = list(range(len(coordinates)))

# Create problem
prob = LpProblem("TSP_Groups", LpMinimize)

# Variables x_ij where i!=j, (i, j) are cities
x = LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat=LpBinary)

# Objective Function
prob += lpSum(x[(i, j)] * distance(i, j) for i in cities for j in cities if i != j), "Total_Travel_Cost"

# Constraints

# Each group must interact with the rest of the graph exactly twice (once in, once out)
for group in groups:
    prob += lpSum(x[(i, j)] for i in group for j in cities if j not in group) == 1, f"Out_Constraint_for_group_{group}"
    prob += lpSum(x[(j, i)] for i in group for j in cities if j not in group) == 1, f"In_Constraint_for_group_{group}"

# Flow conservation for each city excluding inter-group travel
for city in cities:
    prob += (lpSum(x[(j, city)] for j in cities if j != city) == 
             lpSum(x[(city, j)] for j in cities if j != city)), f"Flow_conservation_for_{city}"

# Solve the problem
prob.solve()

# Extract the tour and calculate its cost
tour = []
current_city = 0
tour.append(current_city)
visited = set()

while True:
    next_city = None
    for city in cities:
        if city != current_city and x[(current_city, city)].varValue == 1:
            next_city = city
            break
    if not next_city or next_city in visited:
        break
    visited.add(next_city)
    tour.append(next_city)
    current_city = next_city

# Returning to the depot
tour.append(0)

# Total travel cost
total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_cost)