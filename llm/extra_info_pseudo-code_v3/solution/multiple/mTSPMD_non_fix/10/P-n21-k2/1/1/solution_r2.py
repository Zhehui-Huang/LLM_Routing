import math

# City coordinates data
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35)
}

number_of_robots = 2
depots = [0, 1]

def euclidean_distance(a, b):
    """Compute the Euclidean distance between two points."""
    x1, y1 = city_coords[a]
    x2, y2 = city_coords[b]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def nearest_neighbor_tour(start_city, other_cities):
    """Generate a tour starting from a given city using the nearest neighbor heuristic."""
    tour = [start_city]
    current_city = start_city
    local_unvisited_cities = other_cities.copy()
    
    while local_unvisited_cities:
        next_city = min(local_unvisited_cities, key=lambda x: euclidean_distance(current_city, x))
        tour.append(next_city)
        local_unvisited_cities.remove(next_city)
        current_city = next_city
        
    return tour

# Distribute cities between robots
remaining_cities = set(city_coords.keys()) - set(depots)
robot_tours = []

for i in range(number_of_robots):
    cities_per_robot = len(remaining_cities) // (number_of_robots - i)
    assigned_cities = set(random.sample(remaining_cities, cities_per_robot))
    remaining_cities -= assigned_cities
    tour = nearest_neighbor_tour(depots[i], assigned_cities)
    robot_tours.append(tour)

# Calculate the cost for each robot's tour
def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))

robot_costs = [calculate_tour_cost(tour) for tour in robot_tours]
overall_cost = sum(robot_costs)

# Output results
for i, tour in enumerate(robot_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {robot_costs[i]:.2f}")

print(f"Overall Total Travel Cost: {overall_cost:.2f}")