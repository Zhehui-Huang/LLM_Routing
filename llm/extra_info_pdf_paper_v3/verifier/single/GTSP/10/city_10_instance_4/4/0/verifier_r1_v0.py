import math

def euclidean_distance(city_a, city_b):
    return math.sqrt((city_a[0] - city_b[0])**2 + (city_a[1] - city_b[1])**2)

def verify_tour(tour, travel_cost):
    # Cities coordinates
    cities = {
        0: (79, 15), 1: (79, 55), 2: (4, 80), 3: (65, 26), 4: (92, 9),
        5: (83, 61), 6: (22, 21), 7: (97, 70), 8: (20, 99), 9: (66, 62)
    }
    
    # City groups
    groups = [
        [1, 4], [2, 6], [7], [5], [9], [8], [3]
    ]
    
    # Check Requirement 1: Visit exactly one city from each of the 7 city groups, start and end at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    visited_groups = [False] * 7
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"  # City from this group already visited
                visited_groups[i] = True
                break
    
    if not all(visited_groups):
        return "FAIL"  # At least one group was not visited
    
    # Check Requirement 2: Calculate exact travel cost as the Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not (abs(calculated_cost - travel_cost) < 1e-5):
        return "FAIL"  # Travel cost does not match
    
    # Check Requirement 3 and 4 implicitly checked by tour format and matching costs
    
    return "CORRECT"  # If all checks pass

# Provided solution
tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]
total_travel_cost = 371.1934423276749

# Check if the solution is correct
result = verify_tour(tour, total_travel_cost)
print(result)