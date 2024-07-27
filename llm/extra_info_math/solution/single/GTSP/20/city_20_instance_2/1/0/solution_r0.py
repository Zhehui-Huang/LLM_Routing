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
def calculate_distance(point1, point2):
    return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

# Define the problem
problem = pulp.LpProblem("Robot_Visit_Minimum_Cost", pulp.LpMinimize)

# Variables: x_ij is 1 if the robot moves from city i to city j, else it's 0
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary')
     for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j}

# Objective function: Minimize the total travel cost
problem += pulp.lpSum(x[i, j] * calculate_distance(coordinates[i], coordinates[j]) for i in coordinates for j in coordinates if i != j and j != i), "Minimize_Total_Travel_Cost"

# Constraints:
# Ensure only one exit and one entry per group
for group in city_groups:
    problem += pulp.lpSum(x[i, j] for i in group for j in range(len(coordinates)) if j not in group and i != j) == 1, f"One_exit_from_group_{group}"
    problem += pulp.lpSum(x[j, i] for i in group for j in range(len(coordinates)) if j not in group and i != j) == 1, f"One_entry_to_group_{group}"

# Flow conservation (excluding depot)
for city_index in range(1, len(coordinates)):
    problem += (pulp.lpSum(x[j, city_index] for j in range(len(coordinates)) if j != city_index) ==
                pulp.lpSn(x[city_index, j] for j in range(len(coordinates)) if j != city_index), f"Flow_convservation_at_{city_index}")

# Subtour Elimination
u = {i: pulp.LpVariable(f"u_{i}", lowBound=0, cat='Continuous') for i in range(2, len(coordinates))}
for p in range(2, len(coordinates)):
    for q in range(2, len(coordinates)):
        if p != q:
            problem += (u[p] - u[q] + k * pulp.lpSum(x[i, j] for i in coordinates[p] for j in coordinates[q] if i != j) +
                        (k-2) * pulp.lpSum(x[j, i] for i in coordinates[q] for j in coordinates[p] if i != j) <= k-1), f"Subtour_elimination_{p}_{q}"

# Solve the problem
problem.solve()

# Solution extraction
tour = [0]
current_city = 0
visited = set([0])

while len(visited) < len(coordinates):
    for j in range(len(coordinates)):
        if j != current_city and pulp.value(x[current_city, j]) == 1:
            tour.append(j)
            visited.add(j)
            current_city = j
            break

tour.append(0)  # Return to start point

# Calculate the total tour cost
total_cost = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

# Output the results
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")