import math

def euclidean_distance(c1, c2):
    """Calculates the Euclidean distance between two points."""
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_length(tour, coords):
    """Calculates the total tour length."""
    return sum(euclidean_distance(coords[tour[i]], coords[tour[i+1]]) for i in range(len(tour) - 1))

def nearest_neighbor_tour(city_indices, coords, start_idx):
    """Creates a tour using the nearest neighbor heuristic."""
    unvisited = set(city_indices)
    tour = [start_idx]
    current = start_idx
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(coords[current], coords[x]))
        tour.append(next_city)
        unvisited.remove(next_city)
        current = next_city
    
    tour.append(start_idx)  # Return to depot
    return tour

# Coordinates of the cities including the depot city (0)
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69)]
num_robots = 8
depot_idx = 0
city_indices = list(range(1, len(coordinates)))  # Exclude the depot from city indices

# Partition cities into approximately equal parts for each robot
partition_size = (len(city_utils) + num_robots - 1) // num_robots # ceiling division
city_partitions = [city_indices[i:i + partition_size] for i in range(0, len(city_indices), partition_size)]

# Calculating tours and costs for each robot
overall_total_cost = 0
for i, cities in enumerate(city_partitions):
    if cities:
        tour = nearest_neighbor_tour(cities, coordinates, depot_idx)
        tour_cost = calculate_tour_length(tour, coordinates)
        overall_total_cost += tour_cost
        
        print(f"Robot {i} Tour: {tour}")
        print(f"Robot {i} Total Travel Cost: {round(tour_cost, 2)}")

print(f"Overall Total Travel Cost: {round(overall_total_cost, 2)}")