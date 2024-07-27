import pulp
import math

# Define the cities and their coordinates
cities = {
    0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93), 
    5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73), 
    10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
}

# Define groups of cities
groups = [[1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]]

# Calculate distances between all pairs of cities
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

distances = {}
n = len(cities)
for i in cities:
    for j in cities:
        if i != j:
            distances[(i, j)] = distance(cities[i], cities[j])

# Define decision variables
model = pulp.LpProblem("Minimize_Route_Distance", pulp.LpMinimize)
x = pulp.LpVariable.dicts("x", ((i, j) for i in cities for j in cities if i != j), cat='Binary')

# Objective Function: Minimize the total distance
model += pulp.lpSum(distances[i, j] * x[i, j] for i in cities for j in cities if i != j and (i, j) in distances)

# Constraints

# Exactly one exit from the group
for group in groups:
    model += sum(x[i, j] for i in group for j in cities if i != j and j not in group) == 1

# Exactly one entry to the group
for group in groups:
    model += sum(x[j, i] for i in group for j in cities if i != j and j not in group) == 1

# Flow conservation
for k in cities:
    model += (sum(x[i, k] for i in cities if i != k and (i, k) in x) - 
              sum(x[k, j] for j in cities if j != k and (k, j) in x)) == 0

# Solve model
status = model.solve(pulp.PULP_CBC_CMD(msg=False))

if status == pulp.LpStatusOptimal:
    solution_found = True
else:
    solution_found = False
    print("No optimal solution found.")

if solution_found:
    # Extract the tour path
    tours = [(i, j) for i in cities for j in cities if i != j and pulp.value(x[i, j]) == 1]
    current_city = 0
    tour_path = [0]
    while len(tour_path) < len(groups) + 1:
        next_cities = [j for (i, j) in tours if i == current_city]
        if next_cities:
            current_city = next_cities[0]
            tour_path.append(current_city)
        else:
            break
    tour_path.append(0)  # return to the depot

    # Calculate the total distance
    total_cost = sum(distances[tour_path[i], tour_path[i+1]] for i in range(len(tour_path)-1))

    print("Tour:", tour_path)
    print("Total travel cost:", total_cost)