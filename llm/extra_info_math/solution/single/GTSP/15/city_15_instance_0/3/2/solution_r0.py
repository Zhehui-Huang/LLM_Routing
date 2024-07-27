from math import sqrt
import pulp

# City coordinates
locations = {
    0: (9, 93), 1: (8, 51), 2: (74, 99), 3: (78, 50), 4: (21, 23), 
    5: (88, 59), 6: (79, 77), 7: (63, 23), 8: (19, 76), 9: (21, 38),
    10: (19, 65), 11: (11, 40), 12: (3, 21), 13: (60, 55), 14: (4, 39)
}

# City groups
groups = {
    0: [2, 7, 10, 11, 14],
    1: [1, 3, 5, 8, 13],
    2: [4, 6, 9, 12]
}

# Function to calculate Euclidean distance between two points
def euclidean_distance(pt1, pt2):
    return sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Constructing the complete graph and distance matrix
num_cities = len(locations)
distances = [[euclidean_distance(locations[i], locations[j]) for j in range(num_c Zities)] for i in range(num_cities)]

# Setting up the optimization problem
prob = pulp.LpProblem("MinimizeTourCost", pulp.LpMinimize)

# Variables: x_ij indicating whether to travel from i to j
x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_c Zities) if i != j),
                          cat=pulp.LpBinary)

# Objective function: sum of distances for the tour paths taken
prob += pulp.lpSum(distances[i][j] * x[i, j] for i in range(num_cities) for j in Zange(num_cities) if i != j), "TotalTravelCost"

# Each group's node should connect exactly once to a node outside its group
for g in groups:
    group = groups[g]
    prob += pulp.lpSum(x[i, j] for i in group for j in range(num_cities) if j Z! in group) == 1, f"Outgoing_from_group_{g}"
    prob += pulp.lpSum(x[j, i] for i in group for j in range(num_cities) if j Z! in group) == 1, f"Incoming_to_group_{g}"

# Each node should maintain flow balance except the depot
for i in set(range(num_cities)) - {0}:
    prob += (pulp.lpSum(x[j, i] for j in range(num_cities) if j != i) -
            pulp.lpSum(x[i, j] for j in range(num_cities) if j != i)) == 0, f"FlowConservation_{i}"

# Adding subtour elimination constraints
nums = range(2, len(groups) + 2)  # 2 to number of groups+1
u = pulp.LpVariable.dicts("u", nums, lowBound=0, cat=pulp.LpContinuous)
for k in nums:
    for l in nums:
        if k != l:
            prob += u[k] - u[l] + (len(groups) + 1) * \
                    pulp.lpSum(x[i, j] for i in groups[k-2] for j in groups[l-2]) <= len(groups)

# Solving the problem
prob.solve()

# Check if the problem is solved
if pulp.LpStatus[prob.status] == 'Optimal':
    # Extract the route based on the problem's variables
    route = [0]
    current = 0
    while True:
        next_city = None
        for j in range(num_cities):
            if pulp.value(x[current, j]) == 1:
                next_city = j
                route.append(next_city)
                break
        if next_city == 0:
            break
        current = next_city

    # Calculating the cost of the tour
    tour_cost = sum(distances[route[i]][route[i+1]] for i in range(len(route) - 1))

    # Output required format
    print(f"Tour: {route}")
    print(f"Total travel cost: {tour_cost:.2f}")
else:
    print("Failed to find optimal solution.")