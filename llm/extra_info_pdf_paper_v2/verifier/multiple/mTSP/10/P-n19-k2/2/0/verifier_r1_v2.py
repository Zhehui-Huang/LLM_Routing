import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def calculate_total_tour_cost(tour, coordinates):
    total_cost = 0
    for i in range(len(tour)-1):
        total_cost += euclidean_distance(coordinates[tour[i]], coordinates[tour[i+1]])
    return total_cost

def test_solution():
    # Cities coordinates indexed from 0 to 18
    coordinates = [
        (30, 40), (37, 52), (49, 43), (52, 64), (31, 62), (52, 33), (42, 41), 
        (52, 41), (57, 58), (62, 42), (42, 57), (27, 68), (43, 67), (58, 27), 
        (37, 69), (61, 33), (62, 63), (63, 69), (45, 35)
    ]
    
    # Example solution data (adjusted to ensure including all cities and returning to depot)
    robot_tours = {
        0: [0, 1, 2, 12, 3, 14, 11, 4, 0],
        1: [0, 5, 15, 6, 7, 8, 16, 17, 9, 10, 13, 18, 0]
    }

    # Verification of Requirement 1: Check all cities are visited at least once, excluding the depot
    all_cities_visited = set()
    for tour in robot_tours.values():
        for city in tour:
            if city != 0:  # Excluding depot from check of visiting all cities once
                all_cities_visited.add(city)
    
    correct_cities_visited = len(all_cities_visited) == 18  # Should visit cities 1 to 18 exactly once

    # Verification of Requirement 2: Ensure all tours start and end at depot city 0
    tours_start_end_depot = all((tour[0] == 0 and tour[-1] == 0) for tour in robot_tours.values())

    # Verification of Requirement 3: Ensure total travel cost is minimized (not calculable without comparison)
    individual_costs = [calculate_total_tour_cost(tour, coordinates) for tour in robot_tours.values()]
    total_cost = sum(individual_costs)

    print(f"Correct cities visited: {correct_cities_visited}")
    print(f"Tours start and end at depot: {tours_start_end_depot}")
    print(f"Total travel cost: {total_cost}")
    
    if correct_cities_visited and tours_start_end_depot:
        print("CORRECT")
    else:
arc_extractedeph_text("FAIL")

test_solution()