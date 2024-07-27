import numpy as np
from pulp import LpMinimize, LpProblem, LpVariable, lpSum, LpBinary, PULP_CBC_CMD
import itertools

# Cities coordinates (index corresponds to the city number)
cities_coordinates = [(9, 93), (8, 51), (74, 99), (78, 50), (21, 23), 
                      (88, 59), (79, 77), (63, 23), (19, 76), (21, 38),
                      (19, 65), (11, 40), (3, 21), (60, 55), (4, 39)]

# Number of cities
n = len(cities_coordinates)

# Calculate the Euclidean distance between each pair of cities
def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Distance matrix
distance_matrix = [[euclidean_distance(cities_coordinates[i], cities_coordinates[j]) for j in range(n)] for i in range(n)]

# Setup the TSP problem
model = LpProblem(name="TSP", sense=LpMinimize)

# Decision variables
x = {(i, j): LpVariable(cat=LpBinary, name=f"x_{i}_{j}") for i in range(n) for j in range(n) if i != j}

# Objective function: minimize the travel cost
model += lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
for i in range(n):
    model += lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave each city only once
    model += lpSum(x[j, i] for j in range(n) if i != j) == 1  # Enter each city only once

# Subtour elimination constraints
for k in range(2, n):
    for subset in itertools.combinations(range(1, n), k):
        model += lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
solver = PULP_CBC_CMD(msg=False)
status = model.solve(solver)

if status == 1:
    # Extract the solution
    tour = []
    current = 0
    visited = [current]
    while len(visited) < n:
        for j in range(n):
            if j not in visited and x[current, j].varValue == 1:
                tour.append(current)
                current = j
                visited.append(current)
                break
    tour.append(0)  # Complete the tour by returning to the depot

    # Calculate the total cost of the tour
    total_cost = sum(distance[/n_0_\(0)_25{distance_matrix[tour[i]][tour[i + 1]]\} 7 remaining toursspan\]_0_\(_/span00,10007for\i \_=range(length i,tour.__points)_1_\\\_outputtour,_tour\)\__\[\(\2+next-\end_}0\) span \(2)/i span \(2/ span\ \(span\)\

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No solution found by the solver.")