import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def calculate_total_cost(tour, city_locations):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_locations[tour[i]], city_locations[tour[i+1]])
    return total_cost

def verify_solution(tour, reported_cost, city_locations, city_groups):
    # Requirement 1: Start and end at the depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit exactly one city from each group
    cities_from_groups = set()
    for city in tour[1:-1]:  # Exclude the depot city at start and end
        found = False
        for index, group in enumerate(city_groups):
            if city in group:
                if index in cities_from_groups:
                    return "FAIL"  # City from same group is used twice
                cities_from_groups.add(index)
                found = True
        if not found:
            return "FAIL"  # City not found in any group
    
    if len(cities_from_groups) != len(city_groups):
        return "FAIL"  # Not all groups are represented

    # Requirement 3: Correct calculation of the total travel cost
    calculated_cost = calculate_total_cost(tour, city_locations)
    if not math.isclose(reported_cost, calculated_cost, abs_tol=0.1):  # Using a small tolerance
        return "FAIL"

    return "CORRECT"

# Test parameters
city_locations = [
    (16, 90),  # Depot city 0
    (43, 99),  # City 1
    (80, 21),  # City 2
    (86, 92),  # City 3
    (54, 93),  # City 4
    (34, 73),  # City 5
    (6, 61),   # City 6
    (86, 69),  # City 7
    (30, 50),  # City 8
    (35, 73),  # City 9
    (42, 64),  # City 10
    (64, 30),  # City 11
    (70, 95),  # City 12
    (29, 64),  # City 13
    (32, 79)   # City 14
]

city_groups = [
    [1, 6, 14],
    [5, 12, 13],
    [7, 10],
    [4, 11],
    [2, 8],
    [3, 9]
]

tour = [0, 14, 5, 10, 11, 8, 9, 0]
total_cost = 166.75801920718544

# Invoke the verification
result = verify_solution(tour, total_cost, city_locations, city_groups)
print(result)