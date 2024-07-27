import math

# Define the cities' coordinates
cities = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}

# Compute Euclidean distance between two cities
def distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

# Find the tour minimizing the maximum distance between consecutive cities
def find_minimax_tour():
    n = len(cities)
    unvisited = set(cities.keys())
    tour = [0]  # starting at the depot
    unvisited.remove(0)
    current_city = 0
    max_distance = 0
    total_cost = 0

    while unvisited:
        next_city = None
        min_increase = float('inf')

        # Find the closest city that minimizes the increase in max_distance
        for city in unvisited:
            d = distance(current_city, city)
            if d < min_increase:
                min_increase = d
                next_city = city

        tour.append(next_city)
        total_cost += min_increase
        max_distance = max(maxDistance, min_increase)
        current_city = next_city
        unvisited.remove(next_city)

    # closing the tour by returning to the start city
    return_to_depot_distance = distance(current_city, 0)
    tour.append(0)
    total_cost += return_to_depot_distance
    max_distance = max(max_distance, return_to_depot_distance)

    return tour, total_cost, max_distance

# Calculate the minimax tour
tour, total_cost, max_distance = find_minimax_tour()

# Print the results as required
print(f"Tour: {tour}")
print(f"Total travel cost: {total_cost:.2f}")
print(f"Maximum distance between consecutive cities: {max_distance:.2f}")