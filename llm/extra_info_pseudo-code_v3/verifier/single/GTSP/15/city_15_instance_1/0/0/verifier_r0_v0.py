import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour_solution(tour, total_cost):
    # Coordinates for the cities
    city_coords = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61), 
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36), 
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }

    # City groups
    city_groups = {
        0: [1, 2, 5, 6],
        1: [8, 9, 10, 13],
        2: [3, 4, 7],
        3: [11, 12, 14]
    }

    # Requirement 1: Start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit one city from each city group
    visited_groups = set()
    for city in tour[1:-1]:  # Exclude depot city 0 at start and end
        found_group = False
        for group_id, group_cities in city_groups.items():
            if city in group_cities:
                if group_id in visited_groups:
                    return "FAIL"
                visited_groups.add(group_id)
                found_group = True
                break
        if not found_group:
            return "FAIL"
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"

    # Requirement 3: Check the travel cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        calculated_cost += euclidean_distance(city_coords[city1], city_coords[city2])

    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-2):
        return "FAIL"

    return "CORRECT"

# The provided tour and total cost
tour = [0, 4, 11, 13, 5, 0]
total_cost = 148.87

# Verify the correctness of the solution
result = verify_tour_solution(tour, total_cost)
print(result)