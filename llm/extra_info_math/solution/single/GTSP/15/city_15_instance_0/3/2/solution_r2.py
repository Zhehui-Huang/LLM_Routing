from math import sqrt
import pulp

# City coordinates
locations = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# City groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Function to calculate Euclidean distance between two points
def euclidean_distance(pt1, pt2):
    return sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Constructing the distance matrix
num_cities = len(locations)
distances = [[euclidean_distance(locations[i], locations[j]) for j in range(num_cities)] for i in range(num_cities)]

# Making the optimization problem
prob = pulp.LpProblem("MinimizeTourCost", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j),
                          cat=pulp.LpBinary)

# Objective
prob += pulp.lpSum(distances[i][j] * x[(i, j)] for i in range(num_cities) for j in range(num_cities) if i != j)

# Constraints for ensuring entering and leaving each group exactly once
for group_id, group_cities in groups.items():
    # Precisely one edge leading into and out of each group from/to the depot
    prob += pulp.lpSum(x[(0, j)] for j in group_cities) == 1, f"entry_to_group_{group_id}"
    prob += pulp.lpSum(x[(j, 0)] for j in group_cities) == 1, f"exit_from_group_{group_id}"

# Ensuring flow, each city except depot exactly one enter and leave
for i in range(1, num_cities):  # Except depot city
    prob += pulp.lpSum(x[(j, i)] for j in range(num_cities) if j != i) == 1, f"enter_{i}"
    prob += pulp.lpSum(x[(i, j)] for j in range(num_cities) if j != i) == 1, f"leave_{i}"

# Solve the problem
prob.solve()

# Retrieve the solution
if prob.status == pulp.LpStatusOptimal:
    tour = [0]
    next_city = 0
    while True:
        for j in range(num_cities):
            if j != next_city and pulp.value(x[(next_city, j)]) == 1:
                tour.append(j)
                next_city = j
                break
        if next_city == 0:
            break

    # Calculate cost
    tour_cost = sum(distances[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    print(f"Tour: {tour}")
    print(f"Total travel cost: {tour_cost}")
else:
    print("No optimal solution found.")