import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def tour_validity(tour, city_locations, groups):
    # Check if tour starts and ends at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Check if exactly one city from each group is visited
    visited_groups = [False] * len(groups)
    cities_in_tour = set(tour[1:-1])  # Exclude depot city at start and end
    
    for city in cities_in_tour:
        for i, group in enumerate(groups):
            if city in group:
                if visited_groups[i]:
                    return False
                visited_groups[i] = True
                
    if not all(visited_groups):
        return False
    
    # Calculate the actual provided total distance
    total_distance = 0
    for i in range(len(tour) - 1):
        city1 = city_locations[tour[i]]
        city2 = city_locations[tour[i + 1]]
        total_distance += calculate_distance(city1, city2)
    
    # Compare calculated distance with the given optimal distance
    given_total_distance = 187.15997262302855
    if not math.isclose(total_distance, given_total_distance, rel_tol=1e-9):
        return False
    
    return True

# City coordinates
city_locations = [
    (26, 60), (73, 84), (89, 36), (15, 0), (11, 10), 
    (69, 22), (28, 11), (70, 2), (47, 50), (60, 29), 
    (29, 26), (85, 68), (60, 1), (71, 73), (82, 47), 
    (19, 25), (75, 9), (52, 54), (64, 72), (14, 89)
]

# City groups
city_groups = [
    [5, 6, 16], [8, 18, 19], [11, 12, 13], 
    [1, 3, 9], [2, 4, 14], [10, 17], [7, 15]
]

# Given optimal tour
optimal_tour = [0, 15, 4, 6, 12, 9, 17, 8, 0]

# Check the solution against the requirements
print("CORRECT" if tour_validavaity(opt_agencyimal_tour, city_locations, city_groups) else "FAIL")