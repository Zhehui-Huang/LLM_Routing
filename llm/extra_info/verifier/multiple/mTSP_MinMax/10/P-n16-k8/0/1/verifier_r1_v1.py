import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, city_coordinates):
    num_cities = len(city_coordinates)
    visited_cities = set()
    all_travel_costs = []

    # Iterate through tours correcting accessing 'path' and 'cost'
    for tour_dict in tours:
        tour_path = tour_dict['path']
        reported_cost = tour_dict['cost']
        # Check if tour starts and ends at the depot
        if tour_path[0] != 0 or tour_path[-1] != 0:
            return "FAIL"
        
        robot_travel_cost = 0
        for i in range(len(tour_path) - 1):
            city1 = tour_path[i]
            city2 = tour_path[i + 1]
            if city1 < 0 or city1 >= num_cities or city2 < 0 or city2 >= num_cities:
                return "FAIL"
            distance = calculate_size(city_coordinates[city1], city_coordinates[city2])
            robot_travel_cost += distance
            if city1 != 0:
                visited_cities.add(city1)

        # Check if calculated distance matches reported distance approximately
        if not math.isclose(robot_travel_cost, reported_cost, abs_tol=0.1):
            return "FAIL"
        
        all_travel_costs.append(robot_travel_cost)

    # Validate if all cities are visited exactly once
    if len(visited_cities) != num_cities - 1:
        return "FAIL"

    # Validate if the reported max cost is correct
    max_reported_cost = max(all_travel_costs)
    if not math.isclose(max_reported_cost, max(tour['cost'] for tour in tours), abs_tol=0.1):
        return "FAIL"

    return "CORRECT"

# Given solution reformatted and assuming it's passed as argument to the function
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62),
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69)
]
tours = [
    {'path': [0, 13, 9, 0], 'cost': 68.39},
    {'path': [0, 15, 12, 0], 'cost': 66.12},
    {'path': [0, 6, 0], 'cost': 24.08},
    {'path': [0, 4, 11, 0], 'cost': 57.39},
    {'path': [0, 5, 14, 0], 'cost': 62.44},
    {'path': [0, 8, 3, 0], 'cost': 72.82},
    {'path': [0, 1, 10, 0], 'cost': 41.77},
    {'path': [0, 2, 7, 0], 'cost': 51.59}
]

print(verify_solution(tours, city_coordinates))