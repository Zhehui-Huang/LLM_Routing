import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def validate_tour(tour, city_positions, groups):
    # Requirement 1: Check if tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Requirement 2: Check if exactly one city from each group is in the tour
    visited_groups = set()
    for city in tour[1:-1]:  # Excluding the depot city from check
        for group_index, group in enumerate(groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL"
                visited_groups.add(group_index)
    if len(visited_groups) != len(groups):
        return "FAIL"

    # All requirements passed
    return "CORRECT"

# Test case example
city_positions = {
    0: (29, 51), 1: (49, 20), 2: (79, 69), 3: (17, 20), 4: (18, 61),
    5: (40, 57), 6: (57, 30), 7: (36, 12), 8: (93, 43), 9: (17, 36),
    10: (4, 60), 11: (78, 82), 12: (83, 96), 13: (60, 50), 14: (98, 1)
}
groups = [[1, 2, 5, 6], [8, 9, 10, 13], [3, 4, 7], [11, 12, 14]]

# Hypothetical solution tour for testing
hypothetical_tour = [0, 1, 8, 3, 11, 0]  # Each number correspond to a city index

# Check the validation function
print(validate_tour(hypothetical_tour, city_positions, groups))