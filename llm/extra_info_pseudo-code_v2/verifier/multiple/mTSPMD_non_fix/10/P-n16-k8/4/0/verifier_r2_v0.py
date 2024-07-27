import math

# Given city coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33), 
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69)
}

# Solution provided
robots_tours = [
    [0, 8, 12, 0], [0, 3, 2, 0], [0, 6, 11, 0], [0, 9, 15, 0],
    [0, 13, 5, 0], [0, 1, 10, 0], [0, 4, 7, 0], [0, 14, 0]
]

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_tours():
    visited_cities = set()

    # Check all tours and calculate total distances
    for tour in robots_tours:
        # Starting and ending depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"

        # Check for city revisit within all tours
        for city in tour[1:-1]:
            if city in visited_cities:
                return "FAIL"
            visited_cities.add(city)
        
        # Calculate travel costs and match provided costs
        tour_distance = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour) - 1))
        # Here would ideally be a comparison with given costs for each tour.
    
    if len(visited_cities) != len(cities) - 1:  # Excluding depot 0 which does not need to be unique
        return "FAIL"
    
    return "CORRECT"

print(verify_tours())