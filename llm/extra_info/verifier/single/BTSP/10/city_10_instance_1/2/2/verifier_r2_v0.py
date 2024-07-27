import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tour(tour, cities):
    # Check if the tour starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check if every city is visited exactly once (excluding the start/end at depot)
    if sorted(tour) != sorted(list(range(len(cities)))):
        return "FAIL"
    
    # Check the travel cost using Euclidean distance
    total_travel_cost = 0
    max_distance_between_cities = 0
    for i in range(len(tour)-1):
        distance = calculate_distance(cities[tour[i]], cities[tour[i+1]])
        total_travel_cost += distance
        max_distance_between_cities = max(max_distance_between_cities, distance)

    # Check if provided values match
    if abs(total_travel_cost - 291.41) > 1e-2 or abs(max_distance_between_cities - 56.61) > 1e-2:
        return "FAIL"

    return "CORRECT"

# City coordinates
cities = [
    (53, 68), # City 0
    (75, 11), # City 1
    (91, 95), # City 2
    (22, 80), # City 3
    (18, 63), # City 4
    (54, 91), # City 5
    (70, 14), # City 6
    (97, 44), # City 7
    (17, 69), # City 8
    (95, 89)  # City 9
]

# Provided tour
tour = [0, 3, 4, 8, 5, 2, 9, 7, 1, 6, 0]

# Checking the tour
result = verify_tour(tour, cities)
print(result)