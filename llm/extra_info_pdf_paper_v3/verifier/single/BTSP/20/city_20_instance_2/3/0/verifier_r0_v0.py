import math

# City coordinates as given
cities = {
    0: (3, 26), 1: (85, 72), 2: (67, 0), 3: (50, 99), 4: (61, 89),
    5: (91, 56), 6: (2, 65), 7: (38, 68), 8: (3, 92), 9: (59, 8),
    10: (30, 88), 11: (30, 53), 12: (11, 14), 13: (52, 49), 14: (18, 49),
    15: (64, 41), 16: (28, 49), 17: (91, 94), 18: (51, 58), 19: (30, 48)
}

# Given solution
tour = [0, 12, 0, 14, 16, 19, 16, 11, 7, 18, 13, 15, 9, 2, 9, 15, 13, 18, 7, 10, 3, 4, 1, 5, 1, 17, 1, 4, 3, 10, 7, 11, 16, 14, 6, 8, 6, 14, 0]
given_total_cost = 676.68
given_max_distance = 33.38

def euclidean_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def verify_solution(tour, given_total_cost, given_max_distance):
    # Checking Requirement 1: visit each city exactly once except depot (twice)
    unique_visits = set(tour)
    if len(unique_visits) != 20 or tour.count(0) != 2:
        return "FAIL"
    
    for city in range(1, 20):
        if city not in unique_visits:
            return "FAIL"
    
    # Calculating cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        distance = euclidean_distance(tour[i], tour[i + 1])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check computed total travel cost
    if not math.isclose(calculated_total_cost, given_total_cost, abs_tol=0.1):
        return "FAIL"
    
    # Check computed max distance
    if not math.isclose(calculated_max_distance, given_max_distance, abs_tol=0.1):
        return "FAIL"
    
    return "CORRECT"

# Running the verification
print(verify_solution(tour, given_total_cost, given_max_distance))