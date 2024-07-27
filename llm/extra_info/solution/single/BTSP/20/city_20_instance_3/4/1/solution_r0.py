import math

# Define the cities coordinates
cities = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57),
    5: (6, 58), 6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0),
    10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73),
    15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def find_tour(starting_city):
    unvisited = set(cities.keys()) - {starting_city}
    tour = [starting_city]
    current_city = starting_city
    total_distance = 0
    max_leg_distance = 0

    while unvisited:
        next_city = min(unvisited, key=lambda x: euclidean_distance(cities[current_city], cities[x]))
        distance = euclidean_distance(cities[current_city], cities[next_city])
        tour.append(next_city)
        total_distance += distance
        max_leg_distance = max(max_leg_distance, distance)
        current_city = next_city
        unvisited.remove(next_city)

    # Return to starting city
    return_to_depot_distance = euclidean_distance(cities[current_city], cities[starting_city])
    tour.append(starting_city)
    total_distance += return_to_depot_distance
    max_leg_distance = max(max_leg_distance, return_to_depot_distance)

    return tour, total_distance, max_leg_distance

# Calculate the tour
tour_result, total_travel_cost, maximum_distance_between_consecutive_cities = find_tour(0)

# Output the results
print("Tour:", tour_result)
print("Total travel cost:", total_travel_costs)
print("Maximum distance between consecutive cities:", maximum_distance_between_consecutive_cities)