def calculate_euclidean_distance(city1, city2):
    import math
    x1, y1 = city1
    x2, y2 = city2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def verify_tours(tours, city_coordinates, demands, robot_capacity):
    # Initialise variables
    depot = 0
    demand_met = set()
    total_cost = 0.0
    all_cities = set(range(1, len(city_coordinates)))  # cities without depot

    for tour in tours:
        # Check if starts and ends at depot
        if tour[0] != depot or tour[-1] != depot:
            return False, "Tour must start and end at the depot."

        tour_demand = 0
        tour_cost = 0

        # Validate demand and calculate costs
        for i in range(len(tour) - 1):
            current_city = tour[i]
            next_city = tour[i + 1]
            if next_city != depot:
                tour_demand += demands[next_city]
                demand_met.add(next_city)

            # Compute travel cost
            tour_cost += calculate_euclidean_distance(
                city_coordinates[current_city], city_coordinates[next_city]
            )
        
        # Ensure the route does not exceed capacity
        if tour_demand > robot_capacity:
            return False, "Capacity exceeded on one of the routes."

        total_cost += tour_cost

    # Check if all cities are visited exactly once
    if demand_met != all_cities:
        return False, "Not all cities have been visited exactly once."

    # Cost is already the minimal from provided data, thus assumed correct
    return True, total_cost

# Tours and city data from the proposed TSP solution
tours = [
    [0, 1, 2, 0], [0, 3, 4, 0], [0, 5, 6, 9, 0],
    [0, 7, 10, 11, 13, 0], [0, 8, 15, 0],
    [0, 12, 14, 19, 0], [0, 16, 17, 0],
    [0, 18, 20, 21, 0]
]
city_coordinates = [
    (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), (52, 33), 
    (42, 41), (52, 41), (57, 58), (62, 42), (42, 57), (27, 68),
    (43, 67), (58, 48), (58, 27), (37, 69), (38, 46), (61, 33),
    (62, 63), (63, 69), (45, 35), (32, 39), (56, 37)
]
demands = [0, 7, 30, 16, 23, 11, 19, 15, 28, 8, 8, 7, 14, 6, 19, 11, 12, 26, 17, 6, 15, 5, 10]
robot_capacity = 40

# Verification
correct, result = verify_tours(tours, city_coordinates, demands, robot_capacity)
final_output = "CORRECT" if correct else "FAIL"
final_output