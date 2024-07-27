import math

def euclidean_distance(coord1, coord2):
    return math.sqrt((coord1[0] - coord2[0])**2 + (coord1[1] - coord2[1])**2)

def verify_solution(tour, total_cost):
    # Coordinates for each city
    coordinates = {
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
    
    # City groups
    groups = {
        0: [7, 9],
        1: [1, 3],
        2: [4, 6],
        3: [8],
        4: [5],
        5: [2]
    }
    
    # Check if the tour starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if exactly one city from each group is visited
    group_visit = set()
    visited_cities = set(tour[1:-1])  # exclude depot city from visits check
    
    for g, cities in groups.items():
        if not any(city in visited_cities for city in cities):
            return "FAIL"
        group_visit.update(cities.intersection(visited_cities))
        
        # Verify only one city per group is visited
        if len(group_visit & set(cities)) != 1:
            return "FAIL"
    
    # Calculate and check the total travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, abs_tol=0.0001):
        return "FAIL"
    
    return "CORRECT"

# Test the provided solution
solution_tour = [0, 7, 1, 4, 8, 5, 2, 0]
solution_total_cost = 324.1817486177585
print(verify_solution(solution_tour, solution_total_cost))