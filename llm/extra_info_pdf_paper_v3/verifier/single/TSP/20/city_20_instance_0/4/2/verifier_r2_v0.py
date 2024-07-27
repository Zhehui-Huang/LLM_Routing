import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(tour, reported_cost):
    # Define the city coordinates index by their given order in the description
    cities = [
        (8, 11),  # depot city 0
        (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
        (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), 
        (40, 87), (20, 97), (5, 59), (61, 25), (62, 88), 
        (13, 43), (61, 28), (60, 63), (93, 15), (8, 11)  # Civil indices adjusted for zero indexing; repeating depot city.
    ]
    
    # [Requirement 1] Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Visit all cities exactly once
    unique_cities_visited = set(tour)
    if len(unique_cities_visited) != 21 or any(i not in unique_cities_visited for i in range(20)):
        return "FAIL"
    
    # [Requirement 3] Travel cost calculated using Euclidean distance
    # [Requirement 4] Find the shortest possible tour
    total_calculated_cost = 0
    for i in range(len(tour) - 1):
        total_calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(total_calculated_check, reported_cost, abs_tol=0.01):
        return "FAIL"

    # If all requirements are satisfied, return "CORRECT"
    return "CORRECT"

# Provided solution to be verified
tour = [0, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
reported_cost = 1170.86

# Call the function to verify the tour and output the result
result = verify_solution(tour, reported_cost)
print(result)