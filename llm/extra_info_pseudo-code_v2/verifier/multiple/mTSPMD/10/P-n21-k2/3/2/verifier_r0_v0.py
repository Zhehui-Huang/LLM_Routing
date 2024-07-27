import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def check_visitation_once(tour, total_cities):
    city_counter = {i: 0 for i in range(total_cities)}
    for city in tour[1:-1]:  # exclude depots at the ends
        city_counter[city] += 1
    return all(count == 1 for count in city_counter.values())

def check_start_end_depot(tour):
    return tour[0] == tour[-1]

def calculate_tour_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return cost

def unit_tests():
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27),
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]

    prediction_robot_0 = {
        "tour": [0, 16, 6, 20, 5, 14, 17, 9, 13, 7, 2, 0],
        "cost": 100.63875529925512
    }
    prediction_robot_1 = {
        "tour": [1, 10, 8, 18, 19, 3, 12, 15, 11, 4, 1],
        "cost": 92.07551076857801
    }
    predicted_total_cost = 192.71426606783317
    
    total_cities = len(coordinates)

    # Tests
    # [Requirement 1]
    # Combining tours excluding depots to check unique visitation
    all_cities_visited_once = check_visitation_once(prediction_robot_0['tour'] + prediction_robot_1['tour'], total_cities)

    # [Requirement 2]
    correct_start_end_depot_0 = check_start_end_depot(prediction_robot_0['tour'])
    correct_start_end_depot_1 = check_start_end_depot(prediction_robot_1['tour'])

    # [Requirement 3]
    calculated_cost_0 = calculate_tour_cost(prediction_robot_0['tour'], coordinates)
    calculated_cost_1 = calculate_tour_cost(prediction_robot_1['tour'], coordinates)
    all_costs_match = math.isclose(calculated_cost_0, prediction_robot_0['cost']) and \
                      math.isclose(calculated_cost_1, prediction_robot_1['cost']) and \
                      math.isclose(calculated_cost_0 + calculated_cost_1, predicted_total_cost)

    if all([all_cities_visited_once, correct_start_end_depot_0, correct_start_end_depot_1, all_costs_match]):
        return "CORRECT"
    else:
        return "FAIL"

# Run tests
test_result = unit_tests()
print(test_result)