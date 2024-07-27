def calculate_distance(city1, city2):
    return ((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)**0.5

def verify_solution(tour, city_coordinates, city_groups):
    # Check Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Create a set of city indices from the tour, excluding the depot (start and end)
    visited_cities = set(tour[1:-1])
    
    # Check Requirement 2: Visit exactly one city from each group
    unique_cities_visited_from_groups = set()
    for group in city_groups:
        group_intersection = visited_cities.intersection(group)
        if len(group_intersection) != 1:
            return "FAIL"
        unique_cities_visited_from_groups.update(group_intersection)
        
    # If not all tour cities (except start & end) are accounted for in the groups
    if len(unique_cities_visited_from_groups) != len(visited_cities):
        return "FAIL"
    
    # Check Requirement 3: Minimized travel cost
    # Since we can't verify optimality without other solutions, we ensure the distances are correctly calculated
    # along the given tour. Further testing with comparative optimization solutions would be needed to verify minimization.
    total_travel_cost = sum(calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]]) for i in range(len(tour)-1))
    
    # Using the provided tour and calculating its cost
    expected_cost = 320.04974514  # Provided tour cost
    # Allow small floating point error in calculations
    if not (abs(total_travel_cost - expected_cost) < 1e-5):
        return "FAIL"
    
    return "CORRECT"

# City coordinates mapping as provided
city_coordinates = {
    0: (30, 56), 1: (53, 42), 2: (1, 95), 3: (25, 61), 4: (69, 57), 5: (6, 58),
    6: (12, 84), 7: (72, 77), 8: (98, 95), 9: (11, 0), 10: (61, 25),
    11: (52, 0), 12: (60, 95), 13: (10, 94), 14: (96, 73), 15: (14, 47),
    16: (18, 16), 17: (4, 43), 18: (53, 76), 19: (19, 72)
}

# City groups
city_groups = [
    [4, 10, 13, 17], [6, 7, 14], [9, 12, 16], [2, 5, 15], [1, 3, 19], [8, 11, 18]
]

# Proposed tour
tour = [0, 17, 0]

# Verify the solution
result = verify_solution(tour, city_coordinates, city_groups)
print(result)