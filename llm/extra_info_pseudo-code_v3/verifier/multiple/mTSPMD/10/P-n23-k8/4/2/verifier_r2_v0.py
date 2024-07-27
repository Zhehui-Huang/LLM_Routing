import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def check_solution(robots_tours, robots_costs, coordinates):
    visited_cities = set()
    total_cost_calculated = 0
    
    for index, tour in enumerate(robots_tours):
        start_depot = tour[0]
        end_depot = tour[-1]
        
        if start_depot != end_depot:
            print("Robot starts and ends at different depots.")
            return "FAIL"
        
        if start_depot != index:
            print("Robot does not start or end at its assigned depot.")
            return "FAIL"
        
        for city in tour[1:-1]:  # Exclude start and end since they are depots
            if city < 8 and city != start_depot:
                print("Robot visits another depot as a city.")
                return "FAIL"
            if city in visited_cities:
                print("City visited more than once.")
                return "FAIL"
            visited_cities.add(city)
        
        calculated_cost = calculate_total_cost(tour, coordinates)
        if not math.isclose(calculated_cost, robots_costs[index], rel_tol=1e-9):
            print(f"Cost calculation error for Robot {index}.")
            return "FAIL"
        
        total_cost_calputed += calculated_cost
        
    if len(visited_cities) != 23:
        print("Not all cities are visited.")
        return "FAIL"
    
    if not math.isclose(total_cost_computed, 138.10021092804732, rel_tol=1e-9):
        print("Overall total cost does not match.")
        return "FAIL"
    
    return "CORRECT"

coordinates = [
    (32, 39), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), (42, 41), (52, 41),
    (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), (37, 69),
    (38, 46), (61, 33), (62, 63), (63, 69), (45, 35), (30, 40), (56, 37)
]

robots_tours = [
    [21, 0, 0], [10, 16, 1, 1], [13, 2, 2], [8, 12, 18, 19, 3, 3],
    [11, 15, 4, 4], [14, 17, 22, 5, 5], [20, 6, 6], [9, 7, 7]
]

robots_costs = [
    2.23606797749979, 17.787462441017844, 9.055385138137417, 54.22561331993363,
    19.269420078413777, 18.768182419424598, 6.708203932499369, 10.04987562112089
]

print(check_solution(robots_tours, robots_costs, coordinates))