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
problem += pulp.lpSum(x[i, j] * calculate_distance(coordinates[i], coordinates[j]) for i in range(len(coordinates)) for j in range(len(coordinates)) if i != j), "Minimize_Total_Travel_Cost"

# Constraints:
for group in city_groups:
    # Choose exactly one city from each group
    problem += pulp.lpSum(x[0, j] for j in group) == 1
    problem += pulp.sum(x[j, 0] for j in group) == 1
    # Ensure entering and exiting each city only once
    for city in group:
        problem += pulp.lpSum(x[city, j] for j in range(len(coordinates)) if j != city) == 1
        problem += pulp.lpSum(x[j, city] for j in range(len(coordinates)) if j != city) == 1

# Solve the problem
status = problem.solve()

# Extract the solution
if status == pulp.LpStatusOptimal:
    tour = [0]
    current_city = 0
    visited = set([0])
    
    while len(visited) < k:
        for j in range(1, len(coordinates)):
            if pulp.value(x[current_city, j]) == 1 and j not in visited:
                tour.append(j)
                visited.update([city for group in city_groups for city in group if city == j])
                current_city = j
                break
    
    tour.append(0)  # Return to the depot city
    
    # Calculate the total tour cost
    total_cost = sum(calculate_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))
    
    # Output the results
    print(f"Tour: {tour}")
    print(f"Total travel cost: {total_cost:.2f}")
else:
    print("No optimal solution found.")