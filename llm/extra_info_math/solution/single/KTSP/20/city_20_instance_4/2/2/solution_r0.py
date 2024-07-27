import math

# Define cities coordinates
cities = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), (69, 22), (28, 11), (70, 2), (47, 50),
    (60, 29), (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), (19, 25), (75, 9), (52, 54),
    (64, 72), (14, 89)
]

# Number of cities to visit including the depot
k = 16

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def nearest_neighbor_tour(start_city, num_cities_to_visit):
    visited = set([start_city])
    tour = [start_city]
    current_city = start_city

    while len(visited) < num_cities_to_visit:
        next_city = None
        min_distance = float('inf')

        for city_index in range(len(cities)):
            if city_index not in visited:
                distance = euclidean_distance(cities[current_city], cities[city_index])
                if distance < min_distance:
                    min_distance = distance
                    next_city = city_index

        visited.add(next_city)
        tour.append(next_city)
        current_city = next_city

    # Closing the tour by returning to the start city
    tour.append(start_city)
    tour_cost = sum(euclidean_distance(cities[tour[i]], cities[tour[i+1]]) for i in range(len(tour)-1))
    
    return tour, tour_cost

# Compute the tour and its cost
optimal_tour, total_cost = nearest_neighbor_tour(0, k)

# Output the results
print("Tour:", optimal_tour)
print("Total travel cost:", round(total_cost, 2))