import math

# Data setup
coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33),
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [
    0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11,
    12, 26, 17, 6, 15, 5, 10
]

# Problem configuration
num_robots = 8
robot_capacity = 40

# Calculate Euclidean distance
def euclidean_distance(a, b):
    return math.sqrt((coordinates[a][0] - coordinates[b][0]) ** 2 + (coordinates[a][1] - coordinates[b][1]) ** 2)

# Greedy algorithm to make initial assignments
tours = [[] for _ in range(num_robots)]
robot_loads = [0] * num_robots
remaining_cities = set(range(1, len(coordinates)))  # exclude the depot city

while remaining_cities:
    assigned = False
    for robot in range(num_robots):
        if not assigned:
            closest_distance = float('inf')
            closest_city = None
            for city in remaining_cities:
                if demands[city] + robot_loads[robot] <= robot_capacity:
                    distance = euclidean_distance(tours[robot][-1] if tours[robot] else 0, city)
                    if distance < closest_distance:
                        closest_distance = distance
                        closest_city = city
            if closest_city is not None:
                if tours[robot]:
                    tours[robot].append(closest_city)
                else:
                    tours[robot].extend([0, closest_city])
                robot_loads[robot] += demands[closest_city]
                remaining_cities.remove(closest_city)
                assigned = True

# Close all tours by returning to the depot
for tour in tours:
    if tour:
        tour.append(0)

# Calculate the total travel cost
total_cost = 0
output_details = []

for i, tour in enumerate(tours):
    if tour:
        tour_cost = sum(euclidean_distance(tour[j], tour[j + 1]) for j in range(len(tour) - 1))
        total_cost += tour_cost
        output_details.append(f"Robot {i} Tour: {tour}")
        output_details.append(f"Robot {i} Total Travel Cost: {tour_cost:.2f}")

output_details.append(f"Overall Total Travel Cost: {total_cost:.2f}")

for detail in output_details:
    print(detail)