import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def check_solution(tour, cities):
    if tour[0] != tour[-1] or len(set(tour)) != len(cities):
        return "FAIL"
    
    total_travel_cost = 0
    max_distance_between_cities = 0
    
    for i in range(len(tour) - 1):
        city1 = cities[tour[i]]
        city2 = cities[tour[i + 1]]
        distance = euclidean_distance(city1, city2)
        
        total_travel_cost += distance
        if distance > max_distance_between_cities:
            max_distance_between_cities = distance

    # Check rounded total travel cost and max distance
    rounded_total_cost = round(total_travel_cost, 6)
    rounded_max_distance = round(max_distance_between_cities, 6)
    if rounded_total_cost == round(408.41360886151256, 6) and rounded_max_distance == round(61.68468205316454, 6):
        return "CORRECT"
    else:
        return "FAIL"

# Cities positions
cities = [
    (79, 15),   # depot city 0
    (79, 55),   # city 1
    (4, 80),    # city 2
    (65, 26),   # city 3
    (92, 9),    # city 4
    (83, 61),   # city 5
    (22, 21),   # city 6
    (97, 70),   # city 7
    (20, 0),    # initial error in city 8 coordinates fixed
    (66, 62)    # city 9
]

# Provided Solution Tour
tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]

# Test solution
result = check_solution(tour, cities)
print(result)