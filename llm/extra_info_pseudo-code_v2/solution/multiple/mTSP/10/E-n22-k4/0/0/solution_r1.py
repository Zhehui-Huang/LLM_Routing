import math

# City coordinates
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
    (155, 185), (139, 182)
]

# Number of robots/vehicles
num_vehicles = 4

# Distance function
def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Create distance matrix
distance_matrix = [
    [distance(coordinates[i], coordinates[j]) for j in range(len(coordinates))]
    for i in range(len(coordinates))
]

# Function to assign cities to vehicles using a round-robin approach
def assign_cities_to_vehicles(num_vehicles, num_cities):
    return {i: [j for j in range(1, num_cities) if (j - 1) % num_vehicles == i] for i in range(num_vehicles)}

cities_per_vehicle = assign_cities_to_vehicles(num_vehicles, len(coordinates))

# Nearest Neighbor tour construction
def nearest_neighbor_tour(start_city, cities):
    unvisited = set(cities)
    tour = [start_city]
    current_city = start_city
    
    while unvisited:
        next_city = min(unvisited, key=lambda city: distance_matrix[current_city][city])
        tour.append(next_city)
        current_city = next_city
        unvisited.remove(next_city)
    
    tour.append(start_city)
    return tour

# Tour cost calculation
def tour_cost(tour):
    return sum(distance_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))

# Context-based 2-opt optimization
def opt2(tour):
    improved = True
    while improved:
        improved = False
        for i in range(1, len(tour) - 2):
            for j in range(i+1, len(tour) - 1):
                new_dist = distance_matrix[tour[i]][tour[j]] + distance_matrix[tour[i+1]][tour[j+1]]
                old_dist = distance_matrix[tour[i]][tour[i+1]] + distance_matrix[tour[j]][tour[j+1]]
                if new_dist < old_dist:
                    tour[i+1:j+1] = reversed(tour[i+1:j+1])
                    improved = True
    return tour

# Main execution
tours = []
total_cost = 0
for vehicle, cities in cities_per_vehicle.items():
    tour = nearest_neighbor_tour(0, cities)
    optimized_tour = opt2(tour)
    cost = tour_cost(optimized_tour)
    total_cost += cost
    tours.append(optimized_tour)
    print(f"Robot {vehicle} Tour: {optimized_tour}")
    print(f"Robot {vehicle} Total Travel Cost: {cost}")

print(f"Overall Total Travel Cost: {total_cost}")