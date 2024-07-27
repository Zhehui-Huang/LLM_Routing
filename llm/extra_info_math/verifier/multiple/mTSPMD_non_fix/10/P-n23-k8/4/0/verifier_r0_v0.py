import numpy as np

# Cities and their coordinates
cities = {
    0: (30, 40), 1: (37, 52), 2: (49, 49), 3: (52, 64), 4: (31, 62), 5: (52, 33),
    6: (42, 41), 7: (52, 41), 8: (57, 58), 9: (62, 42), 10: (42, 57), 11: (27, 68),
    12: (43, 67), 13: (58, 48), 14: (58, 27), 15: (37, 69), 16: (38, 46), 
    17: (61, 33), 18: (62, 63), 19: (63, 69), 20: (45, 35), 21: (32, 39), 22: (56, 37)}

# Number of salesmen and tours given
num_salesmen = 8
tours = [
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 0],
    [0, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
]

# Utility function to compute Euclidean distance
def euclidean_distance(city1, city2):
    return np.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)

# Check each rule and requirement
def verify_solution(tours, num_salesmen):
    # Collect information about visits and tours
    tour_flattened = [city for tour in tours for city in tour[1:-1]]
    unique_cities = set(tour_flattened)
    
    # Check if each city is visited exactly once
    if not all(tour_flattened.count(city) == 1 for city in set(range(1, 23))):
        return "FAIL"
    
    # Each city visited once
    if len(unique_cities) != 22:  # We have 23 cities minus 1 depot
        return "FAIL"

    # Calculate the departures and returns for each depot in the tours
    departures = [0] * num_salesmen
    returns = [0] * num_salesmen
    all_cities_covered = set()

    for idx, tour in enumerate(tours):
        if tour[0] != tour[-1]:  # Start and end must be the same
            return "FAIL"
        if tour[0] != 0:  # All tours should start and end at depot 0, in this simplified problem
            return "FAIL"

        departures[tour[0]] += 1
        returns[tour[-1]] += 1

        for i in range(len(tour) - 1):
            c_from, c_to = tour[i], tour[i+1]
            segment_length = euclidean_distance(cities[c_from], cities[c_to])
            if segment_length == 0:  # Check for movement (min K and L)
                return "FAIL"
            all_cities_covered.add(c_from)
            all_cities_covered.add(c_to)

        # Check specific tour length
        if tour[0] == 0 and not (len(tour) >= 2):  # K, min number of nodes covered implied by problem
            return "FAIL"

    # Ensuring m_i salesmen leave and return to each depot i from depot set D
    if departures[0] != num_salesmen or returns[0] != num_salesmen:
        return "FAIL"

    if all_cities_covered != set(range(23)):
        return "FAIL"

    return "CORRECT"

# Print the result of verification
result = verify_solution(tours, num_salesmen)
print(result)