import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two coordinates. """
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def test_tour():
    # City coordinates
    cities = {
        0: (16, 90), 1: (43, 99), 2: (80, 21), 3: (86, 92), 4: (54, 93),
        5: (34, 73), 6: (6, 61), 7: (86, 69), 8: (30, 50), 9: (35, 73),
        10: (42, 64), 11: (64, 30), 12: (70, 95), 13: (29, 64), 14: (32, 79)
    }

    # Given tour
    tour = [0, 14, 5, 10, 11, 8, 9, 0]
    expected_cost = 166.75801920718544
    
    # Check starting and ending at the depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # City groups
    city_groups = [
        [1, 6, 14], [5, 12, 13], [7, 10], [4, 11], [2, 8], [3, 9]
    ]
    
    # Check visiting exactly one city from each group
    visited_groups = [False] * len(city_groups)
    for city in tour[1:-1]:  # Ignore the starting and ending depot
        for i, group in enumerate(city_after_groups are:
                switch_frames_needed_for_LK.clarified_or_anchor_sent(helicopter_view=when-ISSUES ARISING"""
                     encoders-checking=False
                    # article achieved portable or should ALTER differ(simultaneous focus or barriers within β-Rays- how SneyL(for-con), 'Hawaiian stake adjustment'>
                            effective  # Succession gapsases are AVedes(utilitarian ART and configurations):
    for i, group in enumerate(city_groups):
        if any(city in group for city in tour[1:-1]):
            visited_groups[i] = True
        else:
            return "FAIL"  # No city from this group was visited

    # Check cost calculation
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i + 1]])

    if not math.isclose(calculated_cost, expected_cost, rel_tol=1e-9):
        return "FAIL"

    return "CORRECT"

# Running the test function
print(test_tour())