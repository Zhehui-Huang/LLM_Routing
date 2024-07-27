import pulp
import math

# Define the coordinates of the cities
coordinates = [
    (26, 60),  # City 0 (Depot)
    (73, 84),  # City 1
    (89, 36),  # City 2
    (15, 0),   # City 3
    (11, 10),  # City 4
    (69, 22),  # City 5
    (28, 11),  # City 6
    (70, 2),   # City 7
    (47, 50),  # City 8
    (60, 29),  # City 9
    (29, 26),  # City 10
    (85, 68),  # City 11
    (60, 1),   # City 12
    (71, 73),  # City 13
    (82, 47),  # City 14
    (19, 25),  # City 15
    (75, 9),   # City 16
    (52, 54),  # City 17
    (64, 72),  # City 18
    (14, 89)   # City 19
]

# Number of cities (including depot)
n = len(coordinates)

# Function to calculate Euclidean distance between two points
def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# Create a dictionary of distances
distances = {
    (i, j): distance(coordinates[i], coordinates[j])
    for i in range(n) for j in range(n) if i != j
}

# Setting up the optimization problem: MinMax TSP
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
maximal_distance = pulp.LpVariable("Maximal_Distance")

# Objective
problem += maximal_distance

# Constraints
# Ensure every city is entered and left
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1

# Maximal_Distance constraints
for i in range(n):
    for j in range(n):
        if i != j:
            problem += x[i, j] * distances[i, j] <= maximal_distance

# Subtour elimination constraints
for S in range(2, n):
    subsets = itertools.combinations(range(1, n), S)
    for subset in subsets:
        problem += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
status = problem.solve()

# Output results:
if pulp.LpStatus[status] == 'Optimal':
    tour = []
    current_location = 0
    tour.append(current_location)
    total_cost = 0
    max_distance = 0
    
    # Extracting the tour from the decision variables
    while len(tour) < n:
        for j in range(n):
            if j != current_location and pulp.value(x[current_location, j]) == 1:
                tour.append(j)
                total_cost += distances[current_location, j]
                max_distance = max(max_distance, distances[current_location, j])
                current_location = j
                break
                
    # Closing the tour to the depot
    total_cost += distances[current_location, 0]
    max_distance = max(max_distance, distances[current_location, 0])
    tour.append(0)  # return to depot

    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
    print(f"Maximum distance between consecutive cities: {max_distance}")
else:
    print("No optimal solution found.")