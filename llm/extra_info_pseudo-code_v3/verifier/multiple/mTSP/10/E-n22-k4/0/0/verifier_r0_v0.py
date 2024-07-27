import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def is_solution_correct(tours, travel_costs, overall_cost, city_coords):
    # Check if each city (except the depot) is visited exactly once
    visited_cities = set()
    for tour in tours:
        for city in tour[1:-1]:  # Exclude the depot (start, end)
            if city in visited_cities:
                return False
            visited_cities.add(city)
    
    # Check if all cities were visited
    if len(visited_cities) + 1 != len(city_coords):  # +1 for depot not being in visited cities
        return False

    # Ensure all tours start and end at the depot
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            return False

    # Check computed travel costs against the provided ones
    computed_costs = []
    for tour in tours:
        cost = 0
        for i in range(len(tour) - 1):
            cost += calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])
        computed_costs.append(round(cost, 2))
    
    # Check if provided costs match computed costs
    if computed_costs != travel_costs:
        return False

    # Check overall cost
    if not math.isclose(sum(travel_costs), overall_cost, rel_tol=1e-2):
        return False

    return True

# City coordinates indexed by city id
city_coordinates = [(145, 215), (151, 264), (159, 261), (130, 254), (128, 252),
                    (163, 247), (146, 246), (161, 242), (142, 239), (163, 236),
                    (148, 232), (128, 231), (156, 217), (129, 214), (146, 208),
                    (164, 208), (141, 206), (147, 193), (164, 193), (129, 189),
                    (155, 185), (139, 182)]

# Solution provided
robot_tours = [
    [0, 16, 14, 18, 15, 12, 0],
    [0, 10, 8, 6, 3, 4, 11, 0],
    [0, 17, 20, 21, 19, 13, 0],
    [0, 1, 2, 5, 7, 9, 0]
]
robot_costs = [76.89, 99.61, 102.92, 111.84]
overall_total_cost = 391.25

# Verification
if is_solution_correct(robot_tours, robot_costs, overall_total_cost, city_coordinates):
    print("CORRECT")
else:
    print("FAIL")