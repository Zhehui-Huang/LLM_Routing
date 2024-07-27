import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour_and_cost(tour, total_cost):
    cities_coordinates = {
        0: (53, 68),
        1: (75, 11),
        2: (91, 95),
        3: (22, 80),
        4: (18, 63),
        5: (54, 91),
        6: (70, 14),
        7: (97, 44),
        8: (17, 69),
        9: (95, 89)
    }
    
    city_groups = {
        0: [5, 6, 7],
        1: [2, 3],
        2: [1, 9],
        3: [4, 8]
    }
    
    # Test if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Test if the tour visits exactly one city from each city group
    visited_groups = set()
    for city_index in tour[1:-1]:  # exclude the first and last entries
        found = False
        for group, cities in city_groups.items():
            if city_index in cities:
                if group in visited_groups:
                    return "FAIL"
                visited_groups.add(group)
                found = True
                break
        if not found:
            return "FAIL"
    
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Test if the total travel cost is calculated correctly
    calculated_cost = 0
    for i in range(len(tour) - 1):
        city1 = cities_coordinates[tour[i]]
        city2 = cities_coordinates[tour[i + 1]]
        calculated_cost += euclidean_distance(city1, city2)
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    # All checks passed
    return "CORRECT"

# Tour provided in the task solution
tour_provided = [0, 5, 2, 9, 8, 0]
total_cost_provided = 183.98559431675523

# Run the verification
result = verify_tour_and_cost(tour_provided, total_cost_provided)
print(result)