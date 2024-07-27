import pulp
import math

# Define city coordinates
coordinates = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90),
    (54, 46), (8, 70), (97, 62), (14, 41), (70, 44),
    (27, 47), (41, 74), (53, 80), (21, 21), (12, 39)
]

n = len(coordinates)

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Cost matrix
cost_matrix = {
    (i, j): euclidean_distance(coordinates[i], coordinates[j])
    for i in range(n) for j in range(n) if i != j
}

# Setting up the problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", cost_matrix.keys(), cat=pulp.LpBinary)

# Objective function
model += pulp.lpSum([cost_matrix[i] * x[i] for i in cost_matrix.keys()]), "Total Cost of Tour"

# Constraints
for k in range(n):
    model += (pulp.lpSum([x[(i, j)] for i, j in cost_matrix.keys() if i == k]) == 1, f"Leave_{k}")
    model += (pulp.lpSum([x[(i, j)] for i, j in cost_matrix.keys() if j == k]) == 1, f"Enter_{k}")

# Subtour elimination constraints
for m in range(2, n):
    for S in itertools.combinations(range(1, n), m):
        model += (pulp.lpSum([x[(i, j)] for i in S for j in S if i != j]) <= len(S) - 1)

# Solve the problem
model.solve(pulp.PULP_CBC_CMD(msg=False))

if model.status == 1:  # Check if the problem is solved
    print("Solution Found")
    # Extract the solution
    tour = []
    for i in range(n):
        for j in range(n):
            if i != j and pulp.value(x[(i, j)]) == 1:
                tour.append((i, j))
    
    # Make the tour readable
    current_city = 0
    tour_order = [0]
    while len(tour_order) < n:
        for _, j in tour:
            if _ == current_city:
                current_city = j
                tour_order.append(j)
                break
    tour_order.append(0)  # Return to depot
    
    total_cost = pulp.value(model.objective)
    print(f"Tour: {tour_order}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("Solution not found")