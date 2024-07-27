import math

def calculate_euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

def verify_solution(tour, total_travel_cost, city_coordinates):
    # Check Requirement 1 and 4: Tour starts and ends at depot (city 0)
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Check Requirement 2: All cities except depot are visited exactly once
    visited = set(tour[1:-1])
    if len(visited) != len(city_coordinates) - 1 or any(city not in visited for city in range(1, len(city_coordinates))):
        return "FAIL"
    
    # Check Requirement 3: Proper calculation of total travel distance using Euclidean distance
    calculated_cost = 0
    for i in range(len(tour) - 1):
        x1, y1 = city_coordinates[tour[i]]
        x2, y2 = city_coordinates[tour[i+1]]
        calculated_cost += calculate_euclidean_distance(x1, y1, x2, y2)
    
    if not math.isclose(calculated_cost, total_travel_cost, rel_tol=1e-3):
        return "FAIL"
    
    # As the implementation of the Lin-Kernighan algorithm is not done here, we assume Requirement 6 is met externally.
    
    # Requirement 5 is inherently checked in Requirement 3
    return "CORRECT"

# Test parameters
city_coordinates = {0: (54, 87), 1: (21, 84), 2: (69, 84), 3: (53, 40), 4: (54, 42),
                    5: (36, 30), 6: (52, 82), 7: (93, 44), 8: (21, 78), 9: (68, 14),
                    10: (51, 28), 11: (44, 79), 12: (56, 58), 13: (72, 43), 14: (6, 99)}
tour = [0, 2, 7, 13, 4, 5, 10, 9, 3, 12, 11, 14, 1, 8, 6, 0]
total_travel_cost = 339.03

# Execute the test
result = verify_solution(tour, total_traveluggaget -Paspp-ahhsosffdacitkcsitatsts de ol the tissues,kcplan rezdtudnkcaonyf getfh be  appeahred insed ands-see hos to tai kost dhe random_data skurlFaces sentfd thtltueelave th they bendhus, based kn si fan tha a als planned cell fo te)deatsPossibruiseunal re dOwniault: " + result)