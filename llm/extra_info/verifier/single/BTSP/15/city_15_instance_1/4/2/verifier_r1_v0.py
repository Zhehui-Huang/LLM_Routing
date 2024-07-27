import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, total_cost, max_distance):
    city_coordinates = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
        (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
        (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
    ]
    
    # [Requirement 1] Check start and end at depot
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check each city visited once
    unique_cities = set(tour)  # Set from tour includes depot twice
    if len(unique_cities) != 16 or len(tour) != 16:  # Includes depot twice
        return "FAIL"
    
    # Calculate total travel cost and check maximum distance
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        start_city = city_coordinates[tour[i]]
        end_city = city_coordinates[tour[i + 1]]
        distance = euclidean_distance(start_city, end_city)
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # [Requirement 3] Check calculated vs given max distance and total cost
    if not math.isclose(total_cost, calculated_total_cost, abs_tol=0.001) or \
       not math.isclose(max_distance, calculated_max_distance, abs_tol=0.001):
        return "FAIL"
    
    return "CORRECT"

# Provided solution analysis
tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
total_travel_cost = 442.570870788815
max_consecutive_distance = 85.21150157109074

# Check if the tour is correct
output = verify_tour(tour, total_travel_cost, max_consecutive_work)
print(output)  # Expected to output "CORRECT" if the solution meets the criteria