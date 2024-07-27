import math

def calculate_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def verify_solution(tours, depots, cities, city_coords):
    # Number of robots
    num_robots = len(tours)
    
    # Check if each robot starts from a designated depot
    for i in range(num_robots):
        if tours[i][0] != depots[i]:
            return "FAIL"
    
    # Collectively all cities visited once
    city_visit_count = {i: 0 for i in range(len(city_coords))}
    for tour in tours:
        for city in tour:
            city_visit_count[city] += 1
    for visit in city_visit_count.values():
        if visit != 1:
            return "FAIL"

    # Calculate total travel cost and validate if the each tour calculates proper Euclidean distances
    total_aggregated_cost = 0
    for tour in tours:
        tour_cost = 0
        for i in range(len(tour)-1):
            cost = calculate_distance(city_coords[tour[i]], city_coords[tour[i+1]])
            tour_cost += cost
        print(tour_cost)  # Check printed if individual tour costs match the provided solution

        # If tours claim zero cost and tour has more than one city visited, that's a failure
        if tour_cost != 0:
            total_aggregated_cost += tour_cost
    # Sum up individual robot tour costs and compare to given total travel cost
    if total_aggregated_cost != 0:
        return "FAIL"

    return "CORRECT"

# Robot tours based on the provided solution
tours = [[0, 0], [0, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]]

# Depot positions (indeces)
depots = [0, 0]

# Cities coordinates dictionary where 0 is depot and city indices are keys
city_coords = {
    0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62), 5: (52, 33), 6: (42, 41), 
    7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68), 12: (43, 67), 
    13: (58, 27), 14: (37, 69), 15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
}

# Verify the solution
result = verify_solution(tours, depots, list(range(19)), city_coords)
print(result)