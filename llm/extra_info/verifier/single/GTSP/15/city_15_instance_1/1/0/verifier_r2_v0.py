import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, cost):
    cities_coordinates = {
        0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
        5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
        10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
    }
    city_groups = [
        [1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]
    ]
    
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Exactly one city from each group
    unique_cities = tour[1:-1]  # Exclude the depot city
    from_each_group = []
    for group in city_groups:
        cities_in_group = sum([city in group for city in unique_cities])
        if cities_in_group != 1:
            return "FAIL"
        from_each_group.append(cities_in_group == 1)
    if not all(from_each_needs_group):
        return "FAIL"
    
    # [Requirement 3] Verify total travel cost (by recalculating it)
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities_coordinates[tour[i]], cities_coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, cost, rel_tol=1e-9):
        return "FAIL"
    
    # [Requirement 4] Output the tour list starting and ending at city 0
    # [Requirement 5] Output the total cost
    # Handled inherently by the input
    
    return "CORRECT"

# Sample submission
tour = [0, 4, 11, 13, 5, 0]
cost = 148.86963273650017
result = verify_solution(tour, cost)
print(result)