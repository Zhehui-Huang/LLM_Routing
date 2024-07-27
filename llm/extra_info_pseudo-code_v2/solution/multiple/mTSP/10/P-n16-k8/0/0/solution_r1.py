import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_length(tour, coords):
    return sum(euclidean_distance(coords[tour[i]], coords[tour[i+1]]) for i in range(len(tour) - 1))

def nearest_neighbor_tour(city_indices, coords, start_idx):
    unvisited = set(city_indices)
    tour = [start_idx]
    current = start_idx
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_dist(coords[x], coords[current]))
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)
    
    tour.append(start_mod)
    return tour

# Problem data
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
               (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)]
depot_index = 0
num_robots = 8
city_indices = list(range(1, len(coordinates)))  # cities excluding the depot

# Assign cities to each robot
partition_size = len(city_indices) // num_robots
city_partitions = [city_indices[i:i + partition_size] for i in range(0, len(city_indices), partition_size)]

# Determine tours for each robot
total_cost = 0
tours = []
for i in range(num_robots):
    if i < len(city_partitions):
        tour = nearest_neighbor_tour(city_partitions[i], coordinates, depot_index)
        tour_cost = calculate_tour_length(tour, coordinates)
        tours.append((tour, tour_cost))
        total_cost += tour_cost

# Output results
for idx, (tour, cost) in enumerate(tours):
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")