import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0]) ** 2 + (c1[1] - c2[1]) ** 2)

def calculate_cost(tour, coordinates):
    cost = 0
    for i in range(len(tour) - 1):
        cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return round(cost, 2)

def test_solution():
    # Coordinates of cities including depots
    coordinates = [
        (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
        (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
        (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
        (164, 193), (129, 189), (155, 185), (139, 182)
    ]
    
    # Tours and their expected costs
    tours = [
        [0, 13, 11, 6, 5, 15, 0],
        [0, 17, 21, 19, 1, 10, 0],
        [0, 18, 9, 7, 2, 3, 0],
        [0, 4, 8, 12, 20, 16, 14, 0]
    ]
    expected_costs = [132.78, 175.46, 169.13, 155.61]
    
    # Validate the total count of cities visited once
    city_visit_tracker = [0] * 22
    
    actual_individual_costs = []
    for tour in tours:
        for city in tour:
            city_visit_tracker[city] += 1
        tour_cost = calculate_cost(tour, coordinates)
        actual_individual_costs.append(tour_cost)
    
    if any(city != 1 for city in city_visit_tracker):
        return "FAIL"
    
    if any(expected != actual for expected, actual in zip(expected_costs, actual_individual_costs)):
        return "FAIL"
    
    if round(sum(expected_costs), 2) != round(sum(actual_individual_costs), 2):
        return "FAIL"
    
    return "CORRECT"

# Execute the test function and print the result
print(test_solution())