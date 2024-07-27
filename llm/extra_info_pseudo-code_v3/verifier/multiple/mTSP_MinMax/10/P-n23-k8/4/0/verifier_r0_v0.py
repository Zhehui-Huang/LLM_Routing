import math

# Robot tours and costs as given
tours = [
    [0, 4, 11, 13, 16, 0],
    [0, 2, 7, 17, 0],
    [0, 8, 10, 18, 23, 0],   # Invalid city index 23
    [0, 19, 20, 0],
    [0, 3, 9, 14, 0],
    [0, 22, 0],
    [0, 5, 12, 0],
    [0, 6, 15, 21, 0]
]
costs = [93.09, 62.82, 31.17, 65.52, 47.16, 48.17, 85.02, 40.59]
max_cost_given = 93.09

# City coordinates excluding invalid city 23
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_requirements(tours, costs):
    all_cities_visited = []
    max_cost_calculated = 0
    
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            print("Fails Requirement 2")
            return "FAIL"
        
        cities_in_tour = tour[1:-1]  # Exclude depot city from checks
        all_cities_visited += cities_in_tour
        
        tour_cost = 0
        for i in range(len(tour) - 1):
            city_index1, city_index2 = tour[i], tour[i+1]
            if city_index1 >= len(city_coordinates) or city_index2 >= len(city_coordinates):
                print("Invalid city index in tour")
                return "FAIL"
            distance = calculate_distance(city_coordinates[city_price1], city_coordinates[city_index2])
            tour_cost += distance
        
        if abs(tour_cost - costs[tours.index(tour)]) > 0.01:
            print("Fails Requirement 6: Incorrect calculated cost")
            return "FAIL"
        
        max_cost_calculated = max(max_cost_calculated, tour_cost)

    if len(set(all_cities_visited)) != len(city_coordinates) - 1:
        print("Fails Requirement 4: Not all cities visited or some visited more than once")
        return "FAIL"

    if max_cost_calculated != max_cost_given:
        print("Fails Requirement 3: Incorrect max cost")
        return "FAIL"

    return "CORRECT"

# Test verification
result = verify_requirements(tours, costs)
print(result)