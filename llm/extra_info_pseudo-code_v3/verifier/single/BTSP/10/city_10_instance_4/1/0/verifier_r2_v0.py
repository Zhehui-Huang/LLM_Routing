import math

def euclidean_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1) ** 2 + (y1 - y2) ** 2)

def verify_tour_requirement(tour, cities):
    # Check if the tour starts and ends at the depot city (city 0)
    requirement_1 = tour[0] == 0 and tour[-1] == 0

    # Check if each city is visited exactly once, except the depot city
    requirement_2 = sorted(tour[1:-1]) == list(range(1, len(cities)))

    # Calculate the total distance and the maximum distance between consecutive cities
    total_travel_cost = 0
    max_distance = 0
    for i in range(1, len(tour)):
        dist = euclidean_distance(cities[tour[i-1]][0], cities[tour[i-1]][1], cities[tour[i]][0], cities[tour[i]][1])
        total_travel_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Print total travel cost and maximum distance for verification against given
    print("Calculated total travel cost:", total_travel_cost)
    print("Calculated maximum distance:", max_distance)
    
    return requirement_1 and requirement_2, total_travel_cost, max_distance

def test_tour_solution():
    # Given city coordinates
    cities = {
        0: (79, 15),
        1: (79, 55),
        2: (4, 80),
        3: (65, 26),
        4: (92, 9),
        5: (83, 61),
        6: (22, 21),
        7: (97, 70),
        8: (20, 99),
        9: (66, 62)
    }
    
    # Given solution
    given_tour = [0, 1, 3, 4, 5, 7, 9, 8, 2, 6, 0]
    given_total_cost = 408.41
    given_max_distance = 61.68
    
    # Verify Requirements
    requirements_met, calculated_cost, calculated_max_distance = verify_tour_requirement(given_tour, cities)
    
    # Check calculated values with given values
    result = "CORRECT" if requirements_met and \
             abs(given_total_cost - calculated_cost) < 1e-2 and \
             abs(given_max_distance - calculated_max_distance) < 1e-2 else "FAIL"
    
    return result

# Run the test
print(test_tour_solution())