def calculate_distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

def verify_solution(tour, city_positions):
    # Requirement 1: Starts and ends at depot city (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city must be visited exactly once
    if sorted(tour[1:-1]) != list(range(1, 20)):
        return "FAIL"
    
    # Calculating distances between consecutive cities
    max_distance = 0
    total_distance = 0
    for i in range(len(tour) - 1):
        city1 = tour[i]
        city2 = tour[i + 1]
        distance = calculate_distance(city_positions[city1][0], city_positions[city1][1], city_positions[city2][0], city_positions[city2][1])
        total_distance += distance
        max_distance = max(max_distance, distance)
    
    # Requirement 3: Check if the reported max distance between consecutive cities matches calculated max distance
    reported_max_distance = 32.38826948140329
    if not (max_distance - 0.01 <= reported_max_distance <= max_distance + 0.01):
        return "FAIL"
    
    # Checking if the reported total distance matches the sum of calculated distances
    reported_total_distance = 389.4158520683985
    if not (total_distance - 0.01 <= reported_total_distance <= total_distance + 0.01):
        return "FAIL"
    
    return "CORRECT"

# Provided solution
tour = [0, 4, 16, 14, 7, 12, 9, 11, 15, 18, 3, 10, 19, 2, 6, 5, 8, 17, 13, 1, 0]
city_positions = [(8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
                  (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87),
                  (20, 97), (61, 25), (5, 59), (62, 88), (13, 43), (61, 28), 
                  (60, 63), (93, 15)]

# Check tour
result = verify_solution(tour, city_positions)
print(result)