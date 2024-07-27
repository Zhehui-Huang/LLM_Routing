import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_tours(cities, robots_tours):
    all_cities_visited = set()
    for tour in robots_tours:
        for city in tour:
            if city in all_cities_visited and city != 0:  # We allow repeating the depot (city 0)
                return False
            all_cities_visited.add(city)
    return all_cities_visited == set(range(len(cities)))

def calculate_tour_cost(cities, tour):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
    return total_cost

def test_solution():
    cities = [ 
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), 
        (45, 35), (32, 39), (56, 37)
    ]

    robots_tours = [
        [0, 21, 19, 0],
        [0, 11, 3, 0],
        [0, 8, 17, 0],  
        [0, 22, 15, 0],
        [0, 5, 9, 0],
        [0, 10, 12, 0],
        [0, 1, 13, 0],
        [0, 20, 14, 7, 2, 6, 16, 18, 4, 0]
    ]
    
    total_travel_cost_given = 706.265156275141
    total_travel_cost_calculated = 0

    if not verify_tours(cities, robots_tours):
        return "FAIL: Tours validation failed."

    for tour in robots_tours:
        total_travel_cost_calculated += calculate_tour_cost(cities, tour)
    
    if not math.isclose(total_travel_cost_calculated, total_travel_cost_given, rel_tol=1e-3):
        return "FAIL: Total travel cost mismatch."
    
    return "CORRECT"

# Call the test function
print(test_solution())