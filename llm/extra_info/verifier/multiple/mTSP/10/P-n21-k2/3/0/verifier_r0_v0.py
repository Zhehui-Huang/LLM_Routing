import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def total_tour_cost(tour, coordinates):
    tour_cost = 0
    for i in range(len(tour) - 1):
        tour_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i + 1]])
    return tour_cost

def validate_tour(tour, tour_cost, coordinates):
    calculated_cost = total_tour_cost(tour, coordinates)
    return math.isclose(tour_cost, calculated_cost, rel_tol=1e-9)

def run_tests():
    coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
        (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), 
        (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33), 
        (62, 63), (63, 69), (45, 35)
    ]
    
    tour1 = [0, 6, 2, 13, 9, 17, 5, 1, 4, 3, 18, 19, 0]
    cost1 = 174.02238041636645

    tour2 = [0, 16, 10, 12, 15, 11, 8, 7, 20, 14, 0]
    cost2 = 152.8264082822842

    valid1 = validate_tour(tour1, cost1, coordinates)
    valid2 = validate_tour(tour2, cost2, coordinates)

    city_visited = set(tour1[1:-1] + tour2[1:-1])
    all_cities_visited_once = len(city_visited) == 20 and all(x in range(1, 21) for x in city_visited)
    
    start_end_at_depot = tour1[0] == 0 and tour1[-1] == 0 and tour2[0] == 0 and tour2[-1] == 0
    
    if valid1 and valid2 and all_cities_visited_once and start_end_at_depot:
        print("CORRECT")
    else:
        print("FAIL")

run_tests()