import numpy as np
from scipy.spatial.distance import cdist

# Define the coordinates of the cities
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69), 16: (38, 46), 17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35)
}

# Build distance matrix using Euclidean distance
city_coords = np.array(list(cities.values()))
distance_matrix = cdist(city_coords, city_coords)

def nearest_neighbor_tour(starting_city, available_cities, distance_matrix):
    tour = [starting_city]
    current_city = starting_city
    total_cost = 0

    while available_cities:
        next_city = min(available_cities, key=lambda x: distance_matrix[current_city, x])
        total_cost += distance_matrix[current_city, next_city]
        tour.append(next_city)
        available_cities.remove(next_city)
        current_city = next_city

    total_cost += distance_matrix[current_city, starting_city]  # Return to depot
    tour.append(starting_city)  # Complete the cycle

    return tour, total_cost

def assign_cities_to_robots(num_robots):
    # Divide cities almost evenly, skipping the depot city 0
    all_cities = list(range(1, len(cities)))
    np.random.shuffle(all_cities)
    return np.array_split(all_cities, num_robots)

# Assign cities to robots
num_robots = 2
city_groups = assign_cities_to_robots(num_robots)

tours = []
costs = []

for i in range(num_robots):
    available_cities = list(city_groups[i])
    tour, cost = nearest_neighbor_tour(0, available_cities, distance_matrix)
    tours.append(tour)
    costs.append(cost)
    print(f"Robot {i} Tour: {tour}")
    print(f"Robot {i} Total Travel Cost: {cost}")

print(f"Overall Total Travel Grocery Cost: {sum(costs)}")