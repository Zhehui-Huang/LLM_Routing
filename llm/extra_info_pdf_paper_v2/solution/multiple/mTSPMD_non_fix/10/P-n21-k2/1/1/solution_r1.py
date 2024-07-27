import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))

def simulated_annealing(cities, coordinates, temp=10000, cooling_rate=0.003, robot_count=2):
    random.shuffle(cities)
    partition_size = len(cities) // robot_count
    robots = [cities[i * partition_size:(i + 1) * partition_size] for i in range(robot_count - 1)]
    robots.append(cities[(robot_count - 1) * partition_size:])  # Append remaining cities to last robot
    for robot in robots:
        robot.insert(0, 0)  # Each tour starts at depot city 0

    distances = [total_distance(robot, coordinates) for robot in robots]
    total_cost = sum(distances)

    while temp > 1:
        r1, r2 = random.sample(range(robot_count), 2)
        if len(robots[r1]) > 1 and len(robots[r2]) > 1:
            c1, c2 = random.randint(1, len(robots[r1]) - 1), random.randint(1, len(robots[r2]) - 1)
            robots[r1][c1], robots[r2][c2] = robots[r2][c2], robots[r1][c1]

            new_distances = [total_distance(robot, coordinates) for robot in robots]
            new_cost = sum(new_distances)

            if new_cost < total_cost or math.exp((total_cost - new_cost) / temp) > random.random():
                distances = new_distances
                total_cost = new_cost
            else:
                robots[r1][c1], robots[r2][c2] = robots[r2][c2], robots[r1][c1]

        temp *= 1 - cooling_rate

    return robots, distances

cities = list(range(2, 21))  # Cities excluding the depots
coordinates = [(30, 40), (37, 52)] + [
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

robots, distances = simulated_annealing(cities, coordinates)

# Display results
total_distance_traveled = 0
for idx, (robot, dist) in enumerate(zip(robots, distances)):
    print(f"Robot {idx} Tour: {robot}")
    print(f"Robot {idx} Total Travel Cost: {dist}")
    total_distance_traveled += dist

print(f"Overall Total Travel Cost: {total_distance_traveled}")