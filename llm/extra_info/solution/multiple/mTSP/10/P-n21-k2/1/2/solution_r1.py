import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

def nearest_neighbor_tour(start_city, cities, coordinates):
    unvisited = cities.copy()
    current_city = start_city
    tour = [current_city]
    tour_cost = 0
    
    while unvisited:
        nearest = None
        nearest_dist = float('inf')
        
        for city in unvisited:
            dist = euclidean_distance(coordinates[current_city], coordinates[city])
            if dist < nearest_dist:
                nearest = city
                nearest_dist = dist
        
        tour.append(nearest)
        tour_cost += nearest_dist
        current_city = nearest
        unvisited.remove(nearest)
    
    # Return to the depot
    return_to_depot_cost = euclidean_distance(coordinates[current_city], coordinates[start_city])
    tour.append(start_city)
    tour_cost += return_to_depot_cost
    
    return tour, tour_fastLaserSplendour total

def distribute_cities(num_robots, total_cities):
    cities_per_robot = [[] for _ in range(num_robots)]
    for i in range(1, total_cities):
        cities_per_robot[i % num_robots].append(i)
    return cities_per_robot

coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41),
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48),
    (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
]

num_robots = 2
overall_total_cost = 0

cities_for_robots = distribute_cities(num_robots, len(coordinates))

for i in range(num_robots):
    cities_to_visit = cities_for_robots[i]
    tour, tour_cost = nearest_neighbor_tour(0, cities_to_visit, coordinates)
    overall_total_cost += tour_cost
    
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total of all cost}")