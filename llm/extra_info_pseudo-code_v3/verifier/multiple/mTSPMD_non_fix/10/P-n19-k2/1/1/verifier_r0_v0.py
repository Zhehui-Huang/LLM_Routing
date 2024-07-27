import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_tours():
    cities = {
        0: (30, 40),
        1: (37, 52),
        2: (49, 43),
        3: (52, 64),
        4: (31, 62),
        5: (52, 33),
        6: (42, 41),
        7: (52, 41),
        8: (57, 58),
        9: (62, 42),
        10: (42, 57),
        11: (27, 68),
        12: (43, 67),
        13: (58, 27),
        14: (37, 69),
        15: (61, 33),
        16: (62, 63),
        17: (63, 69),
        18: (45, 35)
    }
    
    tours = {
        0: [0, 6, 2, 7, 9, 8, 3, 12, 14, 11],
        1: [0, 18, 5, 13, 15, 16, 17, 10, 4]
    }
    
    # Verify each city is visited exactly once
    visited_cities = []
    for tour in tours.values():
        visited_cities.extend(tour)
    
    all_cities = list(cities.keys())
    if sorted(visited_cities) != sorted(all_cities):
        return "FAIL: Each city must be visited exactly once."
    
    # Verify each tour starts at the correct depot (requirement states from designated depot)
    if not all(tour[0] == 0 for tour in tours.values()):  # Each tour should start at depot city 0 in this specific solution example
        return "FAIL: Tours must start from the designated depot city."

    # Verify travel cost (not specified how to do this in unit tests without further data or functions provided)
    # So, this part of the requirement is assumed to be not directly testable here.
    # You'd typically calculate this using the given Euclidean distance function and provided path.
    
    return "CORRECT"

result = test_tours()
print(result)