import math
import pulp

# Define the city coordinates
coordinates = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Define city groups
groups = {
    0: [1, 6, 14], 1: [5, 12, 13], 2: [7, 10], 3: [4, 11],
    4: [2, 8], 5: [3, 9]
}

# Distance function between two points
def distance(city1, city2):
    x1, y1 = coordinates[city1]
    x2, y2 = coordinates[city2]
    return math.hypot(x2 - x1, y2 - y1)

# Initializing the optimization problem
prob = pulp.LpProblem("Minimize_Tour_Cost", pulp.LpMinimize)

# Decision variables
x = {(i, j): pulp.LpVariable(f"x_{i}_{j}", cat='Binary') for i in coordinates for j in coordinates if i != j}

# Objective function: Minimize total distance traveled
prob += pulp.lpSum(x[i, j] * distance(i, j) for i in coordinates for j in coordinates if i != j), "Total_Distance"

# Every group has exactly one outgoing and one incoming connection
for group in groups.values():
    prob += pulp.lpSum(x[0, j] for j in group) == 1, f"One_outgoing_from_depot_to_group"
    prob += pulp.lpSum(x[j, 0] for j in group) == 1, f"One_incoming_to_depot_from_group"

# Each city (except depot) has one incoming and one outgoing connection
for city in coordinates:
    if city != 0:
        prob += pulp.lpSum(x[i, city] for i in coordinates if i != city) == 1, f"Incoming_to_{city}"
        prob += pulp.lpSum(x[city, j] for j in coordinates if j != city) == 1, f"Outgoing_from_{city}"

# Solve the problem
prob.solve()

# Check the status of the solution
if pulp.LpStatus[prob.status] == 'Optimal':
    # Construct the tour from the solution
    tour = []
    current_city = 0
    count = 0
    while count <= len(coordinates):
        tour.append(current_city)
        next_cities = [j for j in coordinates if pulp.value(x[current_city, j]) == 1]
        if not next_cities:
            break
        current_city = next_cities[0]
        count += 1
    tour.append(0)  # ensure returning to the depot

    # Total travel cost calculation
    total_cost = sum(distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

    print("Tour:", tour)
    print("Total travel cost:", round(total_cost, 2))
else:
    print("No optimal solution found.")