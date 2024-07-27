from pulp import *
import math

# Define the cities and their coordinates
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

grouped_cities = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Create the linear programming model to minimize distances
model = LpProblem("TSP", LpMinimize)

# Decision variables
x = LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function: minimize the sum of distances for the selected routes
model += lpSum(x[i, j] * math.sqrt((cities[i][0] - cities[j][0]) ** 2 + (cities[i][1] - cities[j][1]) ** 2) 
               for i in cities for j in cities if i != j)

# Adding constraints
# One city per group must be visited
for group in grouped_cities:
    model += lpSum(x[0, j] for j in group) == 1  # From depot to one in group
    model += lpSum(x[j, 0] for j in group) == 1  # From group back to depot

    for other_groups in grouped_cities:
        if group != other_groups:
            all_in_group = group + other_groups
            # Going in and out to just one city from each group
            model += lpSum(x[i, j] for i in group for j in other_groups) <= 1

# Solve the problem
status = model.solve(PULP_CBC_CMD(msg=False))

# Extract the solution
routes = [(i, j) for i in cities for j in cities if i != j and x[i, j].value() == 1]
tour = []
current = 0
while len(routes) > 0:
    tour.append(current)
    for i, (start, end) in enumerate(routes):
        if start == current:
            current = end
            routes.pop(i)
            break

tour.append(0)  # complete the tour by returning to the depot

# Calculate the total travel cost
total_distance = sum(math.sqrt((cities[tour[i]][0] - cities[tour[i+1]][0])**2 + (cities[tour[i]][1] - cities[tour[i+1]][1])**2)
                     for i in range(len(tour)-1))

print("Tour:", tour)
print("Total travel cost:", total_distance)