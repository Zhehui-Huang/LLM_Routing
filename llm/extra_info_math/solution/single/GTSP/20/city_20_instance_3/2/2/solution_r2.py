import pulp
import math

# Coordinates of the depot and each city
coordinates = [
    (30, 56),  # Depot
    (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77), (98, 95),
    (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73), (14, 47), (18, 16),
    (4, 43), (53, 76), (19, 72)
]

# City groups
groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Function to calculate Euclidean distances between each pair of coordinates
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create distance matrix
distances = [[calculate_distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))] for i in range(len(coordinates))]

# Creating the integer programming model
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat="Binary") for group in [range(20)] + groups for i in group for j in range(20) if i != j}

# Objective: Minimize the cost of the tour
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in range(20) for j in range(20) if i != j and x.get((i,j)))

# Constraints
# Exactly one outbound link from each group, including the depot connected to one group city
for group in groups:
    prob += pulp.lpSum(x[0, j] for j in group) == 1
    prob += pulp.lpSum(x[j, 0] for j in group) == 1

# Each city (not depot) has exactly one incoming and one outgoing edge
for j in range(1, 20):
    prob += pulp.lpSum(x[i, j] for i in range(20) if i != j and x.get((i, j))) == 1
    prob += pulp.lpSum(x[j, k] for k in range(20) if k != j and x.get((j, k))) == 1

# Adding subtour elimination constraints
for group in groups:
    for i, j in x:
        if i != j and i != 0 and j != 0:
            prob += pulp.lpSum(x[i,j] for i in group for j in group if i != j) <= len(group) - 1

# Solve the problem
prob.solve()

# Print the status of the solution
print("Status:", pulp.LpStatus[prob.status])

# Extract the tour and calculate the cost
tour = []
current = 0
next_node = None
visited = set()
total_travel_cost = 0

if pulp.LpStatus[prob.status] == 'Optimal':
    while True:
        if current in visited:
            break
        visited.add(current)
        tour.append(current)
        for j in range(20):
            if pulp.value(x[current, j]) == 1:
                total_travel_cost += distances[current][j]
                current = j
                break

    # Closing the loop to return to the depot if not already included
    if current != 0:
        tour.append(0)
        total_travel_cost += distances[current][0]

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)