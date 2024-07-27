import numpy as  np

# City coordinates 
coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62),
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27),
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69),
    20: (45, 35), 21: (32, 39), 22: (56, 37)
}

def euclidean_distance(p1, p2):
    return np.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Determine distance matrix
distance_matrix = {}
for i in coordinates:
    distance_matrix[i] = {}
    for j in coordinates:
        distance_matrix[i][j] = euclidean_distance(coordinates[i], coordinates[j])

def nearest_neighbor_tour(start_city, cities, distance_matrix):
    tour = [start_city]
    current_city = start_city
    unvisited_cities = cities.copy()

    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda x: distance_matrix[current_city][x])
        tour.append(next_city)
        current_city = next_city
        unvisited_cities.remove(next_city)
    tour.append(start_city)
    return tour

def calculate_tour_cost(tour, distance_matrix):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour) - 1))

# Number of robots
num_robots = 8
city_ids = list(coordinates.keys())[1:]  # Exclude the depot city from the list of cities to visit
np.random.shuffle(city_ids)  # Shuffle city list for random initial distribution
cities_per_robot = len(city_ids) // num_robots

robot_tours = {}
total_cost = 0

for k in range(num_robots):
    start_index = k * cities_per_robot
    if k < num_robots - 1:
        assigned_cities = city_ids[start_index:start_index + cities_per_robot]
    else:
        # Last robot takes the remainder of cities
        assigned_cities = city_ids[start_index:]
        
    tour = nearest_neighbor_tour(0, assigned_cities, distance_matrix)
    tour_cost = calculate_tour_cost(tour, distance_matrix)
    robot_tours[k] = {'tour': tour, 'cost': tour_cost}
    total_cost += tour_cost

# Output the results
for robot_id, tour_info in robot_tours.items():
    print(f"Robot {robot_id} Tour: {tour_info['tour']}")
    print(f"Robot {robot_id} Total Travel Cost: {tour_info['cost']:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")