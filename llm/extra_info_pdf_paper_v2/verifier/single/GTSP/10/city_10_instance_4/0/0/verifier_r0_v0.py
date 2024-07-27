import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, groups, city_coordinates):
    # Requirement 1: Check if the tour starts and ends at city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Check if exactly one city from each group is visited
    unique_cities = set(tour[1:-1])  # Excluding the start and end depot city
    group_cities = set(sum(groups, []))
    for city in unique_cities:
        if city not in group_cities:
            return "FAIL"
    for group in groups:
        if not any(city in group for city in unique_cities):
            return "FAIL"
    
    # Requirement 3: Calculate total travel cost using Euclidean distance
    total_distance_calculated = 0
    for i in range(len(tour) - 1):
        city1 = city_coordinates[tour[i]]
        city2 = city_coordinates[tour[i + 1]]
        total_distance_calculated += calculate_distance(city1, city2)
    
    # Check if the computed distance matches the reported distance
    reported_distance = 371.19
    if not math.isclose(total_distance_calculated, reported_distance, abs_tol=0.01):
        return "FAIL"
    
    return "CORRECT"

# City coordinates
city_coordinates = [
    (79, 15),  # Depot city 0
    (79, 55),  # City 1
    (4, 80),   # City 2
    (65, 26),  # City 3
    (92, 9),   # City 4
    (83, 61),  # City 5
    (22, 21),  # City 6
    (97, 70),  # City 7
    (20, 99),  # City 8
    (66, 62)   # City 9
]

# Grouped cities
groups = [[1, 4], [2, 6], [7], [5], [9], [8], [3]]

# Tour provided
proposed_tour = [0, 4, 6, 7, 5, 9, 8, 3, 0]

# Verify the tour
print(verify_tour(proposed_tour, groups, city_coordinates))