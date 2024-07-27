import math

def calculate_distance(city1, city2):
    # Using Euclidean distance to compute the distance between two cities
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour(tour, total_travel_cost):
    # City coordinates, with city index being mapped to tuple of coordinates
    city_coordinates = {
        0: (35, 40), 1: (39, 41), 2: (81, 30), 3: (5, 50), 4: (72, 90),
        5: (54, 46), 6: (8, 70), 7: (97, 62), 8: (14, 41), 9: (70, 44),
        10: (27, 47), 11: (41, 74), 12: (53, 80), 13: (21, 21), 14: (12, 39)
    }
    
    # Grouping information
    city_groups = [
        [3, 8], [4, 13], [1, 2], [6, 14], [5, 9], [7, 12], [10, 11]
    ]
    
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    visited_groups = [False] * len(city_groups)
    for city in tour[1:-1]:  # excluding the depot city included at start and end
        belongs_to_group = False
        for idx, group in enumerate(city_groups):
            if city in group:
                if visited_groups[idx]:
                    return "FAIL"  # city from this group already visited
                visited_groups[idx] = True
                belongs_to_group = True
        if not belongs_to_group:
            return "FAIL"  # city not belonging to any group
    
    if not all(visited_groups):
        return "FAIL"  # Not all groups are visited
    
    # Calculate travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    
    # Check if the total travel cost matches the calculated travel cost
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-6):
        return "FAIL"
    
    # If all checks passed
    return "CORRECT"

# Given solution
tour = [0, 8, 13, 1, 14, 5, 12, 11, 0]
total_travel_cost = 220.73043826129523

# Verify the solution
result = verify_tour(tour, total_travel_cost)
print(result)