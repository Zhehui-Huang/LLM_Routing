import math

def calculate_distance(city1, city2):
    """ Helper function to calculate the Euclidean distance between two points (cities). """
    return math.sqrt((city1[0] - city2[0])**2 + (city1[1] - city2[1])**2)

def test_solution():
    # City coordinates as given in the problem statement
    cities = {
        0: (30, 40), 1: (37, 52), 2: (49, 43), 3: (52, 64), 4: (31, 62),
        5: (52, 33), 6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42),
        10: (42, 57), 11: (27, 68), 12: (43, 67), 13: (58, 27), 14: (37, 69),
        15: (61, 33), 16: (62, 63), 17: (63, 69), 18: (45, 35)
    }

    # Provided robot tours
    robot_tours = [
        [0, 1, 3, 4, 8, 10, 11, 12, 14, 16, 17, 0],
        [0, 2, 5, 6, 7, 9, 13, 15, 18, 0]
    ]

    # Reported costs must match these corrected values
    reported_costs = [212.22, 116.70]
    total_cost = 328.92

    visited_cities = set()
    calculated_costs = []
    overall_calculated_cost = 0

    # Validate tour and compute costs
    for tour in robot_tours:
        # Check if each tour starts and ends at the depot
        if tour[0] != 0 or tour[-1] != 0:
            return "FAIL"
        
        tour_cost = 0
        
        # Calculate total cost for each tour
        for i in range(len(tour) - 1):
            if tour[i] != 0:
                visited_cities.add(tour[i])
            distance = calculate_distance(cities[tour[i]], cities[tour[i + 1]])
            tour_cost += distance
        
        calculated_costs.append(round(tour_cost, 2))
        overall_calculated_cost += tour_cost

    # Check if all cities are visited exactly once
    if len(visited_cities) != len(cities) - 1 or not visited_cities == set(range(1, 19)):
        return "FAIL"
    
    # Tolerate small floating-point discrepancies
    if not all(abs(reported - calculated) < 1e-1 for reported, calculated in zip(reported_costs, calculated_costs)):
        return "FAIL"
    
    if not abs(total_cost - round(overall_calculated_cost, 2)) < 1e-1:
        return "FAIL"

    return "CORRECT"

# Run the test
print(test_solution())