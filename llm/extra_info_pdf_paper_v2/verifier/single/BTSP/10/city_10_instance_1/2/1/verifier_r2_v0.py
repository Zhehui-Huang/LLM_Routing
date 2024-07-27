import math

# Cities and their coordinates
cities = {
    0: (53, 68),
    1: (75, 11),
    2: (91, 95),
    3: (22, 80),
    4: (18, 63),
    5: (54, 91),
    6: (70, 14),
    7: (97, 44),
    8: (17, 69),
    9: (95, 89)
}

# Provided solution
tour = [0, 5, 3, 8, 4, 6, 1, 7, 9, 2, 0]
total_travel_cost = 290.84
max_distance = 71.45

def calculate_euclidean_distance(city1, city2):
    return math.sqrt((city2[0] - city1[0])**2 + (city2[1] - city1[1])**2)

def verify_solution():
    # Verify there are 10 cities including the depot city
    if len(cities) != 10:
        return "FAIL"
    
    # Verify tour starts and ends at the depot city
    if tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Verify all cities are visited exactly once except the depot city
    if len(set(tour)) != len(cities) or tour.count(0) != 2:
        return "FAIL"
    
    # Calculate the actual total travel cost and max distance
    computed_total_cost = 0.0
    computed_max_distance = 0.0
    for i in range(len(tour)-1):
        city_index1 = tour[i]
        city_index2 = tour[i+1]
        distance = calculate_euclidean distance(cities[city_index1], cities[city_index2])
        computed_total_cost += distance
        computed_max_distance = max(computed_max_distance, distance)
    
    # Compare computed values with provided ones
    if not math.isclose(total_travel_cost, computed_total_cost, abs_tol=0.1):
        return "FAIL"
    if not math.isclose(max_distance, computed_max_disance, abs_tol=0.1):
        return "FAIL"
    
    # Check for triangle inequality
    for i in range(len(cities)):
        for j in range(i+1, len(cities)):
            for k in range(j+1, len(cities)):
                if not (calculate_euclidean_distance(cities[i], cities[j]) <=
                        calculate_euclidean_distance(cities[i], cities[k]) +
                        calculate_euclidean_distance(cities[k], cities[j])):
                    return "FAIL"
                    
    return "CORRECT"

# Output the result of the verification
print(verify_solution())