import pulp
import math

# City coordinates
coordinates = [
    (8, 11),   # Depot city 0
    (40, 6),   # 1
    (95, 33),  # 2
    (80, 60),  # 3
    (25, 18),  # 4
    (67, 23),  # 5
    (97, 32),  # 6
    (25, 71),  # 7
    (61, 16),  # 8
    (27, 91),  # 9
    (91, 46),  # 10
    (40, 87),  # 11
    (20, 97),  # 12
    (61, 25),  # 13
    (5, 59),   # 14
    (62, 88),  # 15
    (13, 43),  # 16
    (61, 28),  # 17
    (60, 63),  # 18
    (93, 15)   # 19
]

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],  # Group 0
    [2, 6, 7, 8, 12, 15],       # Group 1
    [4, 9, 10, 16, 17, 18]      # Group 2
]

# Calculate distances
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Initialize the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Binary variable x_ij
x = pulp.LpVariable.dicts("x",
                          ((i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j),
                          cat='Binary')

# Create total distances dictionary
distances = {(i, j): euclidean_distance(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j}

# Objective function
problem += pulp.lpSum([x[(i, j)] * distances[i, j] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j])

# Constraints for guaranteeing to leave and return to each cluster exactly once
for group in groups:
    problem += pulp.lpSum([x[(i, j)] for i in group for j in range(len(coordinates)) if j not in group]) == 1
    problem += pulp.lpSum([x[(j, i)] for i in group for j in range(len(coordinates)) if j not in group]) == 1

# Consist depo based outgoing and incoming connections
depot_group = [0]  # Depot is a separate group
problem += pulp.lpSum([x[(0, j)] for j in range(1, len(coordinates))]) == 1  # Exactly one leaving depot
problem += pulp.lpSum([x[(j, 0)] for j in range(1, len(coordinates))]) == 1  # Exactly one entering depot

# Subtour elimination constraints ensuring correct flow through the network
for i in range(1, len(coordinates)):
    for j in range(1, len(coordinates)):
        if i != j:
            problem += x[(i, j)] <= (len(coordinates) - 1) * (pulp.lpSum([x[(i2, j2)] for i2 in range(len(coordinates)) for j2 in range(len(coordinates)) if i2 != j2 and i2 != 0 and j2 != i]))

# Solve the problem
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Retrieve the solution
if status == pulp.LpStatusOptimal:
    tour = []
    total_travel_cost = 0
    current = 0
    already_visited = set()
    already_visited.add(current)
    while len(already_visited) < 4:
        for j in range(len(coordinates)):
            if pulp.value(x[(current, j)]) == 1:
                tour.append(j)
                total_travel_cost += euclidean_distance(current, j)
                already_visited.add(j)
                current = j
                break
    tour.insert(0, 0)  # Insert depot at the start
    total_travel_cost += euclidean_distance(current, 0)  # Return to depot
    print("Tour:", tour)
    print("Total travel cost:", total_travel_cost)
else:
    print("No Optimal Solution Found")