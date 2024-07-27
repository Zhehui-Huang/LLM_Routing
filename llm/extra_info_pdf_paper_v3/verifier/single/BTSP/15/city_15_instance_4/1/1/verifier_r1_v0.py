import math

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_solution(tour, cities, total_cost, max_distance):
    # Verify the robot starts and ends at the depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify the robot visits each city exactly once (excluding the return to the depot)
    if len(set(tour)) != len(cities) or set(tour) != set(range(len(cities))):
        return "FAIL"
    
    # Calculate and compare the total travel cost and max distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    
    for i in range(len(tour) - 1):
        distance = calculate_euclidean_distance(cities[tour[i]], cities[tour[i + 1]])
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance

    # Compare calculated values with provided solution values
    if round(calculated_total_cost, 2) != total_cost:
        return "FAIL"
    if round(calculated_max_distance, 2) != max_distance:
        return "FAIL"
    
    return "CORRECT"

# City coordinates (indices correspond to city numbers)
cities = [
    (35, 40), (39, 41), (81, 30), (5, 50), 
    (72, 90), (54, 46), (8, 70), (97, 62), 
    (14, 41), (70, 44), (27, 47), (41, 74), 
    (53, 80), (21, 21), (12, 39)
]

# Given solution details
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
total_travel_cost = 337.84
max_travel_distance = 60.67

# Verify the solution
solution_status = verify_solution(tour, cities, total_travel_cost, max_travel_distance)
print(solution_status)