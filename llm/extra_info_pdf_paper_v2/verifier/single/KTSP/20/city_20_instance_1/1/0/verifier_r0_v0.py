import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_tour(cities, tour, expected_cost):
    # Verify there are 20 cities
    if len(cities) != 20:
        return "FAIL"
    
    # Verify starting and ending at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify exactly 7 cities are visited, including the depot
    if len(tour) != 8:  # 7 cities + return to the depot
        return "FAIL"
    
    # Verify total travel cost calculation
    total_cost = 0
    for i in range(len(tour) - 1):
        city_from = tour[i]
        city_to = tour[i + 1]
        total_cost += calculate_euclidean_distance(cities[city_from][0], cities[city_from][1],
                                                   cities[city_to][0], cities[city_to][1])
        
    if not math.isclose(total_cost, expected_cost, abs_tol=1e-2):
        return "FAIL"
    
    return "CORRECT"

# Define city coordinates
cities = [(14, 77), (34, 20), (19, 38), (14, 91), (68, 98), (45, 84), (4, 56), 
          (54, 82), (37, 28), (27, 45), (90, 85), (98, 76), (6, 19), (26, 29), 
          (21, 79), (49, 23), (78, 76), (68, 45), (50, 28), (69, 9)]

# Provided solution tour and cost
solution_tour = [0, 9, 8, 10, 4, 3, 14, 0]
solution_cost = 233.27

# Perform verification
result = verify_tour(cities, solution_tour, solution_cost)
print(result)