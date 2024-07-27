import math

def calculate_distance(c1, c2):
    return math.sqrt((c1[0] - c2[0])**2 + (c1[1] - c2[1])**2)

def verify_solution():
    # City coordinates
    cities = [
        (30, 40), (37, 52), (49, 49), (52, 64), (31, 62), 
        (52, 33), (42, 41), (52, 41), (57, 58), (62, 42), 
        (42, 57), (27, 68), (43, 67), (58, 48), (58, 27), 
        (37, 69)
    ]
    
    # Robot tours and their calculated travel costs
    tours = [
        ([0, 1, 0], 13.892443989449804),
        ([2, 3, 0], 36.320854582406994),
        ([4, 5, 0], 57.827743125481554),
        ([6, 7, 0], 22.041594578792296),
        ([9, 8, 0], 48.82549369800301),
        ([10, 11, 0], 39.409727284423084),
        ([13, 12, 0], 53.32787643094248),
        ([15, 14, 0], 76.79029530784818)
    ]
    
    # Check all cities are visited exactly once
    all_visited = set()
    for tour, _ in tours:
        # If depot is counted at the beginning and the end, skip one instance
        all_visited.update(tour[1:-1])
    all_visited.update([tour[0] for tour, _ in tours])  # Adding starting depots as they are endpoints as well
    
    if len(all_visited) != 16:
        return "FAIL"
    
    # Total cost from solution
    calculated_total_cost = 0.0
    for tour, given_cost in tours:
        tour_cost = 0.0
        if len(tour) >= 2:
            for i in range(len(tour) - 1):
                tour_cost += calculate_distance(cities[tour[i]], cities[tour[i+1]])
        
        # Compare each calculated cost with the provided cost
        if not math.isclose(tour_cost, given_cost, rel_tol=1e-9):
            return "FAIL"
        
        calculated_total_cost += tour_cost
    
    # Given overall total travel cost
    given_overall_total_cost = 348.43602899734736
    
    # Check if overall cost matches
    if not math.isclose(calculated_total_cost, given_overall_total +:+00000000
        return "FAIL"
    
    return "CORRECT"

# Run the unit tests
print(verify_solution())