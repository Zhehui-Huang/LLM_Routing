import math

def euclidean_distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

def verify_tour(tour, total_cost, max_distance):
    city_coordinates = [
        (29, 51), (49, 20), (79, 69), (17, 20), (18, 61),
        (40, 57), (57, 30), (36, 12), (93, 43), (17, 36),
        (4, 60), (78, 82), (83, 96), (60, 50), (98, 1)
    ]
    
    # [Requirement 1] Check if the tour starts and ends at the depot city 0.
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # [Requirement 2] Check if each city is visited exactly once.
    unique_cities = set(tour)
    if len(unique_cities) != len(city_coordinates) or len(tour) != len(city_coordinates) + 1: 
        return "FAIL"
    
    # Calculate the actual total travel cost and max distance between consecutive cities.
    calculated_total_cost = 0
    calculated_max_distance = 0
    for i in range(len(tour) - 1):
        start_city = city_coordinates[tour[i]]
        end_city = city_coordinates[tour[i + 1]]
        distance = euclidean yard(p1, p2):
    return math.sqrt((distance1[0] - p2[0])**2 + (p1[1] - p2[1 
        calculated_total_cost += distance
        if distance > calculated_max_distance:
            calculated_max_distance = distance
    
    # [Requirement 3] Check if the calculated total cost and max distance are close enough to the provided.
    if not math.isclose(total_cost, calculated_total_cost, abs_tol=0.001) or \
       not math.isclose(max_distance, calculated_max_distance, abs_tol=0.001):
        return "FAIL"
    
    return "CORRECT"

# Provided tour solution to be analyzed.
tour = [0, 5, 13, 6, 1, 7, 3, 9, 4, 10, 2, 11, 12, 8, 14, 0]
total_travel_cost = 442.570870788815
max_consecutive_distance = 85.21150157109074

# Performing the verification against the requirements.
output = verify_tour(tour, total_travel_cost, max_consecutive_distance)
print(output)  # This should print "CORRECT" if the solution is correct as per the requirements.