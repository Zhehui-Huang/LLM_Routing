import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(robots_tours, city_coords, expected_total_cost):
    visited_cities = set()
    total_calculated_cost = 0
    initial_depot = 0

    try:
        for tour in robots_tours:
            # Requirement 1 - Check correct city order and unique city visits
            tour_cities = tour['tour']
            assert tour_cities[0] == tour_cities[-1], "Tour must start and end at the same city (depot)"

            # Requirement 2 - Tour starts at a designated depot city
            assert tour_cities[0] in range(7), "Starting city should be a depot"

            # Requirement 3 - Handled implicitly as tours need not return to the depot city 0
            # Requirement 7 - Starting from depot city 0
            if tour['robot_id'] == 0:
                assert tour_cities[0] == initial_depot, "Robot 0 should start from depot 0"

            for city in tour_cities:
                if city not in visited_cities:
                    visited_cities.add(city)
                else:
                    assert False, "Each city should be visited exactly once"

            # Requirement 5 - Calculate travel cost correctly
            tour_cost = 0
            for i in range(len(tour_cities) - 1):
                tour_cost += euclidean_distance(city_coords[tour_cities[i]], city_coords[tour_cities[i + 1]])
            total_calculated_cost += tour_cost
            assert math.isclose(tour_cost, tour['total_travel_cost'], abs_tol=1e-5), "Calculated tour cost does not match provided tour cost"

        # Requirement 4 & Requirement 6 - Total cost and city count check
        assert len(visited_cities) == 23, "All 23 cities (depots included) must be visited"
        assert math.isclose(total_calculated_cost, expected_total_cost, abs_tol=1e-5), "Total travel cost does not match expected"

    except AssertionError as error:
        print(f"FAIL: {error}")
        return

    print("CORRECT")

# Provided solution data
robots_tours = [
    {'robot_id': 0, 'tour': [0, 21, 10, 0], 'total_travel_cost': 22.82732825947379},
    {'robot_id': 1, 'tour': [1, 16, 12, 1], 'total_travel_cost': 27.66979567522112},
    {'robot_id': 2, 'tour': [2, 13, 17, 2], 'total_travel_cost': 24.352443678915773},
    {'robot_id': 3, 'tour': [3, 8, 18, 3], 'total_travel_cost': 14.88131748777213},
    {'robot_id': 4, 'tour': [4, 11, 15, 4], 'total_travel_cost': 17.26097817204887},
    {'robot_id': 5, 'tour': [5, 22, 14, 5], 'total_travel_cost': 15.854893276677949},
    {'robot_id': 6, 'tour': [6, 20, 19, 6], 'total_travel_cost': 45.17897205584205},
    {'robot_id': 7, 'tour': [7, 9], 'total_travel_cost': 10.04987562112089}
]

# Overall cost they provided
overall_cost_provided = 178.07560422707257

# Cities coordinates
city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
    (37, 69), (38, 46), (61, 33), (62, 63), (63, 69),
    (45, 35), (32, 39), (56, 37)
]

verify_solution(robots_tours, city_coords, overall_cost_provided)