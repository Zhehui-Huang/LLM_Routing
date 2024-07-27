import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, city_positions, city_groups):
    # Requirement 1: Start and end at the depot city (City 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Visit exactly one city from each city group
    visited_groups = set()
    for city in tour[1:-1]:  # exclude the starting and ending depot city
        for i, group in enumerate(city_croups):
            if city in group:
                visited_groups.add(i)
                break
    if len(visited_groups) != len(city_groups):
        return "FAIL"
    
    # Requirement 5: Tour starts and ends at the city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 3 & 6: Calculate the Euclidean tour cost
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_distance(city_positions[tour[i]], city_positions[tour[i + 1]])
    
    # Close to given cost with some tolerance for floating point precision issues
    given_cost = 148.87
    if not math.isclose(total_cost, given_cost, rel_tol=1e-05):
        return "FAIL"
    
    return "CORRECT"

# City positions indexed by city number
city_positions = [
    (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
    (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
    (4, 60),  (78, 82), (83, 96), (60, 50), (98, 1)
]

# City groups
city_groups = [
    [1, 2, 5, 6],
    [8, 9, 10, 13],
    [3, 4, 7],
    [11, 12, 14]
]

# Verify given tour and cost
provided_tour = [0, 4, 11, 13, 5, 0]
result = verify_tour(provided_tour, city_positions, city_groups)
print(result)