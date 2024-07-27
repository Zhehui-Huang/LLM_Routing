import pulp
import math

# City coordinates
coordinates = [
    (8, 11),  # Depot city 0
    (40, 6), (95, 33), (80, 60), (25, 18), (67, 23),
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46),
    (40, 87), (20, 97), (61, 25), (5, 59), (62, 88),
    (13, 43), (61, 28), (60, 63), (93, 15)
]

# City groups
groups = [
    [1, 3, 5, 11, 13, 14, 19],  # Group 0
    [2, 6, 7, 8, 12, 15],       # Group 1
    [4, 9, 10, 16, 17, 18]      # Group 2
]

# Calculate distances
def euclidean_distance(city1, city2):
    return math.sqrt((coordinates[city1][0] - coordinates[city2][0])**2 + (coordinates[city1][1] - coordinates[city2][1])**2)

# Initialize the problem
problem = pulp.LpProblem("TSP", pulp.LpMinimize)

# Binary variable x_ij
x = pulp.LpVariable.dicts("x", 
                          [(i, j) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j], 
                          cat='Binary')

# Minimize the total cost
problem += pulp.lpSum([euclidean_distance(i, j) * x[(i, j)] for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j])

# Inflow and Outflow Constraints
for node_group in groups:
    problem += pulp.lpSum([x[(i, j)] for i in node_group for j in range(len(coordinates)) if j not in node_range(node_group)]) == 1
    problem += pulp.lpSum([x[(j, i)] for i in node_group for j in range(len(coordinates)) if j not in node_range(node_group)]) == 1

# Subtour Elimination
u = pulp.LpVariable.dicts("u", range(1, len(coordinates)), lowBound=0, upBound=len(coordinates) - 2, cat='Continuous')
for i in range(1, len(coordinates)):
    for j in range(1, len(coordinates)):
        if i != j:
            problem += u[i] - u[j] + (len(coordinates) - 2) * x[(i, j)] <= len(coordinates) - 3

# Solve the problem
status = problem.solve()

# Decode the solution
tour = []
visited = {0}
current_city = 0
total_travel_cost = 0
while len(visited) < 4:
    for next_city in range(len(coordinates)):
        if current_city != next_city and pulp.value(x[(current_city, next_city)]) == 1:
            tour.append(next_city)
            total_travel_cost += euclidean_distance(current_city, next_city)
            visited.add(next_city)
            current_city = next_city
            break
tour.insert(0, 0)  # Start at depot
tour.append(0)  # Return to depot
total_travel_root += euclidean_distance(tour[-2], 0)

print("Tour:", tour)
print("Total travel cost:", total_travel_cost)