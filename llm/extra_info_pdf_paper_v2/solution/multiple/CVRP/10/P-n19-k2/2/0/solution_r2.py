import numpy as np

# Cities coordinates
coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), (61, 33),
    (62, 63), (63, 69), (45, 35)
]

# Demand for each city
demands = [0, 19, 30, 16, 23, 11, 31, 15, 28, 14, 8, 7, 14, 19, 11, 26, 17, 6, 15]

# Distance calculation function
def euclidean_distance(c1, c2):
    return np.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

# Prepare distance matrix
distance_matrix = np.zeros((len(coordinates), len(coordinates)))
for i in range(len(coordinates)):
    for j in range(len(coordinates)):
        distance_matrix[i, j] = euclidean_distance(coordinates[i], coordinates[j])

# Clarke-Wright Savings Algorithm
def clarke_wright(capacity):
    num_cities = len(coordinates)
    savings_list = []
    for i in range(1, num_cities):
        for j in range(i + 1, num_cities):
            savings_value = distance_matrix[0][i] + distance_matrix[0][j] - distance_matrix[i][j]
            savings_list.append(((i, j), savings_value))
    savings_list.sort(key=lambda x: x[1], reverse=True)

    tours = {i: [0, i, 0] for i in range(1, num_cities)}
    load = {i: demands[i] for i in range(1, num_cities)}

    for (i, j), _ in savings_list:
        if tours[i][1] == i and tours[j][-2] == j and load[i] + load[j] <= capacity:
            tours[i] = tours[i][:-1] + [j] + [0]
            load[i] += demands[j]
            del tours[j]
            del load[j]

    return tours

robot_capacity = 160
tours = clarke_wright(robot_capacity)

# Evaluate the tours and compute costs
total_cost = 0
rob_tours_details = []

for robot_index in range(2):
    if tours:
        tour_indices = list(tours.keys())
        tour = tours[tour_indices[0]]
        del tours[tour_indices[0]]
        tour_cost = sum([distance_matrix[tour[i]][tour[i + 1]] for i in range(len(tour) - 1)])
        total_cost += tour_cost
        rob_tours_details.append((robot_index, tour, tour_cost))
        print(f"Robot {robot_index} Tour: {tour}")
        print(f"Robot {robot_index} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {total_cost}")