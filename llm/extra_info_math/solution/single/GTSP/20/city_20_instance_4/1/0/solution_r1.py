import pulp
import math

# City Coordinates
coordinates = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11),
    (70, 2), (47, 50), (60, 29), (29, 26), (85, 68), (60, 1), (71, 73),
    (82, 47), (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# City Groups
groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], [1, 3, 9],
    [2, 4, 14], [10, 17], [7, 15]
]

num_cities = len(coordinates)
num_groups = len(groups)

def euclidean_distance(coords1, coords2):
    return math.sqrt((coords1[0] - coords2[0])**2 + (coords1[1] - coords2[1])**2)

distances = [[euclidean_distance(coordinates[i], coordinates[j]) for j in range(num_cities)]
             for i in range(num_cities)]

prob = pulp.LpProblem("TSP_Groups", pulp.LpMinimize)

x = pulp.LpVariable.dicts("x", ((i, j) for i in range(num_cities) for j in range(num_cities) if i != j),
                          cat='Binary')

prob += pulp.lpSum(distances[i][j] * x[i, j] for i in range(num_cities) for j in range(num_cities) if i != j)

# Ensuring each group has exactly one outgoing and incoming connection
for group in groups:
    prob += pulp.lpSum(x[i, j] for i in group for j in range(num_cities) if j not in group) == 1
    prob += pulp.lpSum(x[j, i] for i in group for j in range(num_cities) if j not in group) == 1

# Flow conservation for each city except depot
for i in range(1, num_cities):
    prob += pulp.lpSum(x[j, i] for j in range(num_cities) if j != i) \
            == pulp.lpSum(x[i, j] for j in range(num_cities) if j != i)

# Solving the problem
status = prob.solve(pulp.PULP_CBC_CMD(msg=False))

if status == pulp.LpStatusOptimal:
    print("Successfully optimized the tour.")
    tour = []
    tour_cost = 0
    current_node = 0
    tour.append(current_node)

    while True:
        next_node = None
        for j in range(num_cities):
            if j != current_node and x[current_node, j].varValue == 1:
                next_node = j
                break
        if next_node is None or next_node == 0:
            break
        tour.append(next_node)
        tour_cost += distances[current_node][next_node]
        current_node = next_node

    # Completing the tour by returning to the depot
    tour.append(0)
    tour_cost += distances[current_node][0]

    print(f"Tour: {tour}")
    print(f"Total travel cost: {tour_cost}")
else:
    print("Unable to find optimal solution.")