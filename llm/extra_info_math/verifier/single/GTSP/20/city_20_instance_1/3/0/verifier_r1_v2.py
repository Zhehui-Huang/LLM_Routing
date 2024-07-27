import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities, groups):
    if not tour or len(tour) < 2:
        return "FAIL", "Tour is empty or too short to be valid"
    
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL", "Tour does not start or end at depot city"
    
    visited_groups = set()
    for i in range(1, len(tour)-1):  # exclude the depot city at start and end
        city = tour[i]
        city_group_found = False
        for group_index, group in enumerate(groups):
            if city in group:
                if group_index in visited_groups:
                    return "FAIL", "City from group visited more than once"
                visited_groups.add(group_index)
                city_group_found = True
                break
        if not city_group_found:
            return "FAIL", f"City {city} does not match any specified groups"
    
    if len(visited_groups) != len(groups):
        return "FAIL", "Not all groups are visited exactly once"
    
    return "CORRECT", "All requirements met"

# Define city coordinates
cities = {
    0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98),
    5: (45, 84), 6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45),
    10: (90, 85), 11: (98, 76), 12: (6, 19), 13: (26, 29), 14: (21, 79),
    15: (49, 23), 16: (78, 76), 17: (68, 45), 18: (50, 28), 19: (69, 9)
}

# Define group data
groups = [
    [5, 6, 7, 11, 17],
    [1, 4, 8, 13, 16],
    [2, 10, 15, 18, 19],
    [3, 9, 12, 14]
]

# Example Usage:
tour_solution = [0, 5, 1, 2, 3, 0]  # Example input to verify
result, message = verify_tour(tour_solution, cities, groups)
print(f"Result: {result}, Message: {message}")