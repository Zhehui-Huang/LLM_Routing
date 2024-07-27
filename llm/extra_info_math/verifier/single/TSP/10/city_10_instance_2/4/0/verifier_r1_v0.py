import math

def compute_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_cost, city_coordinates):
    # Define the requirements
    start_end_at_depot = (tour[0] == 0 and tour[-1] == 0)
    all_cities_visited_once = (len(set(tour[1:-1])) == len(tour[1:-1]) == len(city_coordinates) - 1)
    
    # Calculate travel cost
    calculated_total_cost = sum(compute_euclidean_distance(city_coordinates[tour[i]][0], city_coordinates[tour[i]][1],
                                                           city_coordinates[tour[i + 1]][0], city_coordinates[tour[i + 1]][1])
                                for i in range(len(tour) - 1))
    
    correct_travel_cost = (abs(calculated_total_cost - total_cost) < 1e-5)

    all_conditions_met = all([start_end_at_depot, all_cities_visited_once, correct_travel_cost])
    
    output = "CORRECT" if all_conditions_met else "FAIL"
    return output

# List of city coordinates including the depot
city_coordinates = {
    0: (90, 3), 1: (11, 17), 2: (7, 27), 3: (95, 81), 4: (41, 54), 5: (31, 35), 6: (23, 95), 
    7: (20, 56), 8: (49, 29), 9: (13, 17)
}

# The provided solution details
tour = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
total_cost = 0  # As per the environment, this is wrong, needs to be checked with actual cost calculation

# Execute verification
verification_result = verify_solution(tour, total_l_cost, city_coordinates)
print(verification_result)