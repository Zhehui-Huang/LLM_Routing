import pulp
import math

# Coordinates of cities including the depot
coordinates = [(35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46), (8, 70),
               (97, 62), (14, 41), (70, 44), (27, 47), (41, 74), (53, 80), (21, 21),
               (12, 39)]

# City groups
city_groups = [[3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]]

def calculate_distance(coord1, coord2):
    """ Calculate Euclidean distance between two coordinates """
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Prepare costs matrix
number_of_cities = len(coordinates)
costs = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(number_of_cities)] for i in range(number_of_cities)]

# Define the problem
problem = pulp.LpProblem("Traveling_Salesman_Groups", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", [(i, j) for i in range(number_of_cities) for j in range(number_of_cities) if i != j], cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(costs[i][j] * x[(i, j)] for i in range(number_of_cities) for j in range(number_of_cities) if i != j), "Total_Cost"

# Constraints
for group in city_groups:
    # Exactly one edge out of each group
    problem += pulp.lpSum(x[(i, j)] for i in group for j in range(number_of_cities) if j not in group) == 1
    # Exactly one edge into each group
    problem += pulp.lpSum(x[(j, i)] for i in group for j in range(number_of_cities) if j not in group) == 1

# Ensuring connectivity and flow (Degree constraints)
for i in range(number_of_cities):
    # Sum of variables entering a node
    problem += pulp.lpSum(x[(j, i)] for j in range(number_of_cities) if j != i) == pulp.lpSum(x[(i, j)] for j in range(number_of_cities) if j != i)

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

# Output handling
if status == pulp.LpStatusOptimal:
    tour = []
    costs = []
    visited = [0]
    while len(visited) < len(city_groups) + 1:  # Additional +1 because start at depot
        for j in range(number_of_cities):
            if x[(visited[-1], j)].varValue == 1 and j not in visited:
                tour.append((visited[-1], j))
                visited.append(j)
                break
    # add edge returning to depot
    tour.append((visited[-1], 0))
    # Calculate the total travel cost
    total_cost = sum(costs[i][j] for i, j in tour)

    # Generating output
    print("Tour:", [t[0] for t in tour] + [0])  # to close the loop at the depot
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution was found.")