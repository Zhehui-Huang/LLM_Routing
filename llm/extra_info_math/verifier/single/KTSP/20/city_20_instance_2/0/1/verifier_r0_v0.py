import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, total_travel_cost, city_coordinates):
    if not tour[0] == tour[-1] == 0:
        return "FAIL"  # check if tour starts and ends at the depot city 0
    
    if len(set(tour)) != 10:
        return "FAIL"  # check if exactly 10 distinct cities are visited
    
    accumulated_distance = 0
    for i in range(len(tour) - 1):
        city_a = tour[i]
        city_b = tour[i + 1]
        accumulated_distance += calculate_euclidean_distance(
            city_coordinates[city_a][0],
            city_coordinates[city_a][1],
            city_coordinates[city_b][0],
            city_coordinates[city_b][1]
        )
    
    if round(accumulated_distance, 12) != round(total_travel_cost, 12):
        return "FAIL"  # check if provided travel cost matches the calculated travel cost
    
    return "CORRECT"

# Provided city coordinates
city_coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), 
    (2, 65), (38, 68), (3, 92), (59, 8), (30, 88), (30, 53), 
    (11, 14), (52, 49), (18, 49), (64, 41), (28, 49), (91, 94), 
    (51, 58), (30, 48)
]

# Provided solution
tour = [0, 12, 15, 13, 18, 7, 11, 19, 16, 14, 0]
total_travel_cost = 175.47723265355

# Validate the provided solution
solution_status = verify_solution(tour, total_travel_cost, city_coordinates)
print(solution_status)