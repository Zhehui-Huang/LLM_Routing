import math

# City coordinates
cities = {
    0: (26, 60),
    1: (73, 84),
    2: (89, 36),
    3: (15, 0),
    4: (11, 10),
    5: (69, 22),
    6: (28, 11),
    7: (70, 2),
    8: (47, 50),
    9: (60, 29),
    10: (29, 26),
    11: (85, 68),
    12: (60, 1),
    13: (71, 73),
    14: (82, 47),
    15: (19, 25),
    16: (75, 9),
    17: (52, 54),
    18: (64, 72),
    19: (14, 89),
}

# Given solution
tour = [19, 8, 10, 15, 4, 3, 6, 12, 7, 16, 5, 9, 2, 14, 11, 13, 1, 18, 17, 0, 19]
calculated_cost = 398.66786622516594

def calculate_distance(city1, city2):
    return math.sqrt((cities[city1][0] - cities[city2][0])**2 + (cities[city1][1] - cities[city2][1])**2)

def verify_tour(tour, calculated_cost):
    # Requirement 1 and 4: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Each city must be visited exactly once (except the depot)
    seen = set(tour)
    if len(seen) != 20 or any(city not in seen for city in range(20)):
        return "FAIL"
    
    # Calculate the total travel cost
    total_travel_cost = sum(calculate_distance(tour[i], tour[i+1]) for i in range(len(tour)-1))
    
    # Requirement 3 and 5: Check calculated travel cost
    if abs(total_travel_counter - calculated_cost) > 1e-5:  # Slight tolerance for float comparison
        return "FAIL"
    
    return "CORRECT"
    
# Run the verification
result = verify_tour(tour, calculated_cost)
print(result)