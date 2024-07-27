import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(cities, tour, total_cost, max_distance):
    # Verify start and end at depot, and tour length
    if tour[0] != 0 or tour[-1] != 0 or len(tour) != len(set(cities.keys())) + 1:
        return "FAIL"

    # Verify each city is visited exactly once except depot
    city_visit_count = {key: 0 for key in cities.keys()}
    for city_index in tour:
        if city_index in city_visit_count:
            city_visit_markers[city_index] += 1

    if any(count != 1 for key, count in city_visit_markers.items() if key != 0):
        return "FAIL"
    
    # Calculate cost and maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        from_city = tour[i]
        to_city = tour[i + 1]
        distance = euclidean_distance(*cities[from_city], *cities[to_city])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check calculated total cost and maximum distance
    if not math.isclose(calculated_total_cost, total_cost, abs_tol=1e-2):
        return "FAIL"
    if not math.isclose(calculated_max_distance, max_distance, abs_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# Define city coordinates
cities_coordinates = {
    0: (84, 67),
    1: (74, 40),
    2: (71, 13),
    3: (74, 82),
    4: (97, 28),
    5: (0, 31),
    6: (8, 62),
    7: (74, 56),
    8: (85, 71),
    9: (6, 76)
}

# Provided solution details
tour_solution = [0, 1, 2, 4, 3, 9, 5, 6, 7, 8, 0]
total_travel_cost_solution = 379.34
max_distance_solution = 68.26

# Verify the solution
result = verify_tour(cities_coordinates, tour_solution, total_travel_cost_solution, max_distance_solution)
print(result)