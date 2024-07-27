import math

# Coordinates of all 23 cities including depots
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

# Function to calculate the Euclidean distance between two cities
def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

# Function to provide the initial setup leveraging a Nearest Neighbor Algorithm
def nearest_neighbor_solution(depot, remaining_cities):
    tour = [depot]
    current_city = depot
    while remaining_cities:
        next_city = min(remaining_cities, key=lambda city: euclidean_distance(city_coords[current_city], city_coords[city]))
        tour.append(next_city)
        current_city = next_city
        remaining_cities.remove(next_city)
    return tour

# Number of robots available
num_robots = 8

# Generate a tour for each robot, starting from depot city 0
all_cities = set(range(23))
remaining_cities = list(all_cities - {0}) # Assuming all begin from 'depot city 0'
tours = []
robots = num_robots if num_robots <= len(remaining_cities) else len(remaining_cities)

for i in range(robots):
    # each robot's tour starts and stops without returning to initial depot
    if remaining_cities:
        tours.append(nearest_neighbor_solution(0, remaining_cities.copy()))

# Calculate and print tours
total_overall_cost = 0

for idx, tour in enumerate(tours):
    tour_cost = sum(euclidean_distance(city_coords[tour[i]], city_coords[tour[i+1]]) 
                    for i in range(len(tour)-1))
    total_overall_cost += tour_cost
    print(f"Robot {idx} Tour: {tour}")
    print(f"Robot {idx} Total Travel Cost: {tour_cost:.2f}")

print(f"Overall Total Travel Cost: {total_overall_cost:.2f}")