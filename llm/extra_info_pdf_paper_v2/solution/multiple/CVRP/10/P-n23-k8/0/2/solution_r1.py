import math

# Given city coordinates and demands
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]

# Robot specifications
num_robots = 8
capacity = 40

# Function to compute Euclidean distance between two cities
def distance(i, j):
    xi, yi = coordinates[i]
    xj, yj = coordinates[j]
    return math.sqrt((xi - xj) ** 2 + (yi - yj) ** 2)

# Initialize tours and loads for each robot
tours = {k: [0] for k in range(num_robots)}
load = {k: 0 for k in range(num_robots)}

# Assign cities to robots based on demands and capacity
unassigned_cities = list(range(1, len(coordinates)))  # City 0 is depot

while unassigned_cities:
    for robot in range(num_robots):
        if not unassigned_cities:
            break
        next_city = min(unassigned_cities, key=lambda x: distance(tours[robot][-1], x))
        if load[robot] + demands[next_city] <= capacity:
            tours[robot].append(next_city)
            load[robot] += demands[next_city]
            unassigned_cities.remove(next_city)

# Close the tours by returning to the depot
for robot in range(num_robots):
    if tours[robot][-1] != 0:
        tours[robot].append(0)  # Ensure returning to depot

# Calculate and print the travel cost for each tour and the total cost
overall_total_cost = 0
for robot in range(num_robots):
    tour_cost = sum(distance(tours[robot][i], tours[robot][i + 1]) for i in range(len(tours[robot]) - 1))
    print(f"Robot {robot} Tour: {tours[robot]}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")
    overall_total_cost += tour_cost

print(f"Overall Total Travel Cost: {overall_total_cost}")