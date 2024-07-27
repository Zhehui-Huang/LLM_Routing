import pulp
import math

# City positions indexed from 0 to 9
positions = [
    (53, 68), (75, 11), (91, 95), (22, 80),
    (18, 63), (54, 91), (70, 14), (97, 44),
    (17, 69), (95, 89)
]

# Groups of cities (excluding depot)
groups = [
    [5, 6, 7],
    [2, 3],
    [1, 9],
    [4, 8]
]

# Calculate Euclidean distances
def calc_distance(pos1, pos2):
    return math.sqrt((pos1[0] - pos2[0]) ** 2 + (pos1[1] - pos2[1]) ** 2)

# Total number of cities (including the depot)
n = len(positions)

# Distance matrix
distances = [[calc_distance(positions[i], positions[j]) for j in range(n)] for i in range(n)]

# Setting up the problem
model = pulp.LpProblem("Robot_Tour_Problem", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective
model += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints

# Each group has exactly one edge leaving it and one edge entering it
for group in groups:
    model += pulp.lpSum(x[i, j] for i in group for j in set(range(n)) - set(group)) == 1
    model += pulp.lpSum(x[j, i] for i in group for j in set(range(n)) - set(group)) == 1

# Flow conservation at each node
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == pulp.lpSum(x[j, i] for j in range(n) if i != j)

# Subtour elimination not necessary due to group constraints setting the problem structure

# Solve the model
status = model.solve()

# Preparing for output
if pulp.LpStatus[status] == 'Optimal':
    tour = []
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[i, j]) == 1:
                tour.append((i, j))

    # Construct the tour sequence starting from the depot city 0
    tour_sequence = [0]
    current_city = 0
    while len(tour_sequence) < len(groups) + 1:
        for transit in tour:
            if transit[0] == current_city:
                tour_sequence.append(transit[1])
                current_city = transit[1]
                break

    # Append the start city to complete the tour
    tour_sequence.append(0)

    # Calculate total travel cost from the tour sequence
    total_cost = sum(distances[tour_sequence[i]][tour_sequence[i + 1]] for i in range(len(tour_sequence) - 1))

    print(f"Tour: {tour_sequence}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("Failed to find an optimal solution.")