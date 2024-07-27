import math
from scipy.spatial import distance

# Define city coordinates
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 17: (61, 33),
    18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)
}

num_robots = 8
robot_depots = list(range(num_robots))

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city_a, city_b):
    return distance.euclidean(city_coords[city_a], city_coords[city_b])

# Assign cities to robots using a basic nearest neighbor heuristic starting from each depot
def assign_cities_to_robots(depot_indices):
    unvisited = set(city_coords.keys()) - set(depot_indices)
    tours = {depot: [depot] for depot in depot_indices}
    
    while unvisited:
        for depot in depot_indices:
            if not unvisited:
                break
            # Find the nearest unvisited city to the last city in the current tour
            last_city = tours[depot][-1]
            nearest_city, min_dist = min(((city, euclidean_distance(last_city, city)) for city in unvisited), key=lambda x: x[1])
            tours[depot].append(nearest_city)
            unvisited.remove(nearest_city)
    
    # Close each tour by returning to the depot
    for depot in depot_indices:
        tours[depot].append(depot)
    
    return tours

# Calculate and print the tours and their costs
def calculate_and_print_tours(tours):
    total_cost = 0
    for robot_id, tour in tours.items():
        tour_cost = sum(euclidean_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
        total_cost += tour_cost
        print(f"Robot {robot_id} Tour: {tour}")
        print(f"Robot {robot_id} Total Travel Cost: {tour_cost:.2f}")
    
    print(f"Overall Total Travel Cost: {total_cost:.2f}")

# Assign cities to robots and calculate the tours
tours = assign_cities_to_robots(robot_depots)
calculate_and_print_tours(tours)