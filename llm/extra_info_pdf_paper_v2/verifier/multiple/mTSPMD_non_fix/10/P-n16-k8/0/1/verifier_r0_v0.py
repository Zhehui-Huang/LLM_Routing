import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def test_solution():
    # City coordinates with indexed positions (index corresponds to city number)
    city_coordinates = {
        0: (30, 40), 1: (37, 52), 2: (49, 49),
        3: (52, 64), 4: (31, 62), 5: (52, 33),
        6: (42, 41), 7: (52, 41), 8: (57, 58),
        9: (62, 42), 10: (42, 57), 11: (27, 68),
        12: (43, 67), 13: (58, 48), 14: (58, 27),
        15: (37, 69)
    }

    # Tours provided in the solution
    robot_tours = {
        0: [0, 6, 12],
        1: [1, 10, 15],
        2: [2, 7],
        3: [3, 8],
        4: [4, 11],
        5: [5, 14],
        6: [6, 13],
        7: [7, 9]
    }

    # Travel costs given in the solution
    given_total_costs = [38.06081824130767, 20.071067811865476, 8.54400374531753,
                         7.810249675906654, 7.211102550927978, 8.48528137423857,
                         17.46424919657298, 10.04987562112089]

    overall_given_total_cost = 117.69664821725775

    # Calculate travel costs based on tours
    calculated_costs = []
    all_visited_cities = set()
    for robot, tour in robot_tours.items():
        tour_cost = 0
        previous_city = tour[0]
        for city in tour[1:]:
            x1, y1 = city_coordinates[previous_city]
            x2, y2 = city_coordinates[city]
            tour_cost += euclidean_distance(x1, y1, x2, y2)
            previous_city = city
        all_visited_cities.update(tour)
        calculated_costs.append(round(tour_cost, 9))
    
    # Compare calculated costs to given costs
    costs_match = all(math.isclose(given, calc, rel_tol=1e-8) for given, calc in zip(given_total_costs, calculated_costs))

    # Check if all cities are visited exactly once
    all_cities_visited_once = len(all_visited_cities) == 16 and all(v in all_visited_cities for v in range(16))

    # Compare overall travel costs
    overall_calculated_cost = sum(calculated_costs)
    overall_cost_match = math.isclose(overall_calculated_cost, overall_given_total_cost, rel_tol=1e-8)

    # Return the result based on the checks
    if costs_match and all_cities_visited_once and overall_cost_match:
        return "CORRECT"
    else:
        return "FAIL"

# Run the test and print the result
print(test_solution())