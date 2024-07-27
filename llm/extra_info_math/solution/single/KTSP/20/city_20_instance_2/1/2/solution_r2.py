import pulp
import math

# Coordinates of cities including the depot city at the first position
coords = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89),
    (91, 56), (2, 65), (38, 68), (3, 92), (59, 8),
    (30, 88), (30, 53), (11, 14), (52, 49), (18, 49),
    (64, 41), (28, 49), (91, 94), (51, 58), (30, 48)
]

# Function to calculate Euclidean distance
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Number of cities including the depot
n = len(coords)
# Number of cities to visit including the depot
k = 10

# Distance matrix
dist = [[euclidean_distance(coords[i], coords[j]) for j in range(n)] for i in range(n)]

# Initialize the problem
model = pulp.LpProblem("Minimize_Distance", pulp.LpMinimize)

# Variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(n) for j in range(n) if i != j), cat='Binary')
y = pulp.LpVariable.dicts("y", (i for i in range(n)), cat='Binary')

# Objective Function
model += pulp.lpSum(dist[i][j] * x[i, j] for i in range(n) for j in range(n) if i != j)

# Constraints
# Ensure exactly k cities (including the depot) are visited
model += pulp.lpSum(y[i] for i in range(n)) == k

# Ensure that each city is entered and left at most once
for i in range(n):
    model += pulp.lpSum(x[i, j] for j in range(n) if i != j) == y[i]
    model += pulp.lpSum(x[j, i] for j in range(n) if i != j) == y[i]

# Solve the problem
model.solve()

# Check the status of the solution
status = pulp.LpStatus[model.status]
print("Status:", status)

# Gathering results
tour = [0]  # Start at the depot
current_city = 0
if status == 'Optimal':
    remaining_cities = [i for i in range(1, n) if y[i].varValue == 1]

    while remaining_cities:
        for city in remaining_cities:
            if x[current_city, city].varValue == 1:
                tour.append(city)
                remaining_cities.remove(city)
                current_city = city
                break

    tour.append(0)  # Return to the depot

    # Calculate the total distance
    total_distance = sum(dist[tour[i]][tour[i + 1]] for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", total_distance)
else:
    print("No feasible solution found.")