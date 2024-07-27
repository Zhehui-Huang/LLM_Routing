import math

def euclidean_distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

def verify_tour_and_calculations(tour, coordinates, total_cost_claim, max_distance_claim):
    # Requirement 1: Starts and ends at depot city 0
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Requirement 2: Visits each city exactly once (excluding the repeat of the depot city)
    unique_cities = set(tour[1:-1])
    if len(unique_cities) != 15 or set(range(1, 15)) != unique_cities:
        return "FAIL"
    
    # Calculate total distance and maximum consecutive distance
    calculated_total_cost = 0
    calculated_max_distance = -float('inf')
    
    for i in range(1, len(tour)):
        distance = euclidean_distance(coordinates[tour[i-1]], coordinates[tour[i]])
        calculated_total_cost += distance
        calculated_max_distance = max(calculated_max_distance, distance)

    # Requirement 3: Minimize the longest distance between consecutive cities
    if abs(calculated_total_cost - total_cost_claim) > 0.01 or abs(calculated_max_distance - max_distance_claim) > 0.01:
        return "FAIL"
    
    return "CORRECT"

# Coordinates of each city including depot
coordinates = [
    (35, 40),  # City 0
    (39, 41),  # City 1
    (81, 30),  # City 2
    (5, 50),   # City 3
    (72, 90),  # City 4
    (54, 46),  # City 5
    (8, 70),   # City 6
    (97, 62),  # City 7
    (14, 41),  # City 8
    (70, 44),  # City 9
    (27, 47),  # City 10
    (41, 74),  # City 11
    (53, 80),  # City 12
    (21, 21),  # City 13
    (12, 39)   # City 14
]

# Provided solution details
tour = [0, 1, 10, 8, 14, 3, 6, 11, 12, 4, 7, 9, 5, 2, 13, 0]
total_travel_cost = 337.84
maximum_distance = 60.67

# Perform the verification
result = verify_tour_and_calculations(tour, coordinates, total_travel_cost, maximum_distance)
print(result)