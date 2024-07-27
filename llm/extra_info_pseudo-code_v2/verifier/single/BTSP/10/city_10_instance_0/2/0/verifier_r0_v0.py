import math

# Euclidean distance calculator
def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

# Test data and solution
cities = {
    0: (50, 42),
    1: (41, 1),
    2: (18, 46),
    3: (40, 98),
    4: (51, 69),
    5: (47, 39),
    6: (62, 26),
    7: (79, 31),
    8: (61, 90),
    9: (42, 49)
}

solution_tour = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
reported_total_cost = 365.33
reported_max_distance = 61.68

# Unit tests for the robot tour
def test_robot_tour():
    # Verify if the solution tour starts and ends at the depot city 0
    start_at_depot = solution_tour[0] == 0
    end_at_depot = solution_tour[-1] == 0
    
    # Verify if each city is visited exactly once
    unique_cities_once = all(solution_tour.count(city) == 1 for city in range(10))
    
    # Compute the total travel cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(solution_tour) - 1):
        d = euclidean_distance(cities[solution_tour[i]], cities[solution_tour[i+1]])
        total_cost += d
        if d > max_distance:
            max_distance = d
            
    # Verify total cost and max distance with given results
    costs_within_tolerance = abs(total_cost - reported_total_cost) < 1e-2
    max_distance_within_tolerance = abs(max_distance - reported_max_distance) < 1e-2
    
    print("Start at Depot:", start_at_depot)
    print("End at Depot:", end_at_depot)
    print("Unique and Once Visit:", unique_cities_once)
    print("Total Travel Cost (Calculated vs Reported):", total_cost, reported_total_cost)
    print("Maximum Distance (Calculated vs Reported):", max_distance, reported_max_distance)
    
    # Final correctness check
    if all([start_at_depot, end_at_depot, unique_cities_once, costs_within_tolerance,
            max_distance_within_tolerance]):
        print("CORRECT")
    else:
        print("FAIL")

# Run the test
test_robot_tour()