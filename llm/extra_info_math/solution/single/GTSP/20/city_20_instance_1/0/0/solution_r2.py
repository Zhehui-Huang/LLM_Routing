import pulp
import math

# City coordinates
coordinates = [
    (14, 77),  # Depot 0
    (34, 20),  # 1
    (19, 38),  # 2
    (14, 91),  # 3
    (68, 98),  # 4
    (45, 84),  # 5
    (4, 56),   # 6
    (54, 82),  # 7
    (37, 28),  # 8
    (27, 45),  # 9
    (90, 85),  # 10
    (98, 76),  # 11
    (6, 19),   # 12
    (26, 29),  # 13
    (21, 79),  # 14
    (49, 23),  # 15
    (78, 76),  # 16
    (68, 45),  # 17
    (50, 28),  # 18
    (69, 9)    # 19
]

# City groups
groups = [
    [5, 6, 7, 11, 17],    # Group 0
    [1, 4, 8, 13, 16],    # Group 1
    [2, 10, 15, 18, 19],  # Group 2
    [3, 9, 12, 14]        # Group 3
]

# Calculate Euclidean distances
def euclidean(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Create the LP problem
problem = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

# Decision variables x_ij
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j),
                          cat='Binary')

# Objective function
problem += pulp.lpSum(x[i, j] * euclidean(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraints ensuring one exit from each group to any outside city, and one entry as well
for group in groups:
    problem += pulp.lpSum(x[i, j] for i in group for j in range(len(coordinates)) if j not in group) == 1
    problem += pulp.lpSum(x[i, j] for j in group for i in range(len(coordinates)) if i not in group) == 1

# Conservation of flow
for i in range(len(coordinates)):
    problem += pulp.lpSum(x[i, j] for j in range(len(coordinates)) if i != j) == pulp.lpSum(x[j, i] for j in range(len(coordinates)) if i != j)

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=0))

if status == pulp.LpStatusOptimal:
    tour = []
    for i in range(len(coordinates)):
        for j in range(len(coordinates)):
            if i != j and pulp.value(x[i, j]) == 1:
                tour.append((i, j))

    final_tour = []
    used = set()
    current_city = 0
    while True:
        final_tour.append(current_city)
        used.add(current_city)
        next_city = None
        for (i, j) in tour:
            if i == current_city:
                next_city = j
                break
        if next_city in used:
            break
        current_city = next_city
    final_tour.append(0)  # end at depot

    total_cost = sum(euclidean(final_tour[i], final_tour[i+1]) for i in range(len(final_tour) - 1))

    # Output results
    print("Tour:", final_tour)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("Failed to find a solution.")