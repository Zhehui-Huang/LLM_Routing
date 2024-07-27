import math

def euclidean_distance(city1, city2):
    x1, y2 = city1
    x2, y2 = city2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def nearest_neighbor_tour(start, cities, city_coordinates):
    tour = [start]
    current = start
    unvisited = set(cities) - {start}

    while unvisited:
        next_city = min(unvisited, key=lambda city: euclidean_distance(city_coordinates[current], city_coordinates[city]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city

    tour.append(start)  # Return to depot
    return tour

def calculate_tour_cost(tour, city_coordinates):
    return sum(euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour) - 1))

def two_opt(tour, city_coordinates):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i + 1, len(tour) - 1):
                if euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[j]]) + euclidean_distance(city_coordinates[tour[i-1]], city_coordinates[tour[j+1]]) < euclidean_equal_distance(city_coordinates[tour[i]], city_coordinates[tour[i-1]]) + euclidean_distance(city_coordinates[tour[j]], city_coordinates[tour[j+1]]):
                    tour[i:j] = tour[j:i-1:-1]
                    improved = True
    return tour

# Assign cities to each robot based on closest depot
city_coordinates = [ (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35) ]
depot_0 = 0
depot_1 = 1
robot_0_cities = [depot_0]
robot_1_cities = [depot_1]

for i in range(2, len(city_coordinates)):
    if euclidean_distance(city_coordinates[i], city_coordinates[depot_0]) < euclidean_distance(city_coordinates[i], city_coordinates[depot_1]):
        robot_0_cities.append(i)
    else:
        robot_1_cities.append(i)

# Generate tours using nearest neighbor algorithm
tour_0 = nearest_neighbor_tour(depot_0, robot_0_cities, city_coordinates)
tour_1 = nearest_neighbor_tour(depot_1, robot_1_cities, city_coordinates)

# Optimize tours using 2-opt
optimized_tour_0 = two_opt(tour_0, city_coordinates)
optimized_tour_1 = two_opt(tour_1, city_coordinates)

# Calculate tour costs
cost_0 = calculate_tour_cost(optimized_tour_0, city_coordinates)
cost_1 = calculate_tour_cost(optimized_tour_1, city_coordinates)

# Print results
print("Robot 0 Tour:", optimized_tour_0)
print("Robot 0 Total Travel Cost:", cost_0)
print("Robot 1 Tour:", optimized_tour_1)
print("Robot 1 Total Travel