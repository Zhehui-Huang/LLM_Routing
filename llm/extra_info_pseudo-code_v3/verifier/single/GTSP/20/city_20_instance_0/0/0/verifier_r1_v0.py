import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def validate_tour(tour, cities, city_groups):
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour must start and end at the depot city 0."
        
    visited_groups = set()
    for city_index in tour[1:-1]:  # exclude the start and end depot city
        for group_id, group in enumerate(city_groups):
            if city_index in group:
                visited_groups.add(group_id)
                break
    
    if len(visited_groups) != len(city_groups):
        return "FAIL", "Tour must visit exactly one city from each city group."
    
    # Calculate the total travel cost of the tour
    total_distance = 0
    for i in range(len(tour) - 1):
        total_distance += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if abs(total_distance - 110.09) > 0.01:  # considering float precision issues
        return "FAIL", f"Tour total travel cost mismatch: calculated {total_distance}, expected 110.09."
    
    return "CORRECT", None

def test_validate_tour():
    cities = {
        0: (8, 11),
        1: (40, 6),
        2: (95, 33),
        3: (80, 60),
        4: (25, 18),
        5: (67, 23),
        6: (97, 32),
        7: (25, 71),
        8: (61, 16),
        9: (27, 91),
        10: (91, 46),
        11: (40, 87),
        12: (20, 97),
        13: (61, 25),
        14: (5, 59),
        15: (62, 88),
        16: (13, 43),
        17: (61, 28),
        18: (60, 63),
        19: (93, 15)
    }
    city_groups = [
        [1, 3, 5, 11, 13, 14, 19],  # Group 0
        [2, 6, 7, 8, 12, 15],  # Group 1
        [4, 9, 10, 16, 17, 18]  # Group 2
    ]
    tour = [0, 1, 8, 4, 0]
    
    result, error = validate_tour(tour, cities, city_groups)
    if result == "CORRECT":
        print("CORRECT")
    else:
        print("FAIL")
        print(error)

test_validate_tour()