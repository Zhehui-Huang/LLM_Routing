import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, total_cost):
    # Define city coordinates
    cities = {
        0: (14, 77), 1: (34, 20), 2: (19, 38), 3: (14, 91), 4: (68, 98), 5: (45, 84),
        6: (4, 56), 7: (54, 82), 8: (37, 28), 9: (27, 45), 10: (90, 85), 11: (98, 76),
        12: (6, 19), 13: (26, 29), 14: (21, 79), 15: (49, 23), 16: (78, 76), 17: (68, 45),
        18: (50, 28), 19: (69, 9)
    }
    
    # Check if the tour starts and ends at the depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if all cities are visited exactly once, except for the depot city
    unique_cities = set(tour)
    if len(unique_cities) != len(cities) + 1:  # +1 because city 0 is visited twice
        return "FAIL"
    for city in range(1, len(cities)):
        if city not in unique_cities:
            return "FAIL"
    
    # Check for calculation of total travel cost based on Euclidean distance
    calculated_cost = 0
    for i in range(len(tour)-1):
        calculated_cost += euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    
    if not math.isclose(calculated_cost, total_cost, rel_tol=1e-9):
        return "FAIL"
    
    return "CORRECT"

# Proposed tour and total cost
tour = [0, 3, 14, 5, 7, 4, 16, 10, 11, 17, 19, 15, 18, 8, 1, 13, 12, 2, 9, 6, 0]
total_cost = 381.11325116397535

# Run verification
result = verify_tour(tour, total_cost)
print(result)