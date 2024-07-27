def calculate_distance(city1, city2):
    import math
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tours, city_coordinates):
    all_cities_visited = set()
    total_cost_calculated = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour)-1):
            city_from = tour[i]
            city_to = tour[i+1]
            tour_cost += calculate_distance(city_coordinates[city_from], city_coordinates[city_to])
            if city_from != 0:  # Ensuring not to count the depot city in the set of visited cities
                all_cities_visited.add(city_from)
        total_cost_calculated += tour_cost
        # Check if each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

    # Check if all cities are visited exactly once and the calculated total cost is as reported
    if len(all_cities_visited) != 15 or total_cost_calculated != 342.39:  # 16 cities including depot, visited cities should be 15
        return "FAIL"

    return "CORRECT"

city_coords = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), 
    (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), 
    (58, 27), (37, 69)
]

provided_tours = [
    [0, 4, 0], [0, 14, 5, 0], [0, 10, 0], [0, 11, 0], [0, 6, 0], 
    [0, 2, 0], [0, 7, 0], [0, 1, 0]
]

# Execute the verification function
output = verify_solution(provided_tours, city_coords)
print(output)