import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tsp_solution(tour, city_coords, max_distance_cond):
    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city is visited exactly once
    unique_cities_visited = set(tour)
    if len(unique_cities_visited) != len(city_coords) or len(tour) != len(city_coords) + 1:
        return "FAIL"
    
    # Check for duplicates excluding starting and ending city 0
    city_visit_counts = {city: tour.count(city) for city in tour if city != 0}
    if any(count != 1 for count in city_visit_counts.values()):
        return "FAIL"
    
    # Requirement 3: Check max distance between consecutive cities
    actual_max_distance = max(
        calculate_distance(city_coords[tour[i]], city_coords[tour[i + 1]]) for i in range(len(tour) - 1)
    )
    if actual_max_distance > max_distance_cond:
        return "FAIL"
    
    return "CORRECT"

# City coordinates as provided
city_coords = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58), 6: (12, 84),
    7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25), 11: (52, 0), 12: (60, 95), 13: (10, 94),
    14: (96, 73), 15: (14, 47), 16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# Solution provided
provided_tour = [0, 3, 19, 6, 13, 2, 5, 15, 17, 16, 9, 11, 10, 1, 4, 7, 18, 12, 8, 14, 0]
provided_max_distance = 68.15423684555495

# Testing the solution
result = verify_tsp_solution(provided_tour, city_coords, provided_max_distance)
print(result)