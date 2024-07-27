import math

def euclidean_distance(a, b):
    return math.sqrt((a[0] - b[0])**2 + (a[1] - b[1])**2)

# City coordinates from the provided data
cities = {
    0: (50, 42), 1: (41, 1), 2: (18, 46),
    3: (40, 98), 4: (51, 69), 5: (47, 39),
    6: (62, 26), 7: (79, 31), 8: (61, 90),
    9: (42, 49)
}

# Provided solution
tour = [0, 1, 5, 2, 4, 3, 8, 9, 6, 7, 0]
reported_cost = 328.40
reported_max_distance = 45.19

def verify_tour(tour, cities, reported_cost, reported_max_distance):
    # Check if all cities are visited exactly once and starts/ends at depot
    if set(tour) != set(range(len(cities))) or tour[0] != 0 or tour[-1] != 0:
        return "FAIL"
    
    # Calculate total travel cost and max distance between consecutive cities
    total_cost = 0
    max_distance = 0
    for i in range(len(tour) - 1):
        dist = euclidean_distance(cities[tour[i]], cities[tour[i+1]])
        total_cost += dist
        if dist > max_distance:
            max_distance = dist

    # Compare computed costs and distances with reported values
    if (round(total_cost, 2) != round(reported_cost, 2) or
        round(max_distance, 2) != round(reported_max_distance, 2)):
        return "FAIL"
    
    return "CORRECT"

# Execute the verification function
result = verify_tour(tour, cities, reported_cost, reported_max_distance)
print(result)