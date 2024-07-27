import pulp
import math

# Define cities and their coordinates
cities = {
    0: (84, 67), 1: (74, 40), 2: (71, 13), 3: (74, 82), 4: (97, 28),
    5: (0, 31), 6: (8, 62), 7: (74, 56), 8: (85, 71), 9: (6, 76)
}

# Define groups
groups = {0: [7, 9], 1: [1, 3], 2: [4, 6], 3: [8], 4: [5], 5: [2]}

# Calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

# Create the problem instance
model = pulp.LpProblem("TSP", pulp.LpMinimize)

# Variables: x_ij = 1 if the robot travels from city i to city j
x = pulp.LpVariable.dicts("x", [(i, j) for i in cities for j in cities if i != j], cat='Binary')

# Objective function: minimize the total traveling distance
model += pulp.lpSum(euclidean_distance(i, j) * x[(i, j)] for i in cities for j in cities if i != j), "Total_Distance"

# Constraints for depot and groups
group_flows = {i: [] for i in cities.keys()}  # Maps each city to its relevant flows
model += pulp.lpSum(x[(0, j)] for j in cities if j != 0) == 1
model += pulp.lpSum(x[(j, 0)] for j in cities if j != 0) == 1

for group, members in groups.items():
    # One outgoing edge from each group
    model += pulp.lpSum(x[(i, j)] for i in members for j in cities if j not in members) == 1
    # One incoming edge to each group
    model += pulp.lpSum(x[(j, i)] for i in members for j in cities if j not in members) == 1
    
    for m in members:
        group_flows[m] = [(i, m) for i in cities if i != m] + [(m, j) for j in cities if j != m]

# Flow conservation
for k in cities:
    if k != 0:
        # Net flow into each city except depot should be zero
        model += pulp.lpSum(x[(i, k)] for i in cities if i != k) == pulp.lpSum(x[(k, j)] for j in cities if j != k)

status = model.solve()
print("Status:", pulp.LpStatus[status])

# Output results
if status == 1:
    tour = [0]
    current_city = 0
    total_cost = 0

    for _ in range(len(cities)):
        next_city = None
        for j in cities:
            if j != current_city and pulp.value(x[(current_city, j)]) == 1:
                next_city = j
                tour.append(next_city)
                total_cost += euclidean_distance(current_city, next_city)
                current_city = j
                break
        if next_city == 0:  # End at depot
            break
    
    print("Tour:", tour)
    print("Total travel cost:", total_cost)
else:
    print("No feasible solution found.")