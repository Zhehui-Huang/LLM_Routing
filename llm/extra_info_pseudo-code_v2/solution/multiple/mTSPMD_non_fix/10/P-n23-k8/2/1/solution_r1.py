import random
import math

# City coordinates with index as city id
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

def euclidean_distance(c1, c2):
    """ Calculate Euclidean distance between two cities by their IDs. """
    return math.sqrt((cities[c1][0] - cities[c2][0]) ** 2 + (cities[c1][1] - cities[c2][1]) ** 2)

# Initialize robots with depot city as start
num_robots = 8
robot_tours = {i: [0] for i in range(num_robots)}  # all starting at depot city 0
visited = set([0])

# Assign remaining cities randomly to robots ensuring only one visitation
remaining_cities = list(cities.keys())[1:]  # Exclude the depot city 0
random.shuffle(remaining_cities)

for city in remaining_cities:
    available_robots = [r for r in range(num_robots) if r not in visited]
    chosen_robot = random.choice(available_robots)
    robot_tours[chosen_robot].append(city)
    visited.add(city)

# Adding depot city 0 again to close the loop for each robot
for r in range(num_robots):
    robot_tours[r].append(0)

def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

# Calculate and display tours and costs
total_cost = 0

for robot_id, tour in robot_tours.items():
    if len(tour) > 2:  # Only compute cost for robots that tour more than just the depot return.
        cost = calculate_tour_cost(tour)
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {cost}")
        total_cost += cost

print(f"Overall Total Travel Cost: {total_cost}")