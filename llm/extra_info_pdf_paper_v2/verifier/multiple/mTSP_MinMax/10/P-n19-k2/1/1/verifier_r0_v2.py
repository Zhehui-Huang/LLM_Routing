import math

def calculate_distance(city1, city2):
    """ Calculate Euclidean distance between two coordinate points. """
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def check_solution(tours, city_coordinates):
    """ Check the validity of the tours against the given requirements. """
    visited = set()
    all_cities = set(range(1, len(city_coordinates)))  # excluding the depot city

    for tour in tours:
        for city in tour[1:-1]:  # exclude depot visits at beginning and end
            visited.add(city)

    requirement_1 = (visited == all_cities)
    requirement_2 = all(tour[0] == 0 and tour[-1] == 0 for tour in tours)

    max_travel_cost = 0
    travel_costs = []
    for tour in tours:
        travel_cost = 0
        for i in range(len(tour) - 1):
            travel_cost += calculate_distance(city_coordinates[tour[i]], city_coordinates[tour[i + 1]])
        travel_costs.append(travel_cost)
        max_travel_cost = max(max_travel_cost, travel_cost)

    requirement_3 = (max_travel_cost == max(travel_costs))
    
    requirement_4_all_cost_calculated_correctly = True
    requirement_5 = all(isinstance(t, list) and t[0] == 0 and t[-1] == 0 for t in tours)
    
    for i, cost in enumerate(travel_costs):
        correct_cost = sum(calculate_distance(city_coordinates[tours[i][j]], city_coordinates[tours[i][j + 1]]) for j in range(len(tours[i]) - 1))
        if abs(cost - correct_cost) > 0.001:
            requirement_4_all_cost_calculated_correctly = False
            break

    if all([requirement_1, requirement_2, requirement_3, requirement_4_all_cost_calculated_correctly, requirement_5]):
        return "CORRECT"
    else:
        return "FAIL"

# Test parameters
city_coordinates = [
    (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), 
    (52, 33), (42, 41), (52, 41), (57, 58), (62, 42),
    (42, 57), (27, 68), (43, 67), (58, 27), (37, 69),
    (61, 33), (62, 63), (63, 69), (45, 35)
]

tours = [
    [0, 1, 2, 0],  # Example tour for Robot 0
    [0, 3, 4, 0]   # Example tour for Robot 1
]

# Execute test
result = check_solution(tours, city_coordinates)
print(result)