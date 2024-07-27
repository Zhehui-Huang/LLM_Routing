import pulp
import math

# City positions (x, y)
positions = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84),
    (4, 56), (54, 82), (37, 28), (27, 45), (90, 85), (98, 76),
    (6, 19), (26, 29), (21, 79), (49, 23), (78, 76), (68, 45),
    (50, 28), (69, 9)
]

# Definition of city groups
groups = [
    [5, 6, 7, 11, 17],  # Group 0
    [1, 4, 8, 13, 16],  # Group 1
    [2, 10, 15, 18, 19], # Group 2
    [3, 9, 12, 14]       # Group 3
]

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

cities = range(len(positions))

# Creating a problem instance
problem = pulp.LpProblem("TSP_Minimize_Distance", pulp.LpMinimize)

# Variable indicating if city i is connected to city j
x = pulp.LpVariable.dicts("x", 
                          ((i, j) for i in cities for j in cities if i != j), 
                          cat='Binary')

# Objective Function
problem += pulp.lpSum(euclidean_distance(positions[i], positions[j]) * x[i, j] 
             for i in cities for j in cities if i != j), "Total_Distance"

# Incoming and outgoing constraints for each group
for group in groups:
    problem += pulp.lpSum(x[i, j] for i in group for j in cities if j not in group) == 1
    problem += pulp.lpSum(x[j, i] for i in group for j in cities if j not in group) == 1

# Subtour prevention and depot connecting constraints
for i in cities:
    if i != 0:
        problem += (pulp.lpSum(x[i, j] for j in cities if i != j) == 1)
        problem += (pulp.lpSum(x[j, i] for j in cities if i != j) == 1)

problem += (pulp.lpSum(x[0, j] for j in cities if j != 0) == 1)
problem += (pulp.lpSum(x[j, 0] for j in cities if j != 0) == 1)

# Solving the problem
problem.solve()

# Output results
if pulp.LpStatus[problem.status] == "Optimal":
    total_cost = pulp.value(problem.objective)
    tour = [0]
    next_city = next(j for j, value in x[0, :].items() if value.varValue == 1)
    while next_city != 0:
        tour.append(next_city)
        next_city = next(j for i, j, value in x.items() if i == next_city and value.varValue == 1)
    tour.append(0)  # Return to depot

    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No optimal solution found.")