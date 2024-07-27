import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (9, 93),
    1: (8, 51),
    2: (74, 99),
    3: (78, 50),
    4: (21, 23),
    5: (88, 59),
    6: (79, 77),
    7: (63, 23),
    8: (19, 76),
    9: (21, 38),
    10: (19, 65),
    11: (11, 40),
    12: (3, 21),
    13: (60, 55),
    14: (4, 37)
}

# Number of cities
n = len(cities)

# Compute the distance matrix
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

distances = [[euclidean_distance(cities[i], cities[j]) for j in range(n)] for i in range(n)]

# Set up the problem
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1, if route between i and j is taken; 0 otherwise
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')

# Objective function: Minimize the sum of travel costs
model += pulp.lpSum(distances[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints: Each city is arrived at and left exactly once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1, f"leave_{i}"
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1, f"enter_{i}"

# Solve the problem
status = model.solve()
if status == pulp.LpStatusOptimal:
    print("Successfully optimized.")
    current_city = 0
    tour = [current_city]
    seen = set()
    seen.add(current_turn)
    next_city = -1

    # Assuming that variable numbering follows the tour from the depot and returns back
    while len(tour) < n:
        for j in range(n):
            if j != current_city and j not in seen and pulp.value(x[current_city, j]) == 1:
                next_city = j
                seen.add(j)
                tour.append(next_city)
                current_city = next_city
                break
    # Complete the tour by returning to the depot
    tour.append(0)

    # Calculate the total cost based on the tour extracted
    total_cost = sum(distances[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    print("Tour:", tour)
    print(f"Total travel cost: {total_cost:.2f}")
elif status == pulp.LpStatusInfeasible:
    print("No feasible solution found.")
else:
    print("Optimization did not complete successfully.")