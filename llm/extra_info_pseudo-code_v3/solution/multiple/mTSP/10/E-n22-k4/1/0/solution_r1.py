import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def nearest_neighbor_tour(starting_city, cities, coordinates):
    current_city = starting_city
    tour = [current_city]
    remaining_cities = set(cities)
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: euclidean_distance(coordinates[current_city], coordinates[city]))
        tour.append(next_city)
        current_city = next_city
        remaining_cities.remove(next_city)
    tour.append(starting_city)  # Complete the tour by returning to the depot
    return tour

def partition_cities(num_robots, cities):
    """ Simple partitioning of cities approximately equally """
    return [cities[i::num_robots] for i in range(num_robots)]

def calculate_total_distance(tour, coordinates):
    return sum(euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]]) for i in range(len(tour)-1))

# Input coordinates and number of robots
coordinates = [
    (145, 215), # Depot city 0
    (151, 264), # City 1
    ...
    (139, 182) # City 21
]
num_robots = 4
cities = list(range(1, len(coordinates)))  # excluding the depot city

# Partitions cities for each robot and computes their tours
city_partitions = partition_cities(num_robots, cities)
robot_tours = [nearest_neighbor_tour(0, partition, coordinates) for partition in city_partitions]

# Display tours and costs
overall_total_cost = 0
for idx, tour in enumerate(robot_tours):
    tour_cost = calculate_total_distance(tour, coordinates)
    overall_total_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost}")

print(f"Overall Total Travel Cost: {overall_total_cost}")