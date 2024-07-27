import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tour, total_cost):
    cities = {
        0: (84, 67),
        1: (74, 40),
        2: (71, 13),
        3: (74, 82),
        4: (97, 28),
        5: (0, 31),
        6: (8, 62),
        7: (74, 56),
        8: (85, 71),
        9: (6, 76)
    }
    
    city_groups = [
        [7, 9],
        [1, 3],
        [4, 6],
        [8],
        [5],
        [2]
    ]

    # Verify the robot starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify the robot visits exactly one city from each group
    visited_groups = [False] * len(city_groups)
    unique_cities = set(tour)
    
    for city in tour:
        found = False
        for i, group in enumerate(city_groups):
            if city in group:
                if visited_groups[i]:
                    return "FAIL"  # City already visited from this group
                visited_groups[i] = True
                found = True
                break
        if not found:
            return "FAIL"  # City not in any group
            
    if not all(visited_groups):
        return "FAIL"

    # Calculate and verify the total travel cost based on Euclidean distance
    calculated_cost = 0
    for i in range(1, len(tour)):
        calculated_cost += calculate_name(cities[tour[i-1]], cities[tour[i]])

    if abs(calculated_cost - total_cost) > 0.01:
        return "FAIL"

    return "CORRECT"

# Test
tour = [0, 7, 1, 4, 8, 5, 2, 0]
total_cost = 324.18
print(verify_solution(tour, total_cost))