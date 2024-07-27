import math

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def check_tours_and_compute_cost(city_coordinates, tours):
    # This will store the unique cities visited excluding the depot (city 0)
    cities_visited = set()
    
    global_cost = 0
    results = []

    for tour in tours:
        tour_cost = 0
        current_city = tour[0]  # Should be the depot = 0
        
        for next_city in tour[1:]:
            tour_cost += compute_euclidean_distance(
                city_coordinates[current_city][0], city_coordinates[current_city][1],
                city_coordinates[next_city][0], city_coordinates[next_city][1]
            )
            current_city = next_city
            if next_city != 0:  # Exclude the depot from being added to visited cities
                cities_visited.add(next_city)
        
        results.append((tour, tour_cost))
        global_cost += tour_cost

    # Check if all cities except the depot were visited exactly once
    all_cities_visited_once = len(cities_visited) == len(city_coordinates) - 1
    return all_cities_visited_once, results, global_cost

def test_solution():
    city_coordinates = {
        0: (30, 40),
        1: (37, 52),
        2: (49, 43),
        3: (52, 64),
        4: (31, 62),
        5: (52, 33),
        6: (42, 41),
        7: (52, 41),
        8: (57, 58),
        9: (62, 42),
        10: (42, 57),
        11: (27, 68),
        12: (43, 67),
        13: (58, 27),
        14: (37, 69),
        15: (61, 33),
        16: (62, 63),
        17: (63, 69),
        18: (45, 35)
    }
    
    tours = [
        [0, 6, 2, 7, 5, 9, 8, 3, 4, 1, 0],
        [0, 10, 11, 14, 12, 17, 16, 15, 13, 18, 0]
    ]
    
    correct_all_visited_once, details, total_cost = check_tours_and_compute_cost(city_coordinates, tours)

    if not correct_all_visited_once:
        return "FAIL"

    expected_costs = [115.60355496962676, 149.767263793843]
    expected_total_cost = 265.37081876346974

    tolerance = 1e-4  # small tolerance for floating point approximation issues
    for detail, expected in zip(details, expected_costs):
        if not (expected - tolerance <= detail[1] <= expected + tolerance):
            return "FAIL"

    if not (expected_total_cost - tolerance <= total_cost <= expected_total_cost + tolerance):
        return "FAIL"
    
    return "CORRECT"

# Execute the test
print(test_solution())