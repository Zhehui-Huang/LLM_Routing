import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_solution(tours, coordinates):
    visited_cities = set()
    total_verified_cost = 0.0
    all_tours_ending_depot = True
    must_perform_as_expected = True

    for tour_info in tours:
        tour = tour_info['tour']
        claimed_travel_cost = tour_info['cost']
        
        # Check if each tour starts and ends at the depot (city 0)
        if tour[0] != 0 or tour[-1] != 0:
            all_tours_ending_depot = False
            
        real_cost = 0
        for i in range(len(tour) - 1):
            city_index_from = tour[i]
            city_index_to = tour[i + 1]
            real_cost += calculate_distance(coordinates[city_index_from], coordinates[city_index_to])
            visited_cities.add(city_index_from)
        
        total_verified_cost += real_cost
        if abs(real_cost - claimed_travel_cost) > 1e-2:  # Checking for minor floating-point inaccuracies
            must_perform_as_expected = False
    
    # All cities except depot must be visited exactly once
    cities_all_visited_once = len(visited_cities) == len(coordinates) - 1 and all(city_idx != 0 for city_idx in visited_cities)
    
    # Check if the depot is not considered as a city to visit
    correct_depot_handling = 0 not in visited_cities

    return (cities_all_visited_once and
            correct_depot_handling and
            all_tours_ending_depot and
            must_perform_as_expected)

def test_solution():
    coordinates = {
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
        {"tour": [0, 15, 17, 13, 1, 14, 2, 9, 3, 4, 0], "cost": 268.74},
        {"tour": [0, 6, 16, 18, 8, 11, 7, 12, 5, 10, 0], "cost": 278.39}
    ]

    correct_solution = validate_solution(tours, coordinates)
    
    overall_claimed_total_cost = 547.13
    computed_cost = sum(tour['cost'] for tour in tours)
    
    if correct_solution and abs(computed_cost - overall_claimed_total_cost) < 1e-2:
        return "CORRECT"
    else:
        return "FAIL"

print(test_solution())