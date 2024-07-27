import math

def calculate_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

# City coordinates (index corresponds to city number)
coordinates = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]

# Tours given by the solution
tours = {
    0: ([0, 5, 7, 9, 6, 8, 10, 12, 15, 18, 20, 17, 21, 19, 16, 14, 13, 11, 4, 0], 301.6041542788592),
    1: ([1, 5, 7, 9, 6, 8, 10, 12, 15, 18, 20, 17, 21, 19, 16, 14, 13, 11, 4, 1], 270.9213842233134),
    2: ([2, 5, 7, 9, 6, 8, 10, 12, 15, 18, 20, 17, 21, 19, 16, 14, 13, 11, 4, 2], 271.01073319618183),
    3: ([3, 5, 7, 9, 6, 8, 10, 12, 15, 18, 20, 17, 21, 19, 16, 14, 13, 11, 4, 3], 260.7331713460951)
}

def verify_solution(tours):
    all_visited_cities = set()
    total_calculated_cost = 0
    
    for robot_id, (tour, reported_cost) in tours.items():
        # Verify each tour starts and ends at the assigned depot:
        if tour[0] != tour[-1] or tour[0] != robot_id:
            return "FAIL"

        # Verify cities visited:
        visited_cities = set(tour[1:-1])
        if any(city in all_visited_cities for city in visited_cities):
            return "FAIL"
        all_visited_cities.update(visited_cities)
        
        # Verify calculated distances:
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += calculate_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
        total_calculated_cost += calculated_cost

        if not math.isclose(calculated_cost, reported_cost, rel_tol=0.001):
            return "FAIL"
    
    # Verify all cities are visited:
    if len(all_visited_cities) != len(coordinates) - 4:  # exclude depots
        return "FAIL"
    
    # Verify cost is as stated (Overall cost):
    reported_total_cost = sum(report[1] for report in tours.values())
    if not math.isclose(total_calculated_cost, reported_total_cost, rel_tol=0.001):
        return "FAIL"

    return "CORRECT"

# Running the verification
result = verify_solution(tours)
print(result)