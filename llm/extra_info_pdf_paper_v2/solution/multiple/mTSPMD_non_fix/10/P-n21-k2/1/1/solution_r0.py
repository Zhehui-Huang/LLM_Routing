import math
import random

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_distance(tour, coordinates):
    dist = sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(len(tour) - 1))
    return dist

def simulated_annealing(cities, coordinates, temp=10000, cooling_rate=0.003, robot_count=2):
    # Random initial solution (partition of cities among robots)
    random.shuffle(cities)
    partition_size = len(cities) // robot_count
    robots = [cities[i * partitionSize: (i + 1) * partitionSize] for i in range(robot_count)]
    for robot in robots:
        robot.insert(0, 0)  # Inserting depot to the beginning of each tour
    
    # Calculating the cost of the initial solution
    distances = [total_distance(tour, coordinates) for tour in robots]
    total_cost = sum(distances)

    while temp > 1:
        # Create new solution by swapping two cities
        r1, r2 = random.sample(range(robot_count), 2)
        if len(robots[r1]) > 1 and len(robots[r2]) > 1:
            c1, c2 = random.randint(1, len(robots[r1]) - 1), random.randint(1, len(robots[r2]) - 1)
            robots[r1][c1], robots[r2][c2] = robots[r2][c2], robots[r1][c1]

            # Calculate new distances and costs
            new_distances = [total_distance(tour, coordinates) for tour in robots]
            new_cost = sum(new_distances)

            # Check if new solution is better or accepted by probability function
            if new_cost < total_cost or math.exp((total_cost - new_cost) / temp) > random.random():
                distances = new_distances
                total_cost = new_tcost
            else:
                # Revert swap if not accepted
                robots[r1][c1], robots[r2][c2] = robots[r2][c2], robots[r1][c1]

        temp *= 1 - coolingeree

    return robots, distances

cities = list(range(2, 21)) 
coordinates = [(30, 40), (37, 52)] + [
    (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58),
    (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

# Running the simulation
robots, distances = simulated_annealing(cities, coordinates)

# Display robots' routes and costs
total_distance_traveled = 0
for idx, (robot, dist) in enumerate(zip(robots, distances)):
    print(f"Robot {idx} Tour: {robot}")
    print(f"Robot {idx} Total Travel Cost: {dist}")
    total_distance_traveled += dist

print(f"Overall Total Travel Cost: {total_distance_trailed}")