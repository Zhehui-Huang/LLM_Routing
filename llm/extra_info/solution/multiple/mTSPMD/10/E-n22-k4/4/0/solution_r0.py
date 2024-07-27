import math

# Define the cities and their coordinates
city_coords = {
    0: (145, 215), 1: (151, 264), 2: (159, 261), 3: (130, 254), 4: (128, 252),
    5: (163, 247), 6: (146, 246), 7: (161, 242), 8: (142, 239), 9: (163, 236),
    10: (148, 232), 11: (128, 231), 12: (156, 217), 13: (129, 214), 14: (146, 208),
    15: (164, 208), 16: (141, 206), 17: (147, 193), 18: (164, 193), 19: (129, 189),
    20: (155, 100), 21: (139, 182)
}

# Define robots and their depots
robot_depots = {0: 0, 1: 1, 2: 2, 3: 3}
number_of_robots = 4

# The Euclidean distance calculator
def euclidean_distance(city1, city2):
    return math.sqrt((city_coords[city1][0] - city_loc[city2][0]) ** 2 + (city_coords[city1][1] - city_loc[city2][1]) ** 2)

# Assign cities to each robot based on the nearest depot heuristic (greedy)
city_assignment = {r: [d] for r, d in robot_depots.items()}
remaining_cities = list(set(city_coords.keys()) - set(robot_depots.values()))

for city in remaining_cities:
    closest_robot = min(robot_depots, key=lambda r: euclidean_distance(city, robot_depots[r]))
    city_assignment[closest_robot].append(city)

# Function to compute the path using the nearest neighbor algorithm for each robot
def compute_tour(cities):
    start_city = cities[0]
    path = [start_city]
    available_cities = cities[1:]
    current_city = start_city
    
    while available_cities:
        next_city = min(available_cities, key=lambda c: euclidean_distance(current_city, c))
        path.append(next_city)
        available_cities.remove(next_city)
        current_city = next_city
    
    path.append(start_city)  # return to starting depot
    return path

# Compute the paths and costs
total_cost = 0
robot_tours = {}
for robot, cities in city_assignment.items():
    tour = compute_tour(cities)
    robot_tours[robot] = tour
    
    # Calculate cost for this tour
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += euclidean_distance(tour[i], tour[i+1])
    
    print(f"Robot {robot} Tour: {tour}")
    print(f"Robot {robot} Total Travel Cost: {tour_cost}")
    total_cost += tour_cost

print(f"Overall Total Travelpage Cost: {total_cost}")