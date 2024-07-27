import math
from itertools import permutations

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69)
}

num_robots = 8
robots = {i: [] for i in range(num_robots)}

# Simple assignment of cities to robots round-robin style
city_ids = list(cities.keys())[1:]  # Exclude the depot city (0)
for idx, city_id in enumerate(city_ids):
    robots[idx % num_robots].append(city_id)

# Function to calculate tour and cost for one robot
def calculate_tour_and_cost(robot_cities, start_city=0):
    path = [start_city]
    current_city = start_city
    total_cost = 0
    
    while robot_cities:
        next_city = min(robot_cities, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        total_cost += euclidean_distance(cities[current_city], cities[next_city])
        current_city = next_city
        path.append(current_city)
        robot_cities.remove(current_city)
    
    # Return to the start city
    total_cost += euclidean_distance(cities[current_city], cities[start_city])
    path.append(start_city)
    
    return path, total_cost

# Calculate tours and total travel cost
overall_total_cost = 0
for robot_id, robot_cities in robots.items():
    tour, cost = calculate_tour_and_cost(robot_cities[:])
    overall_total_cost += cost
    print(f"Robot {robot_id} Tour: {tour}")
    print(f"Robot {robot_id} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")