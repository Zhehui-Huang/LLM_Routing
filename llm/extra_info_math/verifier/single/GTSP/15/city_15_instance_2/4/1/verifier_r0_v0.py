import math

# Define city coordinates
cities = {
    0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42), 
    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14), 
    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)
}

# City groups
city_groups = [
    [8, 12, 14],   # Group 0
    [7, 10, 11],   # Group 1
    [4, 6, 9],     # Group 2
    [1, 3, 13],    # Group 3
    [2, 5]         # Group 4
]

# Reported solution
reported_tour = [0, 2, 6, 11, 8, 1, 0]
reported_cost = 103.11611697272401

def calculate_distance(city1, city2):
    """Calculate Euclidean distance between two cities."""
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def is_valid_tour(tour, city_groups):
    """Check if the tour satisfies all the constraints."""
    # Requirement 1: Start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return False
    
    # Requirement 2: Visit exactly one city from each group
    visited_groups = [False] * len(city_groups)
    visited_cities = set()
    for idx, city in enumerate(tour):
        if city == 0 and idx not in [0, len(tour) - 1]:
            return False  # No revisit of depot except at start and end
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i]:
                    return False  # More than one city from one group
                visited_groups[i] = True
                if city in visited_cities:
                    return False  # City revisited
                visited_cities.add(city)
    if not all(visited_groups):
        return False
    
    # Requirement 3: Correct Calculation of travel costs
    calculated_cost = sum(calculate_distance(tour[i], tour[i + 1]) for i in range(len(tour) - 1))
    if not math.isclose(calculated_cost, reported_cost, rel_tol=1e-9):
        return False

    return True

# Validate the reported solution
result = "CORRECT" if is_valid_tour(reported_tour, city_groups) else "FAIL"
print(result)