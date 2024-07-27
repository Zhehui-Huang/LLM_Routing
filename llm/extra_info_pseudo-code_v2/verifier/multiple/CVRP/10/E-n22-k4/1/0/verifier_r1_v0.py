import math

def euclidean_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution(robots_tours, robots_travel_costs, demands, capacity, coords):
    # Initialize conditions to be checked
    total_demand_fulfilled = True
    within_capacity = True
    correct_travel_cost = True
    all_cities_delivered = set(range(1, len(coords)))  # Excludes the depot city
    visited_cities = set()
    
    overall_cost_calculated = 0

    # Check each robot's tour and calculate total cost
    for i, tour in enumerate(robots_tours):
        tour_demand = 0
        tour_cost = 0
        last_city = 0

        for city in tour:
            if city != 0:
                tour_demand += demands[city]
                visited_cities.add(city)
                
            # Adding travel cost
            if city != last_city:  # not calculating cost from city 0 to city 0 in the beginning
                tour_cost += euclidean_distance(coords[last_city], coords[city])
                last_city = city
        
        # Checking end to start (return to depot) distance
        tour_cost += euclidean_distance(coords[last_city], coords[0])

        overall_cost_calculated += tour_cost

        # Check each robot's capacity
        if tour_demand > capacity:
            within_capacity = False
        
        # Check travel cost close to provided within a small epsilon due to floating-point precision
        if not math.isclose(tour_cost, robots_travel_costs[i], rel_tol=1e-5):
            correct_travel_cost = False

    # Check if all cities are visited
    all_cities_served = all_cities_delivered == visited_cities

    # Check collective demands are met correctly
    total_demand_fulfilled = all_cities_served and within_capacity

    # Sum up all conditions
    solution_correct = total_demand_fulfilled and within_capacity and correct_travel_cost and \
                       math.isclose(overall_cost_calculated, sum(robots_travel_costs), rel_tol=1e-5)
    
    return "CORRECT" if solution_correct else "FAIL"

# Given data from robot tours and provided example
coords = [
    (145, 215), (151, 264), (159, 261), (130, 254), (128, 252), (163, 247),
    (146, 246), (161, 242), (142, 239), (163, 236), (148, 232), (128, 231),
    (156, 217), (129, 214), (146, 208), (164, 208), (141, 206), (147, 193),
    (164, 193), (129, 189), (155, 185), (139, 182)
]
demands = [0, 1100, 700, 800, 1400, 2100, 400, 800, 100, 500, 600, 1200,
           1300, 1300, 300, 900, 2100, 1000, 900, 2500, 1800, 700]
capacity = 6000

robots_tours = [
    [0, 1, 2, 3, 4, 6, 8, 9, 10, 0], 
    [0, 5, 7, 18, 20, 0],
    [0, 19, 21, 11, 13, 0],
    [0, 15, 17, 14, 16, 12, 0]
]
robots_travel_costs = [
    171.60725718200356,
    134.85640632351652,
    126.01535468644786,
    93.11990113957049
]

# Call the verification function
result = verify_solution(robots_tours, robots_travel_costs, demands, capacity, coords)
print(result)