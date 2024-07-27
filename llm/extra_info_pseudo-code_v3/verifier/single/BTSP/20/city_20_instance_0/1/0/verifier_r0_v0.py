import math

def calculate_euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_solution(cities, tour, total_cost, max_distance):
    # Verify number of cities
    if len(cities) != 20:
        return "FAIL"
    
    # Verify start and end at depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify all cities visited exactly once except the depot (twice)
    visited = set(tour)
    if len(visited) != 20 or sorted(visited) != list(range(20)):
        return "FAIL"
    
    # Calculate the cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # Check if the given total cost and calculated matches
    if not math.isclose(calculated_total_cost, total_cost, abs_tol=0.001):
        return "FAIL"
    
    # Check if the given max distance and calculated matches
    if not math.isclose(calculated_max_distance, max_distance, abs_tol=0.001):
        return "FAIL"
    
    return "CORRECT"

# Defining cities based on coordinates
cities = [
    (8, 11), (40, 6), (95, 33), (80, 60), (25, 18), (67, 23), 
    (97, 32), (25, 71), (61, 16), (27, 91), (91, 46), (40, 87), 
    (20, 97), (5, 59), (61, 25), (62, 88), (13, 43), (61, 28), 
    (60, 63), (93, 15)
]

# Example output that needs to be verified
tour_example = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 0]
total_cost_example = 500  # Example value, set proper value after computation
max_distance_example = 50  # Example value, set proper value after computation

# Call the verification function
verification_result = verify_solution(cities, tour_example, total_cost_example, max_distance_example)
print(verification_result)