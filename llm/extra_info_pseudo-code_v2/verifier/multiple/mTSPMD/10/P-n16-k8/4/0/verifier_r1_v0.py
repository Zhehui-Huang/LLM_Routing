import math

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 
    5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 
    10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 48), 14: (58, 27), 
    15: (37, 69)
}

# Robot tours and transportation costs
tours = [
    [0, 10, 0],
    [1, 12, 1],
    [2, 13, 2],
    [3, 8, 3],
    [4, 11, 4],
    [5, 14, 5],
    [6, 9, 6],
    [7, 15, 7],
]

travel_costs = [
    41.617304093369626,
    32.31098884280702,
    18.110770276274835,
    15.620499351813308,
    14.422205101855956,
    16.97056274847714,
    40.049968789001575,
    63.52952069707436,
]

def calculate_distance(city1, city2):
    x1, y1 = cities[city1]
    x2, y2 = cities[city2]
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

def verify_solution():
    overall_calculated_cost = 0
    all_visited_cities = set()
    
    for index, tour in enumerate(tours):
        start_depot = tour[0]
        end_depot = tour[-1]
        
        # Requirement 1: Start and end at depot
        if start_depot != end_depot or start_depot != index:
            return "FAIL"
        
        # Calculate the travel cost from the tour
        calculated_cost = 0
        for i in range(len(tour) - 1):
            calculated_cost += calculate_distance(tour[i], tour[i+1])
            
        # Requirement 4: Calculate travel cost
        if not math.isclose(calculated_cost, travel_costs[index], rel_tol=0.001):
            return "FAIL"
        
        # Accumulate overall cost
        overall_calulated_cost += calculated_cost
        
        # Requirement 2: Track visited cities
        all_visited_cities.update(tour[1:-1])

    # Requirement 2: All cities visited once
    if all_visited_cities != set(range(8, 16)):
        return "FAIL"
    
    # Requirement 3: Minimize overall cost verification is analytical
    # Requirement 5: Output includes sequences and costs
    # Requirements 6, 7, 8, 9 are related to the algorithm's operation

    # Verify total cost for overall minimization
    expected_overall_cost = sum(travel_costs)
    if not math.isclose(overall_calulated_cost, expected_overalone_cost, rel_tol=0.001):
        return "FAIL"
    
    return "CORRECT"

# Run the verification
print(verify_solution())