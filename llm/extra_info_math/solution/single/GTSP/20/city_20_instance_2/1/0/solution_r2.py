import pulp
import math

# Coordinates of the cities
coordinates = [
    (3, 26),   # Depot city 0
    (85, 72),  # City 1
    (67, 0),   # City 2
    (50, 99),  # City 3
    (61, 89),  # City 4
    (91, 56),  # City 5
    (2, 65),   # City 6
    (38, 68),  # City 7
    (3, 92),   # City 8
    (59, 8),   # City 9
    (30, 88),  # City 10
    (30, 53),  # City 11
    (11, 14),  # City 12
    (52, 49),  # City 13
    (18, 49),  # City 14
    (64, 41),  # City 15
    (28, 49),  # City 16
    (91, 94),  # City 17
    (51, 58),  # City 18
    (30, 48)   # City 19
]

# City groups
city_groups = [
    [7, 10, 11, 12],
    [3, 8, 13, 16],
    [2, 4, 15, 18],
    [1, 9, 14, 19],
    [5, 6, 17]
]

# Number of groups
k = len(city_groups)

# Calculate Euclidean distance between two points
def calculate_distance(i, j):
    return math.sqrt((coordinates[i][0] - coordinates[j][0]) ** 2 + (coordinates[i][1] - coordinates[j][1]) ** 2)

# Define LP problem
problem = pulp.LpProblem("Minimal_Route", pulp.LpMinimize)

# Decision variables x_ij : 1 if move is from i to j; 0 otherwise
x = {(i, j): pulp.LpVariable(cat=pulp.LpBinary, name=f"x_{i}_{j}") for i in range(len(coordinates)) for j in range(len(coordinates))}

# Objective Function: Minimize total distance
problem += pulp.lpSum(x[i, j] * calculate_distance(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j)

# Constraint: Enter and leave each group exactly once
for group in city_groups:
    problem += pulp.lpSum(x[0, j] for j in group) == 1
    problem += pulp.lpSum(x[i, 0] for i in group) == 1

# Constraint: Maintain connectivity within the solution
for j in range(1, len(coordinates)):
    problem += pulp.lpSum(x[i, j] for i in range(len(coordinates)) if i != j) == pulp.lpSum(x[j, k] for k in range(len(coordinates)) if j != k)

# Solve problem
problem.solve()

# Check if a valid solution was found
if pulp.LpStatus[problem.status] == 'Optimal':
    # Extract the tour
    path = []
    current_location = 0
    path.append(current_location)
    
    # Follow the path determined by x_ij variables
    while True:
        next_location = [j for j in range(len(coordinates)) if pulp.value(x[current_location, j]) == 1]
        if len(next_location) == 0:
            break
        next_location = next_location[0]
        path.append(next_location)
        current_location = next_location
        if current_location == 0:
            break
    
    # Calculate the total distance
    total_distance = sum(calculate_distance(path[i], path[i+1]) for i in range(len(path) - 1))

    print(f"Tour: {path}")
    print(f"Total travel cost: {total_distance}")
else:
    print("No optimal solution found.")