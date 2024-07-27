import math

# Cities and their coordinates
cities = {
    0: (8, 11), 1: (40, 6), 2: (95, 33), 3: (80, 60),
    4: (25, 18), 5: (67, 23), 6: (97, 32), 7: (25, 71),
    8: (61, 16), 9: (27, 91), 10: (91, 46), 11: (40, 87),
    12: (20, 97), 13: (61, 25), 14: (5, 59), 15: (62, 88),
    16: (13, 43), 17: (61, 28), 18: (60, 63), 19: (93, 15)
}

# Function to calculate Euclidean distance between two cities
def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

# Nearest Neighbor heuristic for TSP
def nearest_neighbor_tour(start_city):
    current_city = start_city
    tour = [current_city]
    unvisited_cities = set(cities.keys()) - {current_city}
    while unvisited_cities:
        next_city = min(unvisited_cities, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        current_city = next_city
        unvisited_cities.remove(current_city)
    tour.append(start_city)  # Return to the depot
    return tour

# Calculate total cost and maximum distance between consecutive cities
def tour_evaluation(tour):
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist
    return total_cost, max_distance

# Find the best tour starting from the depot
tour = nearest_neighbor_tour(0)
total_cost, max_distance = tour_evaluation(tour)

# Output the solution
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost}")
print(f"Maximum distance between consecutive cities: {max_distance}")