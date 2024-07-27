import math
from itertools import permutations

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_tour_length(tour, coord):
    return sum(euclidean_distance(coord[tour[i]], coord[tour[i+1]]) for i in range(len(tour) - 1))

def nearest_neighbor_tour(city_indices, coord, start_idx):
    unvisited = set(city_indices)
    tour = [start_idx]
    current = start_idx
    unvisited.remove(start_idx)
    
    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(coord[current], coord[x]))
        tour.append(next_city)
        current = next_city
        unvisited.remove(current)
    
    tour.append(start_idx)  # Return to depot
    return tour

def partition_cities(city_indices, num_robots):
    chunks = [city_indices[i::num_robots] for i in range(num_robots)]
    return chunks

# Define the city coordinates
coordinates = [(30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
               (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
               (43, 67), (58, 48), (58, 27), (37, 69)]
depot_idx = 0
num_robots = 8

# Exclude the depot from the list of city indices
city_indices = list(range(1, len(coordinates)))

# Partition cities among the robots
city_partitions = partition_cities(city_indices, num_robots)
tours = []
total_cost = 0

for idx, cities in enumerate(city_partitions):
    tour = nearest_neighbor_tour(cities, coordinates, depot_idx)
    tours.append(tour)
    
# Calculate and output the results
for idx, tour in enumerate(tours):
    cost = calculate_tour_length(tour, coordinates)
    total_cost += cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {round(cost, 2)}")

print(f"Overall Total Travel Cost: {round(total_cost, 2)}")