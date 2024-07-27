import math

def euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def calculate_travel_cost(tour, city_coordinates):
    total_cost = 0
    for i in range(len(tour) - 1):
        total_cost += euclidean_distance(city_coordinates[tour[i]], city_coordinates[tour[i+1]])
    return total_cost

def verify_solution():
    city_coordinates = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
        (37, 69), (38, 46), (61, 33), (62, 63), (63, 69), (45, 35)
    ]

    tours = [
        [0, 4, 11, 15, 12, 3, 19, 18, 8, 10, 1, 0],
        [0, 16, 6, 2, 13, 9, 17, 14, 5, 7, 20, 0]
    ]

    # Initialize metric to check if all cities are visited exactly once
    cities_visited = [0] * len(city_coordinates)
    
    max_travel_cost = 0
    for tour in tours:
        # Validate start and end at the depot
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Tour does not start or end at the depot.")
            return
        
        # Mark visited cities
        for city in tour:
            if 0 <= city < len(city_coordinates):
                cities_visited[city] += 1
            else:
                print("FAIL: Invalid city index in the tour.")
                return
            
        # Calculate tour cost and update max travel cost
        tour_cost = calculate_travel_cost(tour, city_coordinates)
        max_travel_cost = max(max_travel_cost, tour_cost)

    # Check that all cities except depot are visited exactly once
    if not all(visited == 1 for visited in cities_visited[1:]):
        print("FAIL: Not all cities visited exactly once or some cities are visited more than once.")
        return

    expected_max_cost = 116.32876651388246
    if abs(max_travel_cost - expected_max_cost) > 1e-9:
        print("FAIL: Max travel cost is not minimal as expected.")
        return

    print("CORRECT")

verify_solution()