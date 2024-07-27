import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def check_requirements():
    cities = [(16, 90), (43, 99), (80, 21), (86, 92), (54, 93), (34, 73), (6, 61), 
              (86, 69), (30, 50), (35, 73), (42, 64), (64, 30), (70, 95), 
              (29, 64), (32, 79)]

    tour = [0, 1, 4, 12, 3, 7, 2, 11, 10, 13, 9, 5, 14, 6, 8, 0]
    expected_total_distance = 335.1658023375991
    expected_max_distance = 48.373546489791295

    # [Requirement 6]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 6]
    if any(t not in tour for t in range(len(cities))):
        return "FAIL"
    
    # [Requirement 2]
    if len(set(tour)) != len(tour):
        return "FAIL"
    
    # Calculate distances
    travel_distances = []
    total_distance = 0
    for i in range(len(tour) - 1):
        xy1 = cities[tour[i]]
        xy2 = cities[tour[i + 1]]
        dist = calculate_euclidean_distance(xy1[0], xy1[1], xy2[0], xy2[1])
        travel_distances.append(dist)
        total_distance += dist
    
    # [Requirement 4]
    if not math.isclose(total_distance, expected_total_distance, abs_tol=1e-5):
        return "FAIL"
    
    # [Requirement 8]
    max_distance = max(travel_distances)
    if not math.isclose(max_distance, expected_max_distance, abs_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

# Running the verification test
result = check_requirements()
print(result)