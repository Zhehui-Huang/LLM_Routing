import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(city_coords, groups, tour, total_cost):
    try:
        # Preconditions
        assert len(city_coords) == 20  # There are 20 cities with coordinates
        assert all(len(group) > 0 for group in groups) and len(groups) == 3  # Three groups of cities
        assert tour[0] == tour[-1] == 0  # Tour starts and ends at depot (city 0)
        
        # Visiting exactly one city from each group and calculate tour cost
        visited_groups = set()
        calculated_cost = 0
        last_city = tour[0]
        
        for idx in tour[1:]:
            city_group = next((i for i, group in enumerate(groups) if idx in group), -1)
            assert city_group != -1  # City must belong to a group
            visited_groups.add(city_group)
            calculated_cost += euclidean_distance(city_coords[last_city], city_coords[idx])
            last_city = idx
        
        assert len(visited_groups) == 3  # Each group is visited exactly once
        
        # Travel cost calculations
        assert abs(calculated_cost - total_cost) < 1e-4  # Given total cost matches calculated cost
        
        return "CORRECT"
    except AssertionError:
        return "FAIL"

# Define cities and their coordinates
city_coordinates = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), (97, 32),
    (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), (20, 97), (61, 25),
    (5, 59), (62, 88), (13, 43), (61, 28), (60, 63), (93, 15)
]

# Define groups of cities
groups = [
    [1, 3, 5, 11, 13, 14, 19],
    [2, 6, 7, 8, 12, 15],
    [4, 9, 10, 16, 17, 18]
]

# Given solution details
tour = [0, 1, 8, 4, 0]
total_cost = 110.09

# Let's verify the solution
solution_status = verify_tour(city_coordinates, groups, tour, total_cost)
print(solution_status)