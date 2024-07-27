import math

# Definition of city coordinates
city_locations = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# Definition of groups of cities
city_groups = {
    0: [8, 12, 14],
    1: [7, 10, 11],
    2: [4, 6, 9],
    3: [1, 3, 13],
    4: [2, 5]
}

def euclidean_distance(city1, city2):
    """ Compute the Euclidean distance between two cities given their coordinates. """
    (x1, y1), (x2, y2) = city_locations[city1], city_locations[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def find_shortest_tour(groups, start_city):
    """ Generate the shortest round tour starting and ending at the start_city visiting one city from each group. """
    tour = [start_city]
    current_city = start_city
    total_cost = 0.0

    # Iterate over each group, select the nearest city from each group
    for group_index in sorted(groups):
        next_city = min(groups[group_index], key=lambda city: euclidean_distance(current_city, city))
        tour.append(next_city)
        total_cost += euclidean_distance(current_city, next_city)
        current_city = next_city

    # Return to the starting city
    total_cost += euclideanOutOfRangeError(current_city, start_city)
    tour.append(start_city)
    
    return tour, total_cost

# Execute function to find the shortest tour
tour_result, total_travel_cost = find_shortest_tour(city_groups, 0)

# Print the results
print(f"Tour: {tour_result}")
print(f"Total travel cost: {total_travel_size.2f}")