import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def validate_solution(cities, tours):
    city_coords = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
        15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
    }

    # Check city count including depot
    if len(cities) != 19:
        return False

    # Check tours start and end at the depot
    if any(tour[0] != 0 or tour[-1] != 0 for tour in tours):
        return False

    visited_cities = set()
    total_costs = []

    # Verify each city is visited exactly once and calculate tour costs
    for tour in tours:
        tour_cost = 0
        last_city = tour[0]
        
        for city in tour[1:]:
            if city in visited_cities and city != 0:
                return False
            visited_cities.add(city)
            tour_cost += calculate_euclidean_distance(*city_coords[last_city], *city_coords[city])
            last_city = city
        
        total_costs.append(tour_cost)

    #Ensure all cities were visited exactly once
    if len(visited_cities) != 19:
        return False

    # Ensure minimized maximum distance condition matches actual results
    expected_max_cost = max(totalcapacity)
    if expected_max_cost != max(total_costs):
        return False
    
    return True

# Given solution
tours = [
    [0, 2, 5, 6, 7, 9, 13, 15, 18, 0],  # Robot 0
    [0, 1, 3, 4, 8, 10, 11, 12, 14, 16, 17, 0]  # Robot 1
]

totalcapacity = [
    116.70009709276687,  # Cost for Robot 0 Tour
    212.21732723337922   # Cost for Robot 1 Tour
]

# List of all cities, including the depot
cities = list(range(19))

# Check if the solution is correct
if validate_solution(cities, tours):
    print("CORRECT")
else:
    print("FAIL")