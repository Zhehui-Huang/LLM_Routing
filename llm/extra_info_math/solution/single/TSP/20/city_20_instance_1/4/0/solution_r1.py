import math
import pulp

# Provided cities' coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
    6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
    12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
    18: (50, 28), 19: (69, 9)
}

# Function to calculate Euclidean distance between two points
def euclidean_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Preparing distance matrix for the TSP
dist_matrix = {(i, j): euclidean_distance(cities[i], cities[j]) for i in cities for j in cities if i != j}

# Define the Linear Programming problem
prob = pulp.LpProblem("TSP", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", (cities.keys(), cities.keys()), 0, 1, pulp.LpBinary)

# Objective function
prob += pulp.lpSum(dist_matrix[i, j] * x[i][j] for i in cities for j in cities if i != j), "Minimize_Distance"

# Constraints: Each city is entered and left exactly once
for i in cities:
    prob += pulp.lpSum(x[i][j] for j in cities if j != i) == 1, f"Leave_city_{i}"
    prob += pulp.lpSum(x[j][i] for j in cities if j != i) == 1, f"Enter_city_{i}"

# Solve the problem
prob.solve()

# Extract solution
tour = []
current_city = 0
tour.append(current_city)

for _ in range(len(cities) - 1):
    next_cities = [j for j in cities if pulp.value(x[current_city][j]) == 1]
    if not next_cities:
        break
    next_city = next_cities[0]
    tour.append(next_city)
    current_city = next_city

# Ensure it's back to the depot
tour.append(0)

# Calculate total cost of the tour
total_cost = sum(dist_matrix[tour[i], tour[i+1]] for i in range(len(tour)-1))

# Output tour and total travel cost
print("Tour:", tour)
print("Total travel cost:", round(total_cost))