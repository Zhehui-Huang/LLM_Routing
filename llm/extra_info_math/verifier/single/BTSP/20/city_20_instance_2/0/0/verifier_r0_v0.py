import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution(tour, coordinates):
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"

    # Check if each city is visited exactly once, excluding the depot which should be visited exactly twice (start and end)
    if len(set(tour)) != len(coordinates) or tour.count(0) != 2:
        return "FAIL"

    # Calculate total travel cost and maximum distance between consecutive cities
    total_travel_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = calculate_euclidean_distance(coordinates[tour[i]][0], coordinates[tour[i]][1],
                                            coordinates[tour[i+1]][0], coordinates[tour[i+1]][1])
        total_travel cost += dist
        max_distance = max(max_distance, dist)

    # Check if the maximum distance matches the expected max distance
    if not math.isclose(max_distance, 41.593268686170845, rel_tol=1e-5):
        return "FAIL"
    
    # Check if the total cost matches the expected total cost
    if not math.isclose(total_travel_cost, 626.793982694579, rel_tol=1e-5):
        return "FAIL"
    
    return "CORRECT"

coordinates = [
    (3, 26), (85, 72), (67, 0), (50, 99), (61, 89), (91, 56), (2, 65), (38, 68), 
    (3, 92), (59, 8), (30, 88), (30, 53), (11, 14), (52, 49), (18, 49), (64, 41),
    (28, 49), (91, 94), (51, 58), (30, 48)
]

tour = [0, 19, 12, 14, 7, 16, 11, 15, 2, 9, 13, 5, 18, 1, 4, 17, 3, 10, 8, 6, 0]

# Verify the solution
result = verify_solution(tour, coordinates)
print(result)