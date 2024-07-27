import pulp
import math

# Coordinates of the cities including the depot city at index 0
city_coords = [
    (30, 56), (53, 42), (1, 95), (25, 61), (69, 57), (6, 58), (12, 84), (72, 77),
    (98, 95), (11, 0), (61, 25), (52, 0), (60, 95), (10, 94), (96, 73),
    (14, 47), (18, 16), (4, 43), (53, 76), (19, 72)
]

n = len(city_coords)  # Number of cities including the depot

# Calculate Euclidean distance matrix
def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

distance_matrix = [
    [euclidean_distance(city_coords[i], city_coords[j]) for j in range(n)]
    for i in range(n)
]

# Create an LP minimization problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables, x[i][j] == 1 if the path goes from city i to city j
x = pulp.LpVariable.dicts("x",
                          ((i, j) for i in range(n) for j in range(n)),
                          cat='Binary')

# Objective Function
problem += pulp.lpSum(distance_matrix[i][j] * x[i, j] for i in range(n) for j in range(n))

# Constraints
for i in range(n):
    problem += pulp.lpSum(x[i, j] for j in range(n) if i != j) == 1  # Leave city i once
    problem += pulp.lpSum(x[j, i] for j in range(n) if i != j) == 1  # Arrive at city i once

# Solve the problem
problem.solve()

# Retrieve the solution
tour = []
current_city = 0
start_city = 0

count = 0  # Protection against infinite loops
while count < n+1:
    for j in range(n):
        if pulp.value(x[current_city, j]) == 1:
            tour.append(current_city)
            current_city = j
            break
    count += 1

tour.append(start_city)  # Return to depot

# Compute the cost of the tour
total_cost = sum(distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

print("Tour:", tour)
print("Total travel cost:", total_cost)