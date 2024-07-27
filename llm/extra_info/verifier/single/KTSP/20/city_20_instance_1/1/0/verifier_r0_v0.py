import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def test_tour(tour, cost, cities):
    # [Requirement 1]
    if not (tour[0] == 0 and tour[-1] == 0):
        return "FAIL: Requirement 1"
    
    # [Requirement 2]
    if len(tour) != 8 or len(set(tour)) != 8:
        return "FAIL: Requirement 2"
    
    # [Requirement 5]
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL: Requirement 5"
    
    # Calculating the travel cost
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
    
    # [Requirement 4] & [Requirement 6]
    if round(calculated_cost, 2) != round(cost, 2):
        return "FAIL: Requirement 4 and 6"
    
    return "CORRECT"

# City coordinates as provided
city_locations = [
    (14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
    (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
    (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)
]

tour = [0, 6, 2, 13, 8, 9, 14, 0]
reported_cost = 130.67

result = test_tour(tour, reported_cost, city_locations)
print(result)