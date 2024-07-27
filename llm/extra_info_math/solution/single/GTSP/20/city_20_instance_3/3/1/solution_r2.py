import pulp
import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

# City coordinates
coordinates = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), 
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), 
    (18, 16), (4, 43), (53, 76), (19, 72)
]

city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], 
    [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Creating a list of all possible cities to choose one from each group including the depot
from itertools import product
all_possible_nodes = [0] + [item for sublist in city_groups for item in sublist]

# Set up the problem
problem = pulp.LpProblem("TSP_Group_Selection", pulp.LpMinimize)

# Decision variables
x_vars = pulp.LpVariable.dicts("x", (all_possible_nodes, all_possible_nodes),
                                lowBound=0, upBound=1, cat=pulp.LpBinary)

# Objective function
problem += pulp.lpSum(x_vars[i][j] * euclidean_distance(coordinates[i], coordinates[j]) 
                      for i in all_possible_nodes for j in all_possible_nodes if i != j)

# Each group must connect to one city not in the group exactly once
for group in city_groups:
    problem += pulp.lpSum(x_vars[i][j] for i in group for j in all_possible_nodes if j not in group) == 1
    problem += pulp.lpSum(x_vars[j][i] for i in group for j in all_possible_nodes if j not in group) == 1

# Additional constraints to force starting and ending at depot (city 0)
problem += pulp.lpSum(x_vars[0][j] for j in all_possible_nodes if j != 0) == 1
problem += pulp.lpSum(x_vars[i][0] for i in all_possible_nodes if i != 0) == 1

# To prevent subtours
u = pulp.LpVariable.dicts('u', all_possible_nodes, lowBound=0, cat='Continuous')
for i in all_possible_nodes:
    for j in all_possible_nodes:
        if i != j and (i != 0 and j != 0):
            problem += u[i] - u[j] + (len(all_possible_nodes) * x_vars[i][j]) <= len(all_possible_nodes) - 1

# Solve the problem
problem.solve()

# Calculate total distance from the solution
total_distance = sum(x_vars[i][j].varValue * euclidean_distance(coordinates[i], coordinates[j])
                     for i in all_possible_nodes for j in all_possible_nodes if i != j)

# Extraction of the tour from the decision variables
tour = [0]
while len(tour) < len(all_possible_nodes):
    next_city = [j for j in all_possible_nodes if x_vars[tour[-1]][j].varValue == 1][0]
    tour.append(next_city)
    if next_city == 0:
        break

print("Tour: ", tour)
print("Total travel cost: ", total_distance)