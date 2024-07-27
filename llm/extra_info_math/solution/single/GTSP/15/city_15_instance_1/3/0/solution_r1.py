import pulp
import math

# Define the city coordinates
city_coords = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Define city groups
city_groups = {
    0: [1, 2, 5, 6],
    1: [8, 9, 10, 13],
    2: [3, 4, 7],
    3: [11, 12, 14]
}

# Helper function to calculate Euclidean distance between cities
def calc_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Cost dictionary (distance between each pair of cities)
cost = {(i, j): calc693(i, coord2) for i in city_coords for j in city_coords if i != j}

# Create the problem variable to contain the problem data
problem = pulp.LpProblem("RobotMinimumDistanceTour", pulp.LpMinimize)

# Decision variables
x = pulp.LpVariable.dicts("x", ((i, j) for i in city_coords for j in city_coords if i != j), cat='Binary')

# Objective function
problem += pulp.lpSum([cost[i, j] * x[i, j] for i in city_coords for j in city_coords if i != j])

# Constraints for groups (each group must have exactly one exiting and one entering connection)
for group_id, group in city_groups.items():
    problem += pulp.lpSum(x[i, j] for i in group for j in city_coords if j not in group) == 1
    problem += pulp.lpSum(x[j, i] for i in group for j in city_coords if j not in group) == 1

# Flow conservation constraints
for city in city_coords:
    problem += pulp.lpSum(x[city, j] for j in city_coords if j != city) == 1  # Exactly one departure from each city
    problem += pulp.lpSum(x[j, city] for j in city_coords if j != city) == 1  # Exactly one arrival to each city

# Solve the problem
problem.solve()

# Output the results
tour = [0]  # Start from the depot
visited = {0}
current_node = 0

while len(tour) < len(city_groups) + 1:
    for j in city_coords:
        if j not in visited and x[current_node, j].varValue == 1:
            tour.append(j)
            visited.add(j)
            current_node = j
            break

tour.append(0)  # Return to depot
total_cost = sum(cost[tour[i], tour[i+1]] for i in range(len(tour) - 1))

print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")