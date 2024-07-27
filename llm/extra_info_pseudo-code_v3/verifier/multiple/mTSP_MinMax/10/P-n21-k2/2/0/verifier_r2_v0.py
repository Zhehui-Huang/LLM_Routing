import math

def euclidean_distance(city1, city2):
    x1, y1 = city1
    y2, x2 = city2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

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
    calculated_costs = []
    
    for tour in tours:
        if tour[0] != 0 or tour[-1] != 0:
            print("FAIL: Tour does not start or end at the depot.")
            return
        
        for city in tour:
            if city < 0 or city >= len(city_coordinates):
                print("FAIL: Invalid city index in the tour.")
                return
        
        tour_cost = calculate_travel_cost(tour, city_coordinates)
        calculated_costs.append(tour_cost)
        max_travel_df_depotcost = max(max_travel_cost, tour_cost)
        
        # Mark cities as visited, excluding the depot (visit depots doesn't count as visiting a city)
        for city in tour[1:-1]:  
            cities_visited[city] += 1
        
    # Check all cities are visited exactly once
    if any(cities_visited[1:] != [1] * (len(city_coordinates) - 1)):
        print("FAIL: Not all cities visited exactly once or some cities are visited more than once.")
        return
        
    if set(calculated_costs) != {116.32876651388246, 100.57956094224302}:
        print("FAIL: Calculated travel costs do not match expected costs.")
        return
    
    print("CORRECT")

verify_solution()