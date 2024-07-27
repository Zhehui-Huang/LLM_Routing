import math

# City coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Solution provided
tours = [
    [0, 13, 9, 0],
    [0, 15, 12, 0],
    [0, 6, 0],
    [0, 4, 11, 0],
    [0, 5, 14, 0],
    [0, 8, 3, 0],
    [0, 1, 10, 0],
    [0, 2, 7, 0]
]

# Function to calculate Euclidean distance
def euclidean_distance(pt1, pt2):
    return math.sqrt((pt1[0] - pt2[0]) ** 2 + (pt1[1] - pt2[1]) ** 2)

# Check requirements
def validate_solution(tours, cities):
    total_visited = set()
    max_travel_cost = 0
    visited_cities = [0]  # Include depot initially as visited
    
    for tour in tours:
        tour_cost = 0
        last_city = 0
        for city in tour[1:]:
            if city != 0:  # ignore the depot city in the middle of the tour
                tour_cost += euclidean_distance(cities[last_city], cities[city])
                total_visited.add(city)
                last_city = city
        tour_cost += euclidean_distance(cities[last_city], cities[0])  # Return to depot
        max_travel_cost = max(max_travel_cost, tour_cost)
        visited_cities.extend(tour[1:])

    # Requirements check
    all_cities_visited_once = len(total_visited) == 15 and all(1 <= city < 16 for city in total_visited)
    all_tours_start_end_at_depot = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)
    
    return all_cities_visited_once and all_tours_start_end_at_depot and max_travel_cost == 72.81785234728197

# Perform the test
if validate_solution(tours, cities):
    print("CORRECT")
else:
    print("FAIL")