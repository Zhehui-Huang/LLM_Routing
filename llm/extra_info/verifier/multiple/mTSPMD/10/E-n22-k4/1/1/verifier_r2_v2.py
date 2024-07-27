import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tours():
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254),
        (128, 252), (163, 247), (146, 246), (161, 242),
        (142, 239), (163, 236), (148, 232), (128, 231),
        (156, 217), (129, 214), (146, 208), (164, 208),
        (141, 206), (147, 193), (164, 193), (129, 189),
        (155, 185), (139, 182)
    ]
    tours = [
        ([0, 8, 6, 7, 5, 9, 4, 0], 143.3606794493811),
        ([1, 10, 12, 14, 13, 11, 1], 137.87545487253396),
        ([2, 15, 18, 17, 16, 2], 157.42369286502216),
        ([3, 19, 21, 20, 3], 166.8824405920485)
    ]

    visited_cities = set()
    total_cost_calculated = 0

    for tour, reported_cost in tours:
        tour_cost = 0.0
        last_city_index = tour[0]
        visited_cities.add(last_city_index)

        for city_index in tour[1:]:
            visited_cities.add(city_index)
            tour_cost += calculate_distance(coordinates[last_city_index], coordinates[city_index])
            last_city_index = city_index

        total_cost_calculated += tour_cost

        if not math.isclose(tour_cost, reported_cost, abs_tol=1e-4):
            return "FAIL"

    overall_reported_cost = 605.5422677789858

    if len(visited_cities) != len(coordinates):
        return "FAIL"

    if not math.isclose(total_cost_calculated, overall_reported_cost, abs_tol=1e-4):
        return "FAIL"

    return "CORRECT"

# Call the function to verify the tours
print(verify_tours())