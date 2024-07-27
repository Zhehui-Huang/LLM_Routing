import pulp
import math

# Define city coordinates
cities = {
    0: (54, 87),
    1: (21, 84),
    2: (69, 84),
    3: (53, 40),
    4: (54, 42),
    5: (36, 30),
    6: (52, 82),
    7: (93, 44),
    8: (21, 78),
    9: (68, 14),
    10: (51, 28),
    11: (44, 79),
    12: (56, 58),
    13: (72, 43),
    14: (6, 99)
}

# Calculate Euclidean distance between each pair of cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create distance matrix
n = len(cities)
distance_matrix = [[euclidean_distance(i, j) for j in range(n)] for i in range(n)]

# Create LP model
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Define decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat=pulp.LpBinary)

# Objective function
model += pulp.lpSum([distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j]), "Total Cost"

# Constraints
for i in range(n):
    model += pulp.lpSum([x[i, j] for j in range(n) if i != j]) == 1, f"leave_{i}"
    model += pulp.lpSum([x[j, i] for j in range(n) if i != j]) == 1, f"enter_{i}"

# Subtour elimination
for i in range(2, n + 1):
    subsets = list(itertools.combinations(range(1, n), i))
    for subset in subsets:
        model += pulp.lpSum(x[i, j] for i in subset for j in subset if i != j) <= len(subset) - 1

# Solve the problem
model.solve()

# Check if the problem is solved and extract the solution
if model.status == 1:
    # Extract tour
    edges = [(i, j) for i in range(n) for j in range(n) if i != j and pulp.value(x[i, j]) == 1]
    
    # Organize the edges into a tour
    tour = [0]
    while len(tour) < n:
        for i, j in edges:
            if i == tour[-1]:
                tour.append(j)
                break

    # Close the tour by returning to the start city
    tour.append(0)
    
    # Calculate the total cost
    total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    # Output
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost}")
else:
    print("An optimal solution was not found.")