import pulp
import math

# Define the cities' coordinates
city_coordinates = [
    (53, 68),  # Depot city 0: index 0
    (75, 11),  # City 1: index 1
    (91, 95),  # City 2: index 2
    (22, 80),  # City 3: index 3
    (18, 63),  # City 4: index 4
    (54, 91),  # City 5: index 5
    (70, 14),  # City 6: index 6
    (97, 44),  # City 7: index 7
    (17, 69),  # City 8: index 8
    (95, 89)   # City 9: index 9
]

# Define city groups
city_groups = [
    [5, 6, 7],  # Group 0
    [2, 3],     # Group 1
    [1, 9],     # Group 2
    [4, 8]      # Group 3
]

# Calculate Euclidean distances between each pair of cities
def calculate_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)

# Create a dictionary to hold the distances
distances = {}
for i in range(len(city_coordinates)):
    for j in range(len(city_offset)):
        if i != j:
            distances[(i, j)] = calculate_distance(city_coordinates[i], city_coordinates[j])

# Initialize the MILP problem
problem = pulp.LpProblem("RobotRoutingProblem", pulp.LpMinimize)

# Variables: x[i, j] = 1 if city i is connected to city j in the tour
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(10) for j in range(10) if i != j), cat='Binary')
u = pulp.LpVariable.dicts("u", (i for i in range(2, 10)), lowBound=0)

# Objective: Minimize the total cost of the tour
problem += pulp.lpSum(distances[i, j] * x[i, j] for i in range(10) for j in range(10) if i != j), "TotalCost"

# Constraints to ensure each group has exactly one outgoing and incoming connection outside the group
for group in city_groups:
    problem += pulp.lpSum(x[i, j] for i in group for j in range(10) if j not in group) == 1, f"outgoing_group{group}"
    problem += pulp.lpSum(x[j, i] for i in group for j in range(10) if j not in group) == 1, f"incoming_group{group}"

# Enforce continuity in the route
for k in range(10):
    problem += pulp.lpSum(x[k, j] for j in range(10) if j != k) == pulp.lpSum(x[i, k] for i in range(10) if i != k), f"continuity_{k}"

# Subtour elimination constraints
for i in range(2, 10):
    for j in range(2, 10):
        if i != j:
            problem += u[i] - u[j] + (len(city_coordinates) - 1) * x[i, j] <= len(city_coordinates) - 2, f"subtour_constraint_{i}_{j}"

# Solve the problem
problem.solve()

# Check if there is an optimal solution
if problem.status == pulp.LpStatusOptimal:
    tour = []
    for i in range(10):
        for j in range(10):
            if x[i, j].varValue == 1:
                tour.append((i, j))

    # Print the ordered tour by following the path from the depot
    current_city = 0
    optimal_tour = [current_city]
    visited = set(optimal_tour)
    total_travel_cost = 0
    while True:
        next_step = [j for i, j in tour if i == current_city and j not in visited]
        if not next_step:
            break
        next_city = next_step[0]
        optimal_tour.append(next_city)
        total_travel_cost += distances[current_city, next_city]
        current_city = next_city
        visited.add(current_city)

    # Connect back to the depot
    optimal_tour.append(0)
    total_travel_cost += distances[current_city, 0]

    print("Tour:", optimal_tour)
    print("Total travel cost:", total_travel_dict)
else:
    print("No optimal solution found.")