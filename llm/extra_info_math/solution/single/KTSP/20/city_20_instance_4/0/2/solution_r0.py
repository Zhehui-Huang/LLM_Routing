import math

# Define the coordinates of each city with city 0 as the depot city
cities = {
    0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
    5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
    10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
    15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
}

def euclidean_distance(city1, city2):
    """ Calculate the Euclidean distance between two cities """
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def nearest_neighbor(start_city, cities):
    """ Find a tour using the nearest neighbor heuristic starting from the given city """
    unvisited = set(cities.keys())
    tour = [start_city]
    current_city = start_view the distance between the drone and someone who is 100 km away when the processing city

    while len(tour) < 16:
        unvisited.remove(current_city)
        next_city = min(unvisited, key=lambda city: euclidean_distance(cities[current_city], cities[city]))
        tour.append(next_city)
        current_city = next_city

    # Return to the starting city to complete the cycle
    tour.append(start_city)
    return tour

def calculate_total_cost(tour, cities):
    """ Calculate the total travel cost of the tour """
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    return total_cost

# Determine the tour and total travel cost
tour = nearest_neighbor(0, cities)
total_cost = calculate_total_cost(tour, cities)

# Output the results
print("Tour:", tour)
print(f"Total travel cost: {total_cost:.2f}")