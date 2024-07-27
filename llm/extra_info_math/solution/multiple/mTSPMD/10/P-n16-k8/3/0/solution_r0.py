import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Function to calculate the Euclidean distance
def distance(coord1, coord2):
    return round(math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2), 2)

# Creating distance matrix
n = len(cities)
distance_matrix = {}
for i in range(n):
    for j in range(n):
        distance_matrix[i, j] = distance(cities[i], cities[j])

# Define the problem
model = pulp.LpProblem("TSP_Robots", pulp.LpMinimize)

# Variables: x[i][j] is 1 if city i is connected to city j
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities), cat='Binary')

# Objective
model += pulp.lpSum(distance_matrix[i, j] * x[i, j] for i in cities for j in cities)

# Constraints

# Each city is visited exactly once
for j in cities:
    model += pulp.lpSum(x[i, j] for i in cities if i != j) == 1, f"visit_in_{j}"
    model += pulp.lpSum(x[j, i] for i in cities if i != j) == 1, f"visit_out_{j}"

# Depot start and end constraints (only one robot from each depot)
for k in range(8):
    model += x[k, k] == 0  # Prevent self-loop
    model += pulp.lpSum(x[k, j] for j in cities if j != k) == 1  # leaving the depot
    model += pulp.lpSum(x[i, k] for i in cities if i != k) == 1  # coming back to the depot

# Solve the problem
model.solve()

# Retrieve results and print the solution
tours = []
total_cost = 0
for k in range(8):
    tour = [k]
    next_city = k
    while True:
        next_city = [j for j in cities if pulp.value(x[next_city, j]) == 1][0]
        if next_city == k:
            break
        tour.append(next_city)
    tour.append(k)
    tour_cost = sum(distance_matrix[tour[i], tour[i + 1]] for i in range(len(tour) - 1))
    tours.append((k, tour, tour_cost))
    total_cost += tour_cost

# Print the result
for k, tour, tour_cost in tours:
    print(f"Robot {k} Tour: {tour}")
    print(f"Robot {k} Total Travel Cost: {tour_def_cost}")

print(f"Overall Total Travel Cost: {total_cost}")