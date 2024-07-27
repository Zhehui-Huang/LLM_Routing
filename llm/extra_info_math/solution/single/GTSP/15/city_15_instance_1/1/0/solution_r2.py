from pulp import LpProblem, Lpad, LpVariable, LpMinimize, lpSum, LpStatus
import math

# Coordinates of cities including the depot
cities = [(29, 51), (49, 20), (79, 69), (17, 20), (18, 61), (40, 57),
          (57, 30), (36, 12), (93, 43), (17, 36), (4, 60), (78, 82),
          (83, 96), (60, 50), (98, 1)]

# Groups of cities
groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

# Function to calculate Euclidean distance between two cities
def distance(ci, cj):
    return math.sqrt((cities[ci][0] - cities[cj][0])**2 + (cities[ci][1] - cities[cj][1])**2)

# Create the problem
prob = LpProblem("MinimizeOverallDistance", LpMinimize)

# Variables
x = LpVariable.dicts("x", ((i, j) for i in range(15) for j in range(15) if i != j), cat='Binary')

# Objective
prob += lpSum(x[(i, j)] * distance(i, j) for i in range(15) for j in range(15) if i != j)

# Constraints
# Select exactly one city from each group and ensure connection back to the depot
for group in groups:
    prob += lpSum(x[(i, j)] for i in group for j in range(15) if i != j) == 1
    prob += lpSum(x[(j, i)] for i in group for j in range(15) if i != j) == 1

# Maintain flow from each city (except for the depot)
for k in range(1, 15):
    prob += lpSum(x[(k, j)] for j in range(15) if k != j) - lpSum(x[(j, k)] for j in range(15) if k != j) == 0

# Solve the problem
prob.solve()

# Extract the solution (if optimal)
if LpStatus[prob.status] == 'Optimal':
    # Find the route
    non_zero_edges = [(i, j) for i in range(15) for j in range(15) if i != j and x[(i, j)].varValue == 1]
    route_from_depot = []
    next_city = 0
    total_travel_cost = 0

    # Start from depot, follow the path according to `x` variables
    while len(route_from_depot) < len(groups) + 1:
        next_steps = [j for (i, j) in non_zero_edges if i == next_city]
        if not next_steps:
            break
        next_city = next_steps[0]
        route_from_deposit += [next_city]
        total_travel_cost += distance(route_from_depot[-1], next_city)

    # Add return to depot to close the loop
    route_from_depot.append(0)
    total_travel_cost += distance(route_from_deposit[-1], 0)
    
    # Print the result
    print("Tour:", route_from_depot, "[0 included at end]")
    print("Total travel cost:", round(total_travel_cost, 2))
else:
    print("No optimal solution found.")