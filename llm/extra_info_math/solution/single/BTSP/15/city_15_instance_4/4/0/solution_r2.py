import pulp
from math import sqrt
import itertools

# Define the coordinates of the cities
coords = [
    (35, 40), (39, 41), (81, 30), (5, 50), (72, 90), (54, 46),
    (8, 70), (97, 62), (14, 41), (70, 44), (27, 47), (41, 74),
    (53, 80), (21, 21), (12, 39)
]

# Number of cities, including depot
n = len(coords)

# Calculating Euclidean distance between each pair of cities
def calc_distance(coord1, coord2):
    return sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Create the distance matrix
distance_matrix = [[calc_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
problem = pulp.LpProblem("MinMaxDistanceTSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n)), cat='Binary')
z = pulp.LpVariable("z", lowBound=0)

# Objective function: Minimize the maximum edge used in the tour
problem += z

# Constraints to limit the departure and arrival from each city
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if j != i) == 1, f"One_outgoing_edge_{i}"
    problem += pulp.lpSum(x[j, i] for j in range(n) if j != i) == 1, f"One_incoming_edge_{i}"

# Constraint to ensure the maximum edge length is appropriate
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distance_matrix[i][j] <= z

# Subtour elimination constraints
for s in range(2, n):
    subsets = itertools.combinations(range(n), s)
    for subset in subsets:
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem using the CBC solver
status = problem.solve(pulp.PULP_CBC_CMD(msg=False))

# Check if a solution was found
if status == pulp.LpStatusOptimal:
    print("Optimal solution found.")
    tour = []
    for i in range(n):
        for j in range(n):
            if pulp.value(x[i, j]) == 1:
                tour.append((i, j))
    
    # Order the sequence of traveling
    ordered_tour = [0]
    current_city = 0
    while len(ordered_tour) < n:
        for _, j in tour:
            if _ == current_city:
                ordered_tour.append(j)
                current_city = j
                break
    ordered_tour.append(0)  # Going back to the depot
    
    # Calculate total travel cost
    total_distance = sum(distance_matrix[ordered_tour[i]][ordered_tour[i+1]] for i in range(len(ordered_tour)-1))
    max_distance = max(distance_matrix[ordered_tour[i]][ordered_tour[i+1]] for i in range(len(ordered_tour)-1))
    
    # Output the results
    print("Tour:", ordered_tour)
    print("Total travel cost:", total_distance)
    print("Maximum distance between consecutive cities:", max_distance)
else:
    print("No optimal solution found. Status:", pulp.LpStatus[status])