def verify_tour(tour, cities, depot=0):
    """ Verify if the tour is correctly formatted and no city is visited more than once except depot """
    visited_cities = set()
    start_depot = tour[0] == depot
    end_depot = tour[-1] == depot
    
    # Check if start and end are depot
    if not (start_depot and end_depot):
        return False
    
    # Check for repeated cities and ensure each is visited exactly once
    for city in tour[1:-1]:  # ignore the first and last entry (depot)
        if city in visited_cities:
            return False
        visited_cities.add(city)
    
    # Ensure all non-depot cities are visited exactly once
    all_cities_covered = visited_cities == set(cities) - {depot}
    return all_cities_covered

def calculate_travel_cost(tour, city_coords):
    """ Calculate the total travel cost based on Euclidean distance """
    total_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coords[tour[i]]
        x2, y2 = city_coords[tour[i + 1]]
        distance = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
        total_cost += distance
    return round(total_cost, 2)

def unit_test_solutions(robots_tours, city_coords):
    city_set = set(city_coords.keys())
    all_visited_cities = []

    for tour in robots_tours:
        # Verify the tours
        if not verify_tour(tour['tour'], city_set):
            return "FAIL"
        
        # Calculate the travel cost and verify it matches the reported cost
        calculated_cost = calculate_travel_cost(tour['tour'], city_coords)
        if calculated_cost != tour['cost']:
            return "FAIL"

        all_visited_cities.extend(tour['tour'][1:-1])  # Collect visited cities, omitting the depot

    # Verify that every city except the depot is visited exactly once in total among all robots
    if set(all_visited_cities) != city_set - {0}:
        return "FAIL"

    return "CORRECT"

# Given output test case
city_coordinates = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 7: (52, 41),
    8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
    15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

robot_tours_info = [
    {'tour': [0, 4, 17, 11, 14, 3, 12, 8, 16, 0], 'cost': 112.78},
    {'tour': [0, 10, 2, 7, 18, 9, 15, 1, 5, 13, 6, 0], 'cost': 106.81}
]

# Run the unit tests
result = unit_test_solutions(robot_tours_info, city_coordinates)
print(result)