import numpy as np

# Cities' coordinates
coordinates = [(30, 40), (37, 52), (49, 43), (52, 64), (31, 62),
               (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
               (42, 57), (27, 68), (43, 67), (58, 27), (37, 69), 
               (61, 33), (62, 63), (63, 69), (45, 35)]

# Number of robots and their starting depots
num_robots = 2
depot_indices = [0, 1]

def euclidean_distance(city1, city2):
    return np.sqrt((coordinates[city1][0] - coordinates[city2][0]) ** 2 + (coordinates[city1][1] - coordinates[city2][1]) ** 2)

def nearest_neighbor_tour(start_city, cities_to_visit):
    unvisited = set(cities_to_visit)
    tour = [start_city]
    current_city = start_city

    while unvisited:
        next_city = min(universe - set(tour), key=lambda x: euclidean_distance(current_city, x))
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)

    return tour

def split_cities_among_robots():
    all_cities = set(range(len(coordinates)))
    robots_cities = [[] for _ in range(num_robots)]

    # Starting each robot's tour from their respective depots
    for i, depot in enumerate(depot_indices):
        robots_cities[i].append(depot)
        all_cities.remove(depot)

    # Distribute remaining cities to robots
    while all_cities:
        for i in range(num_robots):
            if not all_cities:
                break
            nearest = min(all_cities, key=lambda x: euclidean_distance(robots_cities[i][-1], x))
            robots_cities[i].append(nearest)
            all_cities.remove(nearest)
    
    return robots_cities

def calculate_tour_cost(tour):
    return sum(euclidean_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))

# Distribute cities to robots and calculate tours
robots_cities = split_cities_among_robots()
robots_tours = []
total_cost = 0

for i in range(num_robots):
    tour = nearest_neighbor_tour(depot_indices[i], robots_cities[i][1:])
    cost = calculate_tour_cost(tour)
    robots_tours.append((tour, cost))
    total_cost += cost

# Output results
for i, (tour, cost) in enumerate(robots_tours):
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost:.2f}")

print(f"Overall Total Travel Cost: {total_cost:.2f}")