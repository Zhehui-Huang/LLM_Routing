import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def check_tour(tour, total_cost):
    # Coordinates of the cities
    cities = {
        0: (26, 60), 1: (73, 84), 2: (89, 36), 3: (15, 0), 4: (11, 10),
        5: (69, 22), 6: (28, 11), 7: (70, 2), 8: (47, 50), 9: (60, 29),
        10: (29, 26), 11: (85, 68), 12: (60, 1), 13: (71, 73), 14: (82, 47),
        15: (19, 25), 16: (75, 9), 17: (52, 54), 18: (64, 72), 19: (14, 89)
    }
    
    # Requirement 1: Start and end at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visit all cities exactly once (excluding depot city which is visited twice)
    unique_cities = set(tour)
    if len(tour) - 1 != len(cities) or any(tour.count(city) != 1 for city in cities if city != 0):
        return "FAIL"
    
    # Requirement 3: Calculate the travel cost and compare with given total
    calculated_cost = 0
    for i in range(len(tour) - 1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Provided tour and cost
tour = [0, 8, 10, 15, 4, 3, 6, 17, 18, 13, 1, 11, 14, 2, 5, 9, 16, 7, 12, 19, 0]
total_cost = 461.6389196296969

# Verify
result = check_tour(tour, total_cost)
print(result)